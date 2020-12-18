<h1>Password-gen</h1>

A tkinter based GUI Password generator.

<h3>Requirements</h3>
*Python:3.7.3<br>
*Tkinter library with tk/tcl version 8.6<br>
*secrets module<br>
*string module<br>
*Pyperclip: 1.8.0

### How to run ? 
Download the executable (Windows) from the release [here](https://github.com/vaylon-fernandes/password-gen/releases/tag/v1.0.0) <br> 
**OR** <br>
First clone the repo using one of the following ways:
1. HTTPS - ```git clone https://github.com/vaylon-fernandes/password-gen.git```
2. SSH - ```git clone git@github.com:vaylon-fernandes/password-gen.git```
3. The github CLI interface - ```gh repo clone vaylon-fernandes/password-gen``` <br>
Move into the repo directory (password-gen) or type ```cd password-gen``` in command prompt (terminal) from the current directory. 
<br> Create a virtual enviroment by typing  ```virtualenv venv``` in a terminal. After the environment has been created, activate by using the command ```venv\scripts\activate\``` on Windows or ```. venv\bin\activate``` on Ubuntu.<br>
Install the requirements using ```pip install -r 'requirements.txt'```. This will install the pyperclip library. The tkinter library is bundled with python.<br>
(**Note**: Some linux distributions don't come without the tkinter library bundled with python, you can install it using ```pip install tkinter```)<br>
Now run the Password-Generator using ```python password-generator.py```
