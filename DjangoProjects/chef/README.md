### **[CHEF](https://docs.chef.io/)** :)

#### **Requirements:**
1. CHEF Starter kit
2. Python3
3. Django


#### **Manages:**
1. KnifeStatus
2. Runlists
3. Chef Version

- **KnifeStatus** :
  - Fetches you reporting/not-reporting servers and hostnames for servers on CHEF

- **Runlists**:
  - Login is required to manage Run-list
  - Add/remove cookbooks to/from Run-list

- **CHEF Version**:
  - Login is required to access this module.
  - Finds chef-client version for given servers and sends data to splunk.

#### **How to run this project**

- Prior running below command, ensure '.chef'(Starter kit) directory exists along with this project

- Run: `python3 manage.py runserver 0.0.0.0:8000`, where [manage.py](https://docs.djangoproject.com/en/3.0/ref/django-admin/) file exists in this project root directory

- Above directories should be on same line/path

      .chef(Starter kit)
      chef (Project)

- Please add 'hostname' to ALLOWED_HOSTS list in [settings.py](https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts) file

- Browse `http://<hostname>:8000` to start application, here hostname is the server name, on which you run this project

