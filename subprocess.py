# Subprocess Module
"""
A running program is called a process. Each process has its own system state, which includes memory, lists of open files, a program counter that keeps 
track of the instruction being executed, and a call stack used to hold the local variables of functions.

Normally, a process executes statements one after the other in a single sequence of control flow, which is sometimes called the main thread of the 
process. At any given time, the program is only doing one thing.

A program can create new processes using library functions such as those found in the os or subprocess modules such as os.fork(), subprocess.Popen(), 
etc. However, these processes, known as subprocesses, run as completely independent entities-each with their own private system state and main thread 
of execution.

Because a subprocess is independent, it executes concurrently with the original process. That is, the process that created the subprocess can go on 
to work on other things while the subprocess carries out its own work behind the scenes.

The subprocess module allows us to:
  1. spawn new processes
  2. connect to their input/output/error pipes
  3. obtain their return codes
  
It offers a higher-level interface than some of the other available modules, and is intended to replace the following functions:
  1. os.system()
  2. os.spawn*()
  3. os.popen*()
  4. popen2.*()
  5. commands.*()
  
We cannot use UNIX commands in our Python script as if they were Python code. For example, echo name is causing a syntax error because echo is not a 
built-in statement or function in Python. So, in Python script, we're using print name instead.

To run UNIX commands we need to create a subprocess that runs the command. The recommended approach to invoking subprocesses is to use the 
convenience functions for all use cases they can handle. Or we can use the underlying Popen interface can be used directly. 

"""
"""
os.system()
The simplest way of running UNIX command is to use os.system().
"""
import os
os.system('echo $HOME')
# /home/alem
# or we can use
os.system('echo %s' %'$HOME')
#/home/alem

"""
os.system('command with args') passes the command and arguments to our system's shell. By using this can actually run multiple commands at once 
and set up pipes and input/output redirections. :os.system('command with args') passes the command and arguments to our system's shell. 
By using this can actually run multiple commands at once and set up pipes and input/output redirections. :
"""
os.system('command_1 < input_file | command_2 > output_file')
os.system('echo $HOME > outfile')
f = open('outfile','r')
f.read()

"""
os.popen()
Open a pipe to or from command. The return value is an open file object connected to the pipe, which can be read or written depending on whether 
mode is 'r' (default) or 'w'. The bufsize argument has the same meaning as the corresponding argument to the built-in open() function. The exit 
status of the command (encoded in the format specified for wait()) is available as the return value of the close() method of the file object, 
except that when the exit status is zero (termination without errors), None is returned.os.popen(). Open a pipe to or from command. The return 
value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'. The bufsize
argument has the same meaning as the corresponding argument to the built-in open() function. The exit status of the command (encoded in the 
format specified for wait()) is available as the return value of the close() method of the file object, except that when the exit status is 
zero (termination without errors), None is returned.
"""

import os
stream = os.popen('echo $HOME')
stream.read()

"""
os.popen() does the same thing as os.system except that it gives us a file-like stream object that we can use to access standard input/output 
for that process. There are 3 other variants of popen that all handle the i/o slightly differently.os.popen() does the same thing as os.system
except that it gives us a file-like stream object that we can use to access standard input/output for that process. There are 3 other variants
of popen that all handle the i/o slightly differently.

If we pass everything as a string, then our command is passed to the shell; if we pass them as a list then we don't need to worry about 
escaping anything. However, it's been deprecated since version 2.6: This function is obsolete. Use the subprocess module. docs.python.org

subprocess.call()
This is basically just like the Popen class and takes all of the same arguments, but it simply wait until the command completes and gives 
us the return code.

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

Run the command described by args. Wait for command to complete, then return the returncode attribute.
"""
import os
os.chdir('/')
import subprocess
subprocess.call(['ls','-l'])

"""
https://www.bogotobogo.com/python/python_subprocess_module.php
"""

