
class constraints_manager:

    def __init__(self):        
        self.constraints = {}


    def contained(self, x, y, interval1 = (0, float('inf')), interval2 = (0, float('inf'))):
        return (
                (y[0] - x[0] >= interval1[0] and y[0] - x[0] <= interval1[1] and 
                x[1] - y[1] >= interval2[0] and x[1] - y[1] <= interval2[1])
                or 
                (y[1] - x[1] >= interval1[0] and y[1] - x[1] <= interval1[1] and
                x[0] - y[0] >= interval2[0] and x[0] - y[0] <= interval2[1])
            )
    
    def contained_debug(self, x, y, interval1 = (0, float('inf')), interval2 = (0, float('inf'))):
        print(f'x: {x}, y: {y}, interval1: {interval1}, interval2: {interval2}. Result: {self.contained(x, y, interval1, interval2)}')
        return self.contained(x, y, interval1, interval2)
        
    def sequence(self, x, y, interval1 = (0, float('inf')), interval2 = (1, float('inf'))):
        return (y[1] - x[0] >= interval1[0] and y[1] - x[0] <= interval1[1] and
                x[1] - y[0] >= interval2[0] and y[1] - x[0] <= interval2[1])
    
    
    def sequence_debug(self, x, y, interval1 = (0, float('inf')), interval2 = (1, float('inf'))):
        print(f'x: {x}, y: {y}, interval1: {interval1}, interval2: {interval2}. Result: {self.sequence(x, y, interval1, interval2)}')
        return self.sequence(x, y, interval1, interval2)


