import socket
from functools import partial
import requests
from django.shortcuts import render, redirect
import subprocess
import concurrent.futures
import re
import paramiko
import pandas as pd

def sshing(username,password,group_name,timer,server):
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', None)
  pd.set_option('display.max_colwidth', None) 

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  h = server.strip()
  command = "sudo -S /opt/chef/embedded/bin/chef-client -v"
  try:
    #Ping Check
    status = "Failed"
    try:
      ping_status = subprocess.check_output("fping %s"%(h),shell=True,universal_newlines=True)
    except:
      output = "Ping Failed"
    else:
      try:
        ssh.connect(hostname=h,username=username,password=password,timeout=9)
      except paramiko.ssh_exception.AuthenticationException:
        output = "Authentication Failed"
      except paramiko.ssh_exception.NoValidConnectionsError:
        output = "Connection Refused"
      except socket.gaierror:
        output = "Not in SISM"
      except (socket.timeout, paramiko.ssh_exception.SSHException):
        output = "SSH Failed"
      except:
        output = "SSH Failed"
      else:
        try:
          stdin,stdout,stderr = ssh.exec_command("%s"%(command),timeout=100) 
          stdin.write("%s\n"%(password))
          stdin.flush()
          output, error = stdout.readlines(), stderr.readlines()
          if len(output) == 0:
            output = ''.join([x.strip() for x in error])
          else:
            output = ''.join([x.strip() for x in output])
            match = re.search('.*Chef\s*:\s*14.\d+.\d+',output)
            if match:
              status = "CHEF Version 14"
            else:
              status = "Not CHEF Version14"
        except socket.timeout:
          output =  "CMD Execution TimedOut"
        except socket.error:
          output = "OS Error"
    finally:
      s1 = pd.Series({h:output})
      s2 = pd.Series({h:status})
      dataframe = pd.DataFrame({'Output':s1,'Status':s2})
      return dataframe
  except:
    return "Something wrong in execution"
  

def sshing_view(request):
  if request.method == 'POST':
    server = request.POST['server']
    username,password,group_name = get_details(request)
    timer = 20
    output = sshing(username,password,group_name,timer,server)
    print(output)
    context = {
	'cv_solo_output':output
	} 
    return render(request,'chefversion/chefversion_output.html',context)

def multi_sshing_view(request):
  if request.method == 'POST':
    servers = request.FILES['server_file']
    username,password,group_name = get_details(request)
    hosts_list = []
    output = []
    timer = 20
    for host in servers:
      host = str(host,'utf-8').strip()
      hosts_list.append(host)
    func = partial(sshing,username,password,group_name,timer)
    with concurrent.futures.ThreadPoolExecutor() as e:
      for i in e.map(func,hosts_list):
         output.append(i)
    return render(request,'chefversion/chefversion_output.html',{'cv_multi_output':output})
      
def get_details(request):
  username = request.POST['username']
  password = request.POST['password']
  group_name = request.POST['groupname']
  return username.strip(),password.strip(),group_name.strip()
