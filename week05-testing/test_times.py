#Test file for times.py file 

#Import the file and functions from times.py
from times import compute_overlap_time, time_range
import pytest
from pytest import raises 
import yaml


""" #Testing function 
def test_given_input():
    #Test variables using time range function 
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    #Result obtained from function
    result = compute_overlap_time(large, short)

    #Expected result obtained from the function
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

#Tests for not overlapping : should be empty lists if not overlapping 
def test_not_overlapping():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected

#Test for multiple intervals: ie MANUALLY CHECK that expected result is what we should get 
def test_multiple_intervals():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60)
    range2 = time_range("2010-01-12 10:50:00", "2010-01-12 11:01:00", 2, 120)
    expected = [('2010-01-12 10:50:00', '2010-01-12 10:54:30'), ('2010-01-12 10:56:30', '2010-01-12 11:00:00')]
    result = compute_overlap_time(range1, range2)
    assert result == expected

#Manually check that the tests should be 11:00, 11:00 
def test_end_start():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    expected = [('2010-01-12 11:00:00', '2010-01-12 11:00:00')]
    result = compute_overlap_time(range1, range2)
    assert expected == result 

def test_negative_time():
    #Checks if an error is raised for exception 
    with raises(ValueError) as exception:
        range1 = time_range("2010-01-12 13:00:00", "2010-01-12 11:00:00")
 """

""" 
@pytest.mark.parametrize("time_range1, time_range2 ,expected", [
#Can do a list of timerange1, timerange2, expected values to input in the test

    #Test 1: Test given input
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
    time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00", 2, 60),
    [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]), 

    #Test 2: Test not overlapping
    (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), 
    time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00"), 
    0), 

    #Test 3: Test multiple intervals
    (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60), 
    time_range("2010-01-12 10:50:00", "2010-01-12 11:01:00", 2, 120), 
    [('2010-01-12 10:50:00', '2010-01-12 10:54:30'), ('2010-01-12 10:56:30', '2010-01-12 11:00:00')]), 

    #Test 4: Test end start:
    (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"), 
    time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"), 
    [('2010-01-12 11:00:00', '2010-01-12 11:00:00')]), 

])

#Placing all the tests in a single function 
def test_eval_overlap(time_range1, time_range2, expected):
    result = compute_overlap_time(time_range1, time_range2)
    assert result == expected 
"""

#Opening the yaml file containing all the parameters to check
with open("fixture.yaml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    print(fixture)

#Parameterized tests using test name 


@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]

def test_time_range_overlap(test_name):
    
    #Test name will be a dictionary which has 3 parameters to put in 
    properties = list(test_name.values())[0]    #Obtain values under each test
    
    #Pass all the parameters under time_range_1 to function time range
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])

    #Obtain expected overlap for every test 
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    #Assert that overlap is same as expected 
    assert compute_overlap_time(first_range, second_range) == expected_overlap

def test_negative_time():
    #Checks if an error is raised for exception 
    with raises(ValueError) as exception:
        range1 = time_range("2010-01-12 13:00:00", "2010-01-12 11:00:00")

   




    
    

