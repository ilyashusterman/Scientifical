# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:18:21 2019

@author: amita
"""
#from datetime import datetime
import time
import os


def check_proccess(proccess):
    return True


def warn_if_script_runtime_is_long(script_filename):
    start_time = time.time()
    print("AAA start_time: ", start_time)
    os.system("py -3 {}".format(script_filename))
    time_to_run = time.time() - start_time        
    print("AAA time to run:", time_to_run )
    print("AAA time_to_run.seconds: ", time)
    if time_to_run > 10:
        return 'Warning'
    else:
        return 'OK'

    
def check_script(script_filename):
    with open(script_filename, 'r') as file: 
        script = file.read() 
    if "import tensorflow" in script:
        return 'GPU'
    else:
        return 'CPU'
