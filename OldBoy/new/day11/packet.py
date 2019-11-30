import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)

print(__file__)
print(os.path.abspath(__file__))

print(os.path.dirname(os.getcwd()))