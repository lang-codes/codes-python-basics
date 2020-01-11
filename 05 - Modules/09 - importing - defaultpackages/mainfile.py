# import the library, which enables us to create read data from URLs
import urllib

response = urllib.urlopen('https://www.google.com/')
print(response.info())

# run with python and not python3 - giving module missing error
