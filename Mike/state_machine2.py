class State(object):
   no_match = 0
   one_match = 1
   both_match = 2
   def __init__(self):
      self.current = State.no_match

class StateMachine(object):
   def __init__(self):
      self._states = {}

   def register(self, state_type, state_function):
      # Assumes no duplicate state_type's
      self._states[state_type] = state_function

   def evaluate(self, state, value):
      words = value.split(' ')
      for word in words:
         ret_value = self._states[state.current](state, word)
         if ret_value != None:
            return ret_value

      # We need to try one more time in case we're ending the both_match state
      if state.current == State.both_match:
         return self._states[state.current](state, word)
      return -1
