import os

print("this is before change directory : ", os.getcwd())
os.chdir(os.path.dirname(__file__))
print(os.path.realpath("."))



print(__file__)