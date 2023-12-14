# Packages Are Modules
# But Modules are not necessarily packages

# A module is a package but it must have a value set for __path__
# after you have imported a module you can easily see if that module is a package by inspecting the __path__ attribute

try:
    import math

    print(math.__path__)
except AttributeError:
    print("math is not a package")

# Modules do not have to be entities in a file system
# loaders, finders
# by the same token this applies to packages
# even tho' they usually are

# packages represent a hiearchy of modules / packages

# try:
# import pack1.mod1
# import pack1.pack1_1.mod1_1
# dotted notation indicates the path hierarchy of modules / packages

# imports pack1
# imports pack1.pack1_1
# imports pack1.pack1_1.module1

# sys modules contains cache for all entries
# the namespace where the import was run contains pack1

# FILE BASED PACKAGES
# package path are created using file system directories and files
# a package is a module that can contain other modules / packages
# on a file system a directory to use a package
# where does the code go for the package if its a directory?
# it goes into __init__.py

# the __init__.py file is what tells Python that directory is a package as opposed to standard directory
# if we dont have __init__.py it creates implicit namespace package

# app/
#   pack1/
#       __init__.py
#       module1.py
#       module2.py

# import pack1
# the code for pack1 is in __init__.py
# the code is loaded, executed, and cached in sys.modules with a key of pack1
