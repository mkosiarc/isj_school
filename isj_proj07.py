#!/usr/bin/env python3

class TooManyCallsError(Exception):
    """ custom exception for limit_calls decorator """
    pass

def limit_calls(max_calls=2,error_message_tail="called too often"):
    """ Decorator limiting calls to function"""
    
    def wrap(f):
        calls = 0;
        def wrapped(*args):
           nonlocal calls
           calls = calls + 1

           if calls > max_calls:
                raise TooManyCallsError('function "' + f.__name__ +'" - ' + error_message_tail)
           return f(*args)
        return wrapped
    return wrap


class Log():
    """ class for file logging """

    def __init__(self,filename):
        """ __init__ """
        self.file = open(filename,"w")

    def logging(self,line):
        """ insert a line to file """
        self.file.write(line + "\n")
    
    def __enter__(self):
        """ __enter__ """
        self.file.write("Begin\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ __exit__  """
        self.file.write("End\n")
        self.file.close()

def ordered_merge(*args, **kwargs):
    """ ordered_merge function """
    selector = kwargs.get('selector',[])

    #make iterables 
    args = [ iter(item) for item in list(args) ]

    #generate result
    result = [ next(args[item]) for item in selector ]

    return result
