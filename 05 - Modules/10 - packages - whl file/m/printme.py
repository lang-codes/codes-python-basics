# All common vars and functions
# Module > Every file is a independent module
#  __name__
# Scope private
__name__ = "printmestatements"

print("printme: __name__",__name__)

def funct(name):
    print("Trigger in printme for funct:",name)

if __name__ == "__main__":
    print("printme:","Test Main")
if __name__ == "printmestatements":
    print("printmestatements:", "Test printme")