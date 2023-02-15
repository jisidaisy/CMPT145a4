# importing statistics
import statistics as s


# our class Statistics
class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.,a list called mylist
        """
        self.__count = 0
        self.__avg = 0
        self.__mylist = []

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.__mylist.append(value)
        self.__count += 1
        k = self.__count
        diff = value - self.__avg
        self.__avg += diff / k

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """

        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """

        return self.__count

    # our method range to get difference between max and min elements until the elements are added
    def range(self):
        # try block
        try:
            # return range
            return max(self.__mylist) - min(self.__mylist)
        # except block
        except:
            # return None
            return None

            # our method mode to get most occured elements until the elements are added

    def mode(self):
        # try block
        try:
            return s.mode(self.__mylist)
        # except block
        except:
            # return None
            return None

            # our method min to get minimum element until the elements are added

    def min(self):
        # try block
        try:
            # returning min
            return min(self.__mylist)
        # except block
        except:
            # return None
            return None

            # our method max to get maximum element until the elements are added

    def max(self):
        # try block
        try:
            # returning max
            return max(self.__mylist)
        # except block
        except:
            # return None
            return None