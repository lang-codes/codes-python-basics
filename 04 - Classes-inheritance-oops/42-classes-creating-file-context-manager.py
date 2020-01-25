# HEAD
# File Context Manager
# DESCRIPTION
# 
# RESOURCES

class File:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file   
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with File('some_file.txt') as f:
    f.write('blah blah...')
