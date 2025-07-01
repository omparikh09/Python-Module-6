"""
Write a Python program that uses a custom iterator to iterate over a list of integers.
"""

class ListIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    
numbers = [10, 20, 30, 40, 50]

iterator = ListIterator(numbers)

for num in iterator:
    print(num)