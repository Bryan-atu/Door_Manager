import sys
import os

# Add the parent directory (Door_Manager) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Car:
    def __init__(self, num_doors=4):
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

    def set_num_doors(self, num_doors):
        if num_doors > 0:
            self.num_doors = num_doors
        else:
            raise ValueError("number of doors must be a positive integer")