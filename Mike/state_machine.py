class State(object):
   no_match = 0
   one_match = 1
   both_match = 2
   def __init__(self):
      self.current = State.no_match

class StateMachine(object):
   def __init__(self):
      self._states = []

   def register(self, state_function):
      self._states.append(state_function)

   def evaluate(self, state, value):
      words = value.split(' ')
      for word in words:
         for state_func in self._states:
            print "word: {0}".format(word)
            print "state: {0}".format(state.current)
            ret_value = state_func(state, word)
            if ret_value != None:
               return ret_value
