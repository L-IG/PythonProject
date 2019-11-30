import os,sys

print(__file__)
print(os.path.abspath(__file__))

other_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,other_path)
print(sys.path)


from hello import hello
