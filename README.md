# DS5111_FALL2023_SW2_Lab
DS 5111 Lab #2

1. What did you have to do to get make to work?

Since the "make" command wasn't previously installed, the following line had to be run first before "make" could be utilized: sudo apt install make

2. Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)

Similar to the "make" command, the python3 -m venv env command could not be run without running the necessary underlying code as shown here: sudo apt install python3.10-venv. Luckily, the resulting error message had the solution clearly outlined with several options to choose from. Without the guidance, it would've taken a bit longer to run a Google search to debug the issue.

3. Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;

The newline separator initiates the execution of a preceding command. Thus, two bash commands separated by a newline character would result in individual executions of the two bash commands. Note that background jobs are not run sequentially - they are run concurrently.  Unlike the newline character, the semicolon separator doesn't trigger the execution of commands. Rather, it enables the sequential execution of commands within the same command line. 

4. As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?
The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?

In the case where a file named "run" is present within my directory, a similar solution for the "tests" job can be invoked to fix a possible collision. By adding an additional row in the makefile immediately prior to the "run" job with the text ".PHONY: run". A phony target is one that isn't the name of a file, but rather a name for a job to be executed when an explicit execution request is made.

The purpose of the two additional lines is ???

