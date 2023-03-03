# Insurance_Project

### This repository is the complete guideline for any Datascience enthusiast to develope end to end project

### to create enviornment for any DS project
```
conda create --prefix ./env python=3.9 -y
```
### to activate environment
```
conda activate ./env
```
### In this project everything done on the cloud

### to create any file using git bash
```
touch filename
```
# data_dump.py file created in which we will dump our data in mongodb database
# data inserted to database

### creating script to get all the required files in our project

### template.py created it will be used as generic file for any project to develope

# setup.py file is created. It shows which version of our project we are going to publish.

1. how to write setup.py file?

ans: go to the below provided link
'''
https://docs.python.org/3/distutils/setupscript.html
'''
In this setup.py, version is the most important parameter. You have to change the version
as many times as you want to release the new version of your project.

In this setup.py, author_email is the parameter in which we have to mention from 
where we have to fetch our data. for this project i have to give the email id associated 
with my github rofile.

In this setup.py, packages is the parameter It will find packages for each __init__.py file in our project

# In the requirements.txt file we will assign install the required packages for our project

In that above mentioned file there is a -e . is there which means,
1. -e -> editable mode 
2. . -> current directory 

# now our work flow shold concentrate on logging file and exception file
1. create a folder exception 
'''
mkdir E:\\Insurance_Project\\Insurance_Project
'''
2. Within exception folder create __init__.py
'''
touch E:\\Insurance_Project\\Insurance_Project\\exception\\__init__.py
'''
2. coding started for init file in logging folder and exception folder

'''
https://docs.python.org/3/howto/logging.html
'''
# time to work in main.py to check our logger and exception