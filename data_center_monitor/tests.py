# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:05:53 2019

@author: Amitay
"""

import unittest
from proccessmanager import check_proccess, check_script, warn_if_script_runtime_is_long
import sys


class TestProccessManager(unittest.TestCase):
 
    def setUp(self):
        print("sys.version", sys.version)
        self.proccess = 'proccess'
        self.gpu_stressor_script_filename = 'stressors/stressor_gpu_script.py'
        self.cpu_stressor_script_filename = 'stressors/stressor_cpu_script.py'
        self.long_runtime_stressor_filename = 'stressors/stressor_cpu_long_runtime.py'
 
    def test_proccessor_classifier_should_return_gpu_when_script_contains_import_tensorflow(self):
        self.assertEqual(check_script(self.cpu_stressor_script_filename),'CPU')
        self.assertEqual(check_script(self.gpu_stressor_script_filename),'GPU')
    
 
    def test_long_cpu_proccess_should_return_warning (self):
        self.assertEqual(warn_if_script_runtime_is_long(self.long_runtime_stressor_filename), 'Warning')
        pass
    
    
if __name__ == '__main__':
    unittest.main()
    #to connect from the server to the smart NIC: 192.168.100.1/2