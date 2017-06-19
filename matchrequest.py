class MatchRequest(object):
   def __init__(self):
       self.idx = 0
       self.matches = {}
   def __iter__(self):
       return self
   def __next__(self):
       self.idx += 1
       try:
           return self.matches[self.idx-1]
       except IndexError:
           self.idx = 0
           raise StopIteration
   next = __next__