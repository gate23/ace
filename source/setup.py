from distutils.core import setup
import py2exe

setup(name="ace",
      author="Ralphs, Minor, Dunlap, Young",
      license="MIT License",
      windows=['main.py'],
      options={"py2exe":  {"includes":["sip", "PyQt4.QtGui", "PyQt4.QtCore"]}}
      )
