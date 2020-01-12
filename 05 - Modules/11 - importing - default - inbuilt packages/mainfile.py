# HEAD
# Modules - Using inbuilt python library or external installed library
# DESCRIPTION
# Describes the import of library, which enables us to create read 
#           data from URLs
# RESOURCES
# 

# import the library, which enables us to create read 
#           data from URLs
import urllib

response = urllib.urlopen('https://www.google.com/')
print(response.info())

# run this file with python 2.x and not python3 - giving module 
#           missing error for python 3.x
