#!/usr/bin/env python3

class Polynomial:
    """ Class representing polynomial """
    def __init__(self,*arg,**kwargs):
        """ Initialize polynomial object"""
        self.polynomial = []
        if(len(kwargs) != 0):
           self.polynomial = []
           order = sorted(kwargs.keys())[-1]
           order = int(order[1])
           for i in range(0,int(order)+1):
                self.polynomial.append(0)
           for key,value in kwargs.items():
               index = int(key[1])
               self.polynomial[index] = value 
                
        elif(len(arg) != 0):
            if isinstance(arg[0],list):
                self.polynomial = arg[0]
            else:
                self.polynomial = list(arg)
        if self.polynomial[-1] == 0 and len(self.polynomial) != 1:  
           self.polynomial.pop()
    
    def __repr__(self):
        """ representation of objects is the same as the string format of object """
        return self.__str__()

    def __str__(self):
        """ Convert object with polynom represented as list to string """
        join_with = {
            (True, True): '-',
            (True, False): '',
            (False, True): ' - ',
            (False, False): ' + '
        }

        result = []
        for power, coeff in reversed(list(enumerate(self.polynomial))):
            if coeff == 0:
               continue
            join = join_with[not result, coeff < 0]
            coeff = abs(coeff)
            if coeff == 1 and power != 0:
                coeff = ''

            f = {0: '{}{}', 1: '{}{}x'}.get(power, '{}{}x^{}')

            result.append(f.format(join, coeff, power))

        return ''.join(result) or '0'
 
    def __eq__(self, other): 
        """ compare two polynomial objects in string format """
        return self.__str__() == other.__str__()
        

    def __add__(self,other):
        """ add two polynomials """
        len_self = len(self.polynomial)
        len_other = len(other.polynomial)
        if len_self >= len_other:
            sum = list(self.polynomial)
            for power,coeff in list(enumerate(other.polynomial)):
                sum[power] = sum[power] + other.polynomial[power]
        else:
            sum = list(other.polynomial)
            for power,coeff in list(enumerate(self.polynomial)):
                sum[power] = sum[power] + self.polynomial[power]

        return Polynomial(sum)

    def derivative(self):
        """ takes derivative of a polynomial """
        if len(self.polynomial) == 1:
            return Polynomial(0)
        der = [ self.polynomial[i] * i for i in range(1,len(self.polynomial))]

        return Polynomial(der)

    def at_value(self,value,second_value=''):
        """ Evalutes polynomial at value using the horner method""" 
        if second_value != '':
           return self.at_value(second_value) - self.at_value(value)        
        p = self.polynomial[-1]
        for i in range(len(self.polynomial)-2,-1,-1):
            p = p * value + self.polynomial[i]

        return p

    def multiply(self,a):
        """ help method used by __pow__ for multiplying polynomial by itself"""
        c = [0]*(len(a) + len(self.polynomial)-1)

        for i in range(len(a)):
            ai = a[i]
            for j in range(len(self.polynomial)):
                c[i + j] += ai * self.polynomial[j]

        return c

    def __pow__(self, n):
        """ raise polynomial to n-th power """
        a = [1]
        for i in range(n):
            a = self.multiply(a)
        return Polynomial(a)
    

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1" 
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
