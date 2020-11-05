#Test file for times.py file 

#Import the file and functions from times.py
from times import compute_overlap_time, time_range
import pytest
from pytest import raises 

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

@pytest.mark.parametrize("time_range1, time_range2 ,expected", [

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

def test_negative_time():
    #Checks if an error is raised for exception 
    with raises(ValueError) as exception:
        range1 = time_range("2010-01-12 13:00:00", "2010-01-12 11:00:00")



    




    
    

