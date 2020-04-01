import pandas as pd
from functools import partial
import concurrent.futures
import subprocess
from django.shortcuts import render
import requests

def append_to_runlist(action,cb,h):#,saveinto):
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', None)
  pd.set_option('display.max_colwidth', None)
  try:
    output = subprocess.check_output("knife node run_list %s %s recipe[%s]"%(action,h,cb),shell=True)
    output = str(output,'utf-8').strip()
    status = "Successful"
  except Exception as e:
    output = e
    status = "Not successful"
  print(output)
  s1 = pd.Series({h:output})
  s2 = pd.Series({h:status})
  dataframe = pd.DataFrame({'Runlist':s1,'Status':s2})
  print(dataframe)
  return dataframe

def solo_input(request):
  try:
    if request.method == 'POST':
      h = request.POST['host_input']
      cookbook_name = request.POST['cookbook']
      action_to_do = request.POST['action']
      h = h.strip() #type<h> : str
      cookbook_name = cookbook_name.strip()
      action_to_do = action_to_do.strip()
      appended=append_to_runlist(h=h,cb=cookbook_name,action=action_to_do)
      context={
	"runlist_solo_output_content":appended
      }
      return render(request,'runlists/runlists_output.html',context)
  except Exception as e:
    print(e)
    context={
      "data":"Error Occured"
    }
    return render(request,'runlists/error.html',context)

def file_input(request):
  try:
    if request.method == 'POST':
      uploaded_file = request.FILES['f1']
      cookbook_name = request.POST['cookbook']
      action_to_do = request.POST['action']
      action_to_do = action_to_do.strip()
      cookbook_name = cookbook_name.strip()
      hosts_list = [] #array of servers from input file
      output_data = []
      uploaded_filename = uploaded_file.name
      for host in uploaded_file:
        host = str(host,'utf-8').strip()
        hosts_list.append(host)
      print(action_to_do)
      func = partial(append_to_runlist,action_to_do,cookbook_name)
      with concurrent.futures.ThreadPoolExecutor() as e:
        for i in e.map(func,hosts_list):
          output_data.append(i)
      context={
        "output_content":output_data
      }
      return render(request,'runlists/runlists_output.html',context)
  except Exception as e:
    print(e)
    context={
      "data":"Error Occured"
    }
    return render(request,'runlists/error.html',context)
