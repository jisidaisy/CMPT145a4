import Statistics

def test_add():
    '''
    Purpose:
        Test the add() method of the Statistics class.
    Pre-conditions:
        (none)
    Post-conditions:
        (none)
    Return:
        :return: True if the test passes, False otherwise.
    '''
    s = Statistics.Statistics()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(5)
    if s.count() != 5:
        print("Error in add(): incorrect count")
        return False
    if s.mean() != 3:
        print("Error in add(): incorrect mean")
        return False
    return True

def test_mean():
    '''
    Purpose:
        Test the mean() method of the Statistics class.
    Pre-conditions:
        (none)
    Post-conditions:
        (none)
    Return:
        :return: True if the test passes, False otherwise.
    '''
    s = Statistics.Statistics()
    if s.mean() != 0:
        print("Error in mean(): incorrect mean")
        return False
    return True
