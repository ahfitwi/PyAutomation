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
