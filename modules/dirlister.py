#!/bin/python

#Purpose: This snippet  of code exposes a run function that lists all of the files in the current
#directory and returns that list as a string.
#Each module developed should expose a run function that takes a var number of args
#This enables you to load each module the same way and leaves enough extensibility
#so that you can customize the configuration files to the module if you desire 
import os

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")

    return str(files)
