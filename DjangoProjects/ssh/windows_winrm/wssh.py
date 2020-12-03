import subprocess
import pandas as pd
import concurrent.futures
from getpass import getpass
import winrm
import os
from functools import partial # for paraller execution
import requests
from django.shortcuts import render, redirect

def winrming(username,password,command,host):
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', None)
  pd.set_option('display.max_colwidth', None)
  try:
    prot = winrm.protocol.Protocol(endpoint = "http://%s:5985/wsman"%(host.strip()),transport = 'ntlm',username = username.strip(),password = password.strip(),server_cert_validation = 'ignore')
    shell = prot.open_shell()
  except:
    output = '-'
    status = 'SSH Failed'
  else:
    try:
      command = prot.run_command(shell,command)
      output,error,status = prot.get_command_output(shell,command)
      output = str(output,'utf-8').strip()
      error = str(error,'utf-8').strip()
      # Error occured
      if len(output) == 0:
        output = error
        status = 'Error'
      else:
        status = 'Success'
    except:
      status = 'Unable to run command'
      output = '-'
  finally:
    host = host.strip()
    output = pd.Series({host:output})
    status = pd.Series({host:status})
    dataframe = pd.DataFrame({'Output':output,'Status':status})
    return dataframe
  

def solo_winrming(request):
  if request.method == 'POST':
    server = request.POST['server']
    username,password,command= get_details(request)
    output = winrming(username,password,command,server)
    context = {
	'windows_solo_output':output
	} 
    return render(request,'windows_winrm/wssh.html',context)

def multi_winrming(request):
  if request.method == 'POST':
    servers = request.FILES['server_file']
    username,password,command = get_details(request)
    hosts_list = []
    output = []
    for host in servers:
      host = str(host,'utf-8').strip()
      hosts_list.append(host)
    func = partial(winrming,username,password,command)
    with concurrent.futures.ThreadPoolExecutor() as e:
      for i in e.map(func,hosts_list):
         output.append(i)
    return render(request,'windows_winrm/wssh.html',{'windows_multi_output':output})
      
def get_details(request):
  username = request.POST['username']
  password = request.POST['password']
  command = request.POST['command']
  return username.strip(),password.strip(),command.strip()

