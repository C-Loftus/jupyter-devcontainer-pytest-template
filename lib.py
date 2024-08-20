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