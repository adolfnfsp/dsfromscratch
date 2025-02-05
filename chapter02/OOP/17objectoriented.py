'''
Object-Oriented Programming
'''
class CountingClicker:
    """A class can/should have a docstring, just like a function"""
    def __init__(self, count = 0):
        """this is a constructor"""
        self.count = count
    
    def __repr__(self):
        """produce string representation of class instance"""
        return f"CountingClicker(count={self.count})"
    
    # example of private method/API implementation
    def _privmethod(self, hallo = "greeting"):
        """example of private method implementation
        based on convention
        """
        pass

    # public API implementation of our class
    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times
    
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0


clicker1 = CountingClicker()            # initialized to 0
clicker2 = CountingClicker(100)         # starts with count=100
clicker3 = CountingClicker(count=100)   # more explicit way of doing the same

# test cases for our clicker using assert
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

"""subclass to objectoriented.py base class"""
# A subclass inherits all the behaviour of its parent class.
class NoResetClicker(CountingClicker):
    """class with non-reset-able clicker"""
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

