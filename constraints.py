
class constraints_manager:

    def check(x, y):
        return (constraints_manager.contained(x, y), constraints_manager.sequence(x, y))

    def contained(x, y, interval1 = (0, float('inf')), interval2 = (0, float('inf'))):
        return (
                (y['b'] - x['b'] >= interval1[0] and y['b'] - x['b'] <= interval1[1] and 
                x['e'] - y['e'] >= interval2[0] and x['e'] - y['e'] <= interval2[1])
                or 
                (y['e'] - x['e'] >= interval1[0] and y['e'] - x['e'] <= interval1[1] and
                x['b'] - y['b'] >= interval2[0] and x['b'] - y['b'] <= interval2[1])
            )
    
    def contained_debug(x, y, interval1 = (0, float('inf')), interval2 = (0, float('inf'))):
        print(f'x: {x}, y: {y}, interval1: {interval1}, interval2: {interval2}. Result: {constraints_manager.contained(x, y, interval1, interval2)}')
        return constraints_manager.contained(x, y, interval1, interval2)
        
    def sequence( x, y, interval1 = (0, float('inf')), interval2 = (1, float('inf'))):
        return (y['e'] - x['b'] >= interval1[0] and y['e'] - x['b'] <= interval1[1] and
                x['e'] - y['b'] >= interval2[0] and y['e'] - x['b'] <= interval2[1])
        
    def sequence_debug( x, y, interval1 = (0, float('inf')), interval2 = (1, float('inf'))):
        print(f'x: {x}, y: {y}, interval1: {interval1}, interval2: {interval2}. Result: {constraints_manager.sequence(x, y, interval1, interval2)}')
        return constraints_manager.sequence(x, y, interval1, interval2)


