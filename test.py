# Generate README.md file

import os
path = './'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
        for file in f:
            print("t", str(file))
            if not len(r.split('.git')) >= 2 and not len(r.split('__pycache__')) >= 2:
                files.append(os.path.join(r, file))
with open("./README.md", mode="w", encoding="utf8") as f:
    f.write("""
* PYTHON DEMO CODES


> These are set of codes intended to demostrate the most commonly used syntax usage with codes. They cover the most common use + implementation cases for most concepts and built in functionality. If you have more to add please do send a pull request.
    
    """ + '\n')
    for fl in files:
        print('[{0}]({0})'.format(fl.lstrip('.')))
        f.write("""

* Topic 

""".format(fl.lstrip('.')))
        f.write("""[{0}](https://github.com/python-demo-codes/basics/blob/master{1})""".format(fl, fl.lstrip('.').replace(" ","%20")) + '\n\r')
