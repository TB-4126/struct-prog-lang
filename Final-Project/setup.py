from setuptools import setup, Extension

#rebuild the module using these commands in Ubuntu terminal to reinstall cevaluator module
# go to Users/tbond/Documents/CS_Projects/Garter/tbond-interpreter-trivial
#python3 -m venv .venv
#pip3 install .

setup(
   name = "cevaluator",
   version = "0.0.4",
   ext_modules = [
      Extension("cevaluator", ["src/cevaluator.c"])
   ]
)