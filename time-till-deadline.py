"""
Exercise:
a) Accept user input of goal and a deadline
b) Print back:
  How much time remains until that deadline?
  Hint: make use of datetime module for time calculation
  ex: learn python:10.02.2021
"""

from datetime import datetime


user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")


goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculate how many days from now till deadline
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")


"""
Built-In vs Third-Party Modules
- Python comes only with a set of built-in modules
- Many more modules out there, which are NOT part of Python installation
ex: Pandas, NumPy, PyTorch, plotly, matplotlib, theano, Tensorflow, Keras, scikit learn, more...
- You need to install these third-party modules
- Built-in Modules and packages are most common ones
- Depending on what application you write, add specific ones (such as web app or ML app)
- Lets say we need to download modules for Web Development such as Django
- Where can we find those modules and download them? Answer: PyPI
"""

"""
   Module vs Package
Module -> Any Python file is a module
Package -> Collection of python modules
  * Package must include an __init__.py file
  * This __init__ file distinguishes a package from a directory
"""

"""
How to download a package from PyPI?

pip: is a package manager for python
used to install manager for Python Package Index, but also other indexes
ex: pip install Django / pip uninstall Django
"""

