#Test file for times.py file 

#Import the file and functions from times.py
from times import compute_overlap_time, time_range

#Testing function 
def test_given_input():

    #Test variables
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    #Result obtained from function
    result = compute_overlap_time(large, short)

    #Expected result obtained from the function
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected