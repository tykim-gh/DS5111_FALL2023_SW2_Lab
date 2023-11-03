# DS5111_FALL2023_SW2_Lab
DS 5111 Lab #2

1. What did you have to do to get make to work?

Since the "make" command wasn't previously installed, the following line had to be run first before "make" could be utilized: sudo apt install make. In addition, I had to add a line to activate the virtual environment for each of the functions written in the makefile since the pylint and pytest packages were installed in said virtual environment.

2. Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)

Similar to the "make" command, the python3 -m venv env command could not be run without running the necessary underlying code as shown here: sudo apt install python3.10-venv. Luckily, the resulting error message had the solution clearly outlined with several options to choose from. Without the guidance, it would've taken a bit longer to run a Google search to debug the issue.

3. Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;

The newline separator initiates the execution of a preceding command. Thus, two bash commands separated by a newline character would result in individual executions of the two bash commands. Note that background jobs are not run sequentially - they are run concurrently.  Unlike the newline character, the semicolon separator doesn't trigger the execution of commands. Rather, it enables the sequential execution of commands within the same command line. 

4. As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?
The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?

In the case where a file named "run" is present within my directory, a similar solution for the "tests" job can be invoked to fix a possible collision. By adding an additional row in the makefile immediately prior to the "run" job with the text ".PHONY: run". A phony target is one that isn't the name of a file, but rather a name for a job to be executed when an explicit execution request is made.

The path or directory that Python searches through to find the modules and files is stored in the path attribute of the sys module. Due to the fact that the path is a list, we can use the append method to add new directories to the path. In this case, it is enabling the pytest to search for the correct test_clockdeco_param.py file located underneath the tests folder.










Extra Credit

1. tree -L 2 -I '__pycache__|env'

2. The "* *" is a wildcard used for recursive directory traversal. It will match files and directories in the current directory as well as all of its subdirectories. The subsequent characters is also a wildcard that matches all files and directories within a specified directory.

3. I have included them in the requirements.txt file.

4. When a Python script is executed directly, the '__name__' variable is allocated to '"__main__"', which causes the script to execute the main program. However, when the script is imported as a module into another script, the '__name__' variable is assigned to name of the module or, in this case, the name of the script file without the ".py" file extension.

5. Continuing from my answer to Question 4, if two print statements were added above and below the if __name__... line, an import of the file would cause only the print statement above the line to execute. The other print statement underneath the line will only execute when the script is executed directly as the main program, instead of being imported as a module.

