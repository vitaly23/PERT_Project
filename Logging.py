'''
     Author:  Vitaly Gorelik
     ID:      316883529
'''

import logging

'''
    Represent logger for the application.
    Use it as mixing class with the other classes in the project.
'''
class MyLogger():
    @property
    def logger(self):
        name = '.'.join([__name__, self.__class__.__name__])
        return logging.getLogger(name)
