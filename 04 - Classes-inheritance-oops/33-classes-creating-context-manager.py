# HEAD
# File Context Manager
# DESCRIPTION
# 
# RESOURCES

class ContextManager():
    def __init__(self):
        print('init method called')
    def __enter__(self):
        print('enter method called')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')

