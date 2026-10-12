def even_or_odd(number):
    return ("Even" if number % 2 == 0 else "Odd")
import codewars_test as test
from solution import even_or_odd

@test.describe("Example tests")
def example_tests():
    
    @test.it('even_or_odd(1) should return "Odd"')
    def test_positive_odd():
        test.assert_equals(even_or_odd(1), "Odd")
        
    @test.it('even_or_odd(2) should return "Even"')
    def test_positive_even():
        test.assert_equals(even_or_odd(2), "Even")

    @test.it('even_or_odd(-1) should return "Odd"')
    def test_negative_odd():
        test.assert_equals(even_or_odd(-1), "Odd")
            
    @test.it('even_or_odd(-2) should return "Even"')
    def test_negative_even():
        test.assert_equals(even_or_odd(-2), "Even")