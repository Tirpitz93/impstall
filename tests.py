import subprocess
import sys
import unittest

import impstall


class TestInstall(unittest.TestCase):

    def test_pypi_install(self):
        impstall.now("bson")
        import bson

        impstall.now("unum")
        import unum

    def test_git_install(self):
        impstall.now("git+https://github.com/Tirpitz93/Unum")
        import unum

    def tearDown(self):

        args = [sys.executable, '-m', 'pip'] + ['uninstall', '-y', 'bson', 'unum']
        _handle = subprocess.Popen(args)
        _handle.wait()
