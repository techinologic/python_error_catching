import urllib.request
#
#
# try:
#     webpage = urllib.request.urlopen('http://google.com')
# except:
#     print('Could not access webpage!')
# else:
#     for line in webpage:
#         print(line)
#

# # Circuit breaker real world example
# class CircuitBreaker:
#
#     def __init__(self, max_amps):
#         self.capacity = max_amps
#         self.load = 0
#
#     # checks if load is below capacity
#     def connect(self, amps):
#         if self.load + amps > self.capacity:
#             raise Exception('Load will exceed capacity')
#         elif self.load + amps < 0:
#             raise Exception('Negative load not permitted')
#         else:
#             self.load += amps
#
# # create a 20A circuit breaker
#
# cb = CircuitBreaker(20)
#
# print(cb.load)
# cb.connect(21)

# handling household problems

class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)

class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)

def cause_error(error_type):
    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overlaoded')
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher', 'spraying water')
    else:
        raise Exception('Generic household problem')

try:
    cause_error('yard')
except ElectricalError as e:
    print(e)
    print('Fix it myself.')
except PlumbingError as e:
    print(e)
    print('Call plumber now!')
except:
    print('Call landlord')

