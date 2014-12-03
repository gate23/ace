"""
setup.py

This is the setup file for py2exe to build out a Windows executable.
"""

from distutils.core import setup
import py2exe

setup(name="Algae Count Estimator",
      author="Ralphs, Minor, Dunlap, Young",
      license="MIT License",
      windows=[{
                "script":"ace.py",
                "icon_resources": [(1, "ace.ico")]
              }],
      options={"py2exe":  {"includes":["sip", "PyQt4.QtGui", "PyQt4.QtCore"]}}
      )
