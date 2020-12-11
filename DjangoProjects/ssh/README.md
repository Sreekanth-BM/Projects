# Server Management
This Django application helps on automating tasks on servers.

#### Supports:
- Linux [SSH->Paramiko]
  - Provide the list of servers and command to execute.
  - Output is displayed and can also export to csv file.
- Windows [Winrm]
  - Provide the list of servers and a command to execute.
  - Output is displayed and can also export to csv file.


#### How to run this application
- Please add 'server name' to ALLOWED_HOSTS list in [settings.py](https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts) file
- Browse `http://<hostname>:8000` to start application, here hostname is the server name, on which you run this project
- Run: `python3 manage.py runserver 0.0.0.0:8000`, where [manage.py](https://docs.djangoproject.com/en/3.0/ref/django-admin/) file exists in this project root directory
