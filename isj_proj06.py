#!/usr/bin/env python3

import collections
import itertools

def first_nonrepeating(input_string):
    """ function that finds first nonreapeating character in string """
    if not type(input_string) == str:
        return None
    
    elif not input_string.isprintable() or not input_string or input_string.isspace():
        return None 

    freq_dict = collections.Counter(input_string)
    for char in input_string:
        if freq_dict[char] == 1:
           return char
    return None

def combine4(numbers,target):
    """ function that finds all combinations of arithmetic expressions that are the same as target """

    if len(numbers) != 4:
        raise ValueError('Wrong number of arguments')
    for number in numbers:
        if type(number) != int:
            raise TypeError('Wrong type of argument')
        if number < 0:
            raise ValueError('The number argument is negative')
    if type(target) != int:
        raise TypeError('Wrong type of argument')

    operators = ['+', '-', '*', '/']

    permutation_of_operators = list(itertools.product(operators,repeat=3))
    permutations_of_numbers = list(itertools.permutations(numbers,4))
    expressions = []
    for numperm in permutations_of_numbers:
        for op_perm in permutation_of_operators:
            y = []
            for i in range(len(numperm)):
                if i == 3:
                     y.append(op_perm[0])
                     y.append(op_perm[1])
                     y.append(numperm[i])
                     y.append(op_perm[2])
                else:
                     y.append(numperm[i])
            expressions.append(y)

    for numperm in permutations_of_numbers:
        for op_perm in permutation_of_operators:
            expressions.append(numperm+op_perm)

    result = []
    for exp in expressions:
        if eval_postfix(exp) == target:
            result.append(to_infix(exp))

    return sorted(list(set(result)))



def to_infix(postfix):
    """ Utility function to translate from postfix notation """
    operators = ['+', '-', '*', '/']
    stack = []
    for char in postfix:
        # if it is operand
        if char not in operators:

            stack.append(char)

        # it is operator
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.append("("+ str(op2) + char + str(op1) + ")")

    return stack.pop()

def eval_postfix(postfix):
    """ Utility function that evalutes expressions in postfix notation """
    s = []
    operators = ['+', '-', '*', '/']
    for char in postfix:
        plus = None
        if char not in operators:
            s.append(int(char))

        elif s:
            op1 = s.pop()
            op2 = s.pop()
            if char == "+":
                plus = op2 + op1
            elif char == "-":
                plus = op2  - op1
            elif char == "*":
                plus = op2 * op1
            elif char == "/":
                if op1== 0:
                    return None                
                plus = op2 / op1    
        if plus is not None:
            s.append(plus)
    return s.pop()
