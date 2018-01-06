#!/usr/bin/env python
# -*- coding: utf-8 -*-

PKG = 'openni_description'

import os
import subprocess
import unittest

import rospkg


class TestOpenniDescription(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        True

    def test_urdf_turtlebot(self):
        """
        Check if check_urdf command passes with the urdf that is generated in
        the .test file this test case is called from.
        """
        self.assertTrue(os.path.isfile(rospkg.RosPack().get_path('openni_description') + "/test/sample_kobuki.urdf.xacro")
        print(subprocess.check_output(["rosrun", "xacro", "xacro", rospkg.RosPack().get_path('openni_description') + "/test/sample_kobuki.urdf.xacro", "-o", "./sample_kobuki.urdf"]))
        self.assertEqual(0, subprocess.call(["check_urdf", "./sample_kobuki.urdf"]))

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_openni_description', TestOpenniDescription) 
