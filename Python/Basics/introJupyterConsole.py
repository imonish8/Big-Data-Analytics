print("Hello Jupyter Console !!")
2+2
for i in range(1,5):
    print("Jupyter Console is easy peasy !!!")
%lsmagic
%pwd
%timeit sum(range(1,5))
%%timeit
total = 0
for i in range(100):
    total += i
%%writefile /Users/imonish8/Desktop/Big-Data-Analytics/Python/Notebooks/NumpyConsole.py
print("Hello Pandas and Numpy In Jupyter Console !!! ")
print("Hello")
from IPython.display import Image
Image(url='https://www.python.org/static/community_logos/python-logo.png')
%history -f introJupyterConsole.py
