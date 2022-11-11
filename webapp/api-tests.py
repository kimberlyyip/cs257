'''
  Sophia Wang, Kimberly Yip, Sydney Nguyen

  This file is to test out api endpoints. 
'''

import server
import unittest

class ServerTester(unittest.TestCase):
  def setUp(self):
    self.server.Server() 

  def tearDown(self):
    pass
  
'''
  Test to check sorting on the smaller file
'''
