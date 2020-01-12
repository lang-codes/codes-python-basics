# HEAD
# Class Tree Traversal
# DESCRIPTION
# Describes the inheritance tree using namespace links,
#       displaying higher superclasses with 
#       indentation for height


# Print the class name and attributes and properties and methods
def classtree(cls, indent, print_str, cls_str):
    print('.' * indent + cls.__name__)
    cls_str.setdefault("__name__", str(cls.__name__))
    if print_str == True:
        print('.' * indent + str(tuple(cls.__dict__.keys())))
        cls_str.setdefault("__dict__", str(tuple(cls.__dict__.keys())))
    for supercls in cls.__bases__:
        classtree(supercls, indent + 4, print_str, cls_str)
    return cls_str

# Print the instance tree structure for a class
def instancetree(inst, print_str):
    print('Tree of %s' % inst)
    return classtree(inst.__class__, 4, print_str, {})

# Get the structure classes passed as keyword arguments
def get_structure(**kwargs):
    res = []
    print_str = kwargs.get('print_str')
    for key in kwargs.keys():
        if key != 'print_str':
            if print_str == True:
                res.append(
                        instancetree(kwargs[key](), print_str)
                    )
            elif print_str == False or print_str == None:
                res.append(
                        instancetree(kwargs[key](), print_str=False)
                    )
    return tuple(res)


if __name__ == '__main__':

    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(B, C):
        pass
    class E:
        pass
    class F(D, E):
        def method(self):
            pass

    # Module USAGE: Structure print for classes
    structure = get_structure(A=A, B=B, C=C, D=D, E=E, F=F, print_str=False)
    print(structure)
