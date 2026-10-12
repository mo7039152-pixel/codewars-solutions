def get_sum(a,b):
    s = min(a,b)
    m = max(a,b)
    total = 0
    while(s <= m):
        total += s
        s += 1
    return total    
# def get_sum(a, b):
#     low = min(a, b)
#     high = max(a, b)
#     n = (high - low) + 1
#     return n * (low + high) // 2   
# (O(1))
###########
# def get_sum(a, b):
#   return sum(range(min(a, b), max(a, b) + 1)) #+1 casuse python does not take the last num  in range#
from solution import get_sum
import codewars_test as test


@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)