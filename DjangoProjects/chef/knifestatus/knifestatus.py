from functools import partial
from django.template.defaultfilters import linebreaksbr
import pandas as pd
import concurrent.futures
import subprocess
from django.shortcuts import render
import requests

def classify_view(request):
  return render(request,'knifestatus/ks_classify.html')

def dataframe_knifestatus(output):
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', None)
  pd.set_option('display.max_colwidth', None)
  output = str(output,'utf-8')
  all_hosts = output.split('\n')
  dict_all_hosts, platform_all_hosts, time_all_hosts = {},{},{}
  reports = ['minute','hour','second']
  for host in all_hosts:
    if "hours" in host:
      status = "Not Reporting"
      hostname = host.split(',')[1].strip()
      platform = host.split(',')[2].strip()
      time = host.split(',')[0].strip()
    elif any(x in host for x in reports):
      status = "Reporting"
      hostname = host.split(',')[1].strip()
      platform = host.split(',')[2].strip()
      time = host.split(',')[0].strip()
    elif len(host) == 0:
      continue
    else:
      status = "Node not converged"
      hostname = host.split(' ')[1].strip()
      platform = "linux" if 'l' in hostname else "windows"
      time = "No handshake yet"
    dict_all_hosts[hostname]=status
    platform_all_hosts[hostname] = platform
    time_all_hosts[hostname] = time

  series = pd.Series(dict_all_hosts)
  platform_series = pd.Series(platform_all_hosts)
  time_series = pd.Series(time_all_hosts)
  ks_dataframe = pd.DataFrame({'Status':series,'Platform':platform_series,'Time':time_series})
  return ks_dataframe  

def classification_view(request):
  output = subprocess.check_output("knife status",shell=True)
  ks_dataframe =  dataframe_knifestatus(output)  
  return render(request,'knifestatus/knifestatus_output.html',{'knifestatus_report':ks_dataframe})

def finds_knifestatus(h):
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', None)
  pd.set_option('display.max_colwidth', None)
  reports = ['minute','hour','second']
  try:
    host = h.split('.')[0]
    output = subprocess.check_output("knife status 'name:%s*' OR 'name:%s*'"%(host.lower(),host.upper()),shell=True)
    output = str(output,'utf-8').strip()
    # Classify status
    if "hours" in output:
      status = "Not reporting"
      chef_name = output.split(',')[1].strip()
    elif any(x in output for x in reports):
      status = "Reporting"
      chef_name = output.split(',')[1].strip()
    else:
      output = "Node not found"
      status = "Not found"
      chef_name = "Not found"
  except Exception as e:
    output = e
    status = "Error"
    chef_name ="Error"

  s1 = pd.Series({h:output})
  s2 = pd.Series({h:status})
  s3 = pd.Series({h:chef_name})
  dataframe = pd.DataFrame({'KnifeStatus':s1,'Status':s2,'CHEF_Hostnames':s3})
  return dataframe

def solo_input(request):
  try:
    if request.method == 'POST':
      criteria = request.POST['criteria']
      criteria = criteria.strip()
      output = subprocess.check_output("knife status '%s'"%(criteria),shell=True)
      ks_data=dataframe_knifestatus(output)
      context={
	"ks_solo_output_content":ks_data
      }
      return render(request,'knifestatus/knifestatus_output.html',context)
  except Exception as e:
      print(e)
      context={
        "data":"Error Occured"
      }
      return render(request,'knifestatus/error.html',context)

def file_input(request):
  try:
    if request.method == 'POST':
      uploaded_file = request.FILES['f1']
      hosts_list = [] #array of servers from input file
      output_data = []
      uploaded_filename = uploaded_file.name
      for host in uploaded_file:
        host = str(host,'utf-8').strip()
        hosts_list.append(host)
      with concurrent.futures.ThreadPoolExecutor() as e:
        for i in e.map(finds_knifestatus,hosts_list):#,uploaded_filename):
          output_data.append(i)
      context={
        "output_loc":"/tmp/DJ/outputs/knifestatus/ks_%s"%(uploaded_file.name),
        "output_content":output_data
      }
    return render(request,'knifestatus/knifestatus_output.html',context)
  except Exception as e:
    print(e)
    context={
      "data":"Error Occured"
    }
    return render(request,'knifestatus/error.html',context)
