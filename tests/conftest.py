import os
import sys

# Getting src directory path
src_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'src'))

# Adding src path to PYTHONPATH
sys.path.insert(0, f"{src_path}/")

# Getting src directory path
tests_path = os.path.dirname(
    os.path.abspath(__file__))

# Adding src path to PYTHONPATH
sys.path.insert(0, tests_path)
