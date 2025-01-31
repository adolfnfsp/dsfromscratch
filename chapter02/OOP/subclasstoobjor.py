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