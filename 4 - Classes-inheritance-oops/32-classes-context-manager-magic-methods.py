# Describes the magic methods of classes
# https://rszalski.github.io/magicmethods/

# Context Managers

# In Python 2.5, a new keyword was introduced in Python along with a new method for code reuse: the with statement. The concept of context managers was hardly new in Python (it was implemented before as a part of the library), but not until PEP 343 was accepted did it achieve status as a first-class language construct. You may have seen with statements before:

# with open('foo.txt') as bar:
#     # perform some action with bar

# Context managers allow setup and cleanup actions to be taken for objects when their creation is wrapped with a with statement. The behavior of the context manager is determined by two magic methods:

# __enter__(self)
#     Defines what the context manager should do at the beginning of the block created by the with statement. Note that the return value of __enter__ is bound to the target of the with statement, or the name after the as.
# __exit__(self, exception_type, exception_value, traceback)
#     Defines what the context manager should do after its block has been executed (or terminates). It can be used to handle exceptions, perform cleanup, or do something always done immediately after the action in the block. If the block executes successfully, exception_type, exception_value, and traceback will be None. Otherwise, you can choose to handle the exception or let the user handle it; if you want to handle it, make sure __exit__ returns True after all is said and done. If you don't want the exception to be handled by the context manager, just let it happen.

# __enter__ and __exit__ can be useful for specific classes that have well-defined and common behavior for setup and cleanup. You can also use these methods to create generic context managers that wrap other objects. Here's an example:

# class Closer:
#     '''A context manager to automatically close an object with a close method
#     in a with statement.'''

#     def __init__(self, obj):
#         self.obj = obj

#     def __enter__(self):
#         return self.obj # bound to target

#     def __exit__(self, exception_type, exception_val, trace):
#         try:
#            self.obj.close()
#         except AttributeError: # obj isn't closable
#            print 'Not closable.'
#            return True # exception handled successfully

# Here's an example of Closer in action, using an FTP connection to demonstrate it (a closable socket):

# >>> from magicmethods import Closer
# >>> from ftplib import FTP
# >>> with Closer(FTP('ftp.somesite.com')) as conn:
# ...     conn.dir()
# ...
# # output omitted for brevity
# >>> conn.dir()
# # long AttributeError message, can't use a connection that's closed
# >>> with Closer(int(5)) as i:
# ...     i += 1
# ...
# Not closable.
# >>> i
# 6

# See how our wrapper gracefully handled both proper and improper uses? That's the power of context managers and magic methods. Note that the Python standard library includes a module contextlib that contains a context manager, contextlib.closing(), that does approximately the same thing (without any handling of the case where an object does not have a close() method).
