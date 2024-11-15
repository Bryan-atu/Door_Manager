import pytest
import sys
import os

# Add the parent directory of the test file to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Debugging: Print the Python path
print("PYTHON PATH:", sys.path)

from car import Car

def test_default_num_doors():
    # Test default number of doors
    car = Car()
    assert car.get_num_doors() == 4

def test_custom_num_doors():
    # Test custom number of doors
    car = Car(num_doors=2)
    assert car.get_num_doors() == 2

def test_set_num_doors_valid():
    # Test setting a valid number of doors
    car = Car()
    car.set_num_doors(3)
    assert car.get_num_doors() == 3

def test_set_num_doors_invalid():
    # Test setting an invalid number of doors
    car = Car()
    with pytest.raises(ValueError, match="number of doors must be a positive integer"):
        car.set_num_doors(-1)
