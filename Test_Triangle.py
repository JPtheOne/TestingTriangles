import pytest       #Library to control tests
import itertools    #Library to iterate
import random       #Randomizer is used in some tests to explore a wider range of values
from Triangle import Triangle

class Test_Triangle: #To use pytest, the name of the class should always start with "Test*"

    @staticmethod
    def generate_permutations(*args): #Function to generate permutations of parameters
        return list(itertools.product(*args))

    def test_EquilateralCases(self): #For all the possible cases when the triangle has the 3 same sides
        ran_side= random.randint(1,999)
        triangle = Triangle(ran_side, ran_side, ran_side)
        assert triangle.check_triangle_type() == "Equilateral triangle"     

    def test_IsoscelesCases(self): #For all the permutations of having two same sides and one different side
        ran_side  = random.randint(1,999)
        ran_side2 = random.randint(1,999)

        triangle  = Triangle(ran_side, ran_side, ran_side2)
        assert triangle.check_triangle_type() == "Isosceles triangle"     
        
        triangle  = Triangle(ran_side, ran_side2, ran_side)
        assert triangle.check_triangle_type() == "Isosceles triangle"  
        
        triangle  = Triangle(ran_side2, ran_side, ran_side)
        assert triangle.check_triangle_type() == "Isosceles triangle"  

    def test_ScaleneCases(self): #When every side has a different length, regardless of the order but respecting the rule of the sum of sides
        ran_side  = random.randint(1,999)
        ran_side2 = random.randint(1,999)
        ran_side3 = random.randint(1,999)

        triangle  = Triangle(ran_side, ran_side2, ran_side3)
        assert triangle.check_triangle_type() == "Scalene triangle" 
        triangle  = Triangle(ran_side, ran_side3, ran_side2)
        assert triangle.check_triangle_type() == "Scalene triangle"
        triangle  = Triangle(ran_side2, ran_side, ran_side3)
        assert triangle.check_triangle_type() == "Scalene triangle" 
        
    def test_Negative(self): #whenever a side length is negative
        a_values = [-1, -2,-3]
        b_values = [-1, -2,-3]
        c_values = [-1, -2,-3]

        permutations = self.generate_permutations(a_values, b_values, c_values)

        for p in permutations:
            triangle = Triangle(*p)
            assert triangle.check_triangle_type() == "Not a triangle"

    def test_Zero(self): #Whenever any side is 0
        a_values = [0]
        b_values = [0,1]
        c_values = [0,1]

        permutations = self.generate_permutations(a_values, b_values, c_values)

        for p in permutations:
            triangle = Triangle(*p)
            assert triangle.check_triangle_type() == "Not a triangle"        
 
    def test_NoTriangle(self): #If the sum of two sides is bigger than the third side
        triangle = Triangle(2,3,9)
        assert triangle.check_triangle_type() == "Not a triangle"
        triangle = Triangle(1,4,8)
        assert triangle.check_triangle_type() == "Not a triangle"
        triangle = Triangle(6,5,12)
        assert triangle.check_triangle_type() == "Not a triangle"
     
    def test_OtherthanNumber(self): #Whenever any other data rather than integers is given as parameter
        with pytest.raises(ValueError):
            triangle = Triangle("sadasd",2,3)
        with pytest.raises(ValueError):
            triangle = Triangle(1,2.5,3)
        with pytest.raises(ValueError):
            triangle = Triangle(1,3,"!")
        with pytest.raises(ValueError):
            triangle = Triangle("a",4.7, "!#34423")
  
    def test_NoParameter(self): #Whenever parameters are null or empty
        with pytest.raises(TypeError):
            Triangle()

    def test_BigValues(self): #Raises exception when the sizes exceed 1000
        with pytest.raises(ValueError):
            Triangle(29, 49, 2999)
        with pytest.raises(ValueError):
            Triangle(3229, 49, 29)
        with pytest.raises(ValueError):
            Triangle(29, 2149, 99)
        with pytest.raises(ValueError):
            Triangle(2912, 2149, 9912)