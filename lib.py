# Define any classes and functions here that can be isolated
# outside of the notebook to allow for easier testing

class Adder:
    def add(self, x, y) -> int:
        return x + y
    
class Multiplier:

    def mult(self, x, y):
        
        result = 0
        adder = Adder()

        for _ in range(y):
            result = adder.add(result, x)

        return result