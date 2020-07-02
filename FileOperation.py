f = open('A:\desktop shrt\Python\PythonRead.txt',"r")
print(f.readline())
f.close()
f = open('A:\desktop shrt\Python\PythonRead.txt',"a")
print(f.write("Added arun"))
f.close()


import os
if os.path.exists('A:\desktop shrt\Python\PythonRead1.txt'):
    #os.remove('A:\desktop shrt\Python\PythonRead1.txt')
    pass


