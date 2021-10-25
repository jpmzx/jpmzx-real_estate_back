from utils.http_server import run_server
import os
import sys


src_path = os.path.dirname(
    os.path.abspath(__file__))  # Current file directory path
sys.path.insert(0, src_path)  # Appending directory to PYTHONPATH

if __name__ == '__main__':
    run_server()
