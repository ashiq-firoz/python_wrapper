# python_wrapper
Wrapping tool for python 

# Benefits

* When we code in python and have this feeling to place a set of code inside a function or a loop or a class,
  We will just copy paste and spent time in getting all indentations right.
  
  * python_wrapper module does this for you with a single line of code
  

# How to setup

* Copy the file and paste it in libs folder in the python directory inside c:/programs/users/name/AppData/programs

# How to Use

* import python_wrapper as pw
<br>
 pw.wrapper(os.path.realpath(__file__),'class',5)
  
  *os.path.realpath(__file__) -> to get the path of your current py file
  *class or if or else or anything that need to be wrapped
  * 5 -> line number from which wrapping starts
  
