class Triangle: 
    
    def __init__(self,a,b,c):
        #Declaration of exceptions
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int): #ValueError to accept only ints
            raise ValueError("All parameters must be integers.")
        
        if a > 1000 or b > 1000 or c > 1000: #To control sizes being smaller than 1000
            raise ValueError("Numbers of that size are not accepted.")
       
        self.a = a
        self.b = b
        self.c = c
    
    def check_triangle_type(self): #Method to determine triangle type
        a = self.a
        b = self.b
        c = self.c

        if a + b <= c or a + c <= b or b + c <= a: #Whenever the basic rule is broken 
            return "Not a triangle"
        elif a == b == c:                          #Having same sizes
            return "Equilateral triangle"
        elif a == b or b == c or c == a:           #Having two same sizes and one different
            return "Isosceles triangle"
        else:                                      #Having every size with different length
            return "Scalene triangle"

 