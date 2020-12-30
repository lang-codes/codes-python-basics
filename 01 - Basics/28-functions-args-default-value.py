# HEAD
# Python Functions - providing default value for
#           argument in function definition
# DESCRIPTION
# Describes
#       Creating arguments with default value in function definition
# 
# RESOURCES
#


# Default values for arguments can be assigned
#       in declaration/definition of function
# Assigning default values for arguments
#       in definition of function


def helloDefaultValue(name="Default Value"):
    print('2. helloDefaultValue ' + name)


# Default value of argument will be used
helloDefaultValue()


# Passed value will be used instead of default
helloDefaultValue("Passed value used instead of default value")

