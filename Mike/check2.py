from state_machine2 import State, StateMachine

start_word = "hello"
end_word = "you"
distance = 0

def state_no_match(state, word):
   if word == start_word:
      state.current = State.one_match
      return None

def state_one_match(state, word):
   global distance
   global start_word
   if word == start_word:
      distance = 0
      return None
   elif word == end_word:
      distance += 1
      state.current = State.both_match
      return None
   else:
      distance += 1
      return None
      
def state_both_match(state, word):
   global distance 
   return distance

def main():
   sm = StateMachine()
   sm.register(State.no_match, state_no_match)
   sm.register(State.one_match, state_one_match)
   sm.register(State.both_match, state_both_match)

   some_string = "hello how are you"
   initial_state = State()
   print sm.evaluate(initial_state, some_string)

   some_string = "hello how are hello you"
   initial_state = State()
   print sm.evaluate(initial_state, some_string)

   some_string = "you are hello"
   initial_state = State()
   print sm.evaluate(initial_state, some_string)
   
   some_string = "hello how are hello"
   initial_state = State()
   print sm.evaluate(initial_state, some_string)

if __name__=="__main__":
   main()
