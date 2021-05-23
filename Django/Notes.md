## Installation

- First of all install python 
- check the python latest version using `python --version` command
  
### Install Django globally using command
- `py -m pip install Django`
- run `django-admin` command to check django is successfully installed
- now run `py -m django --version` to check version
  
### Installing django in a separate virtual environment
- `py -m venv project-name` -This will create a folder called ‘project-name’ if it does not already exist and setup the virtual environment(development server)
- here project-name is our virtual environment 
- `project-name\Scripts\activate.bat`-The virtual environment will be activated and you’ll see “(project-name)” next to the command prompt to designate that. Each time you start a new command prompt, you’ll need to activate the environment again

- Now install django here using the django installation commands
  `py -m pip install Django`
- Now we can run `django-admin` or `django-admin --version` command to check whether django is working or not

- run `deactivate` to deactivate the virtual environment
### Start django project
Now I will use the globally installed django.
Navigate to the folder where we want to create project
 use `django-admin startproject project-name`
 a project-name folder along with manage.py is created
- For now we'll only edit url(all newly created pages will be registered here) and settings file(contain global setting for our project)


- Now we will set the development environment for our project or setup local development server which allow us to preview our application which we are working on
` python manage.py runserver`

- So now we had created our main project, within our project we will create several apps(all apps combine to form a single project), we can consider an app as a module
`python manage.py startapp challenges`(challenges is app name)




