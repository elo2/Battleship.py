from state_machine import State, StateMachine

start_word = "hello"
end_word = "you"
distance = 0

def state_no_match(state, word):
   if state.current == State.no_match:
      if word == None:
         print "No more words"
         return -1
      elif word == start_word:
         print "Found start word"
         state.current = State.one_match
      else:
         print "Didn't find start word or none"

def state_one_match(state, word):
   global distance
   if state.current == State.one_match:
      if word == None:
         print "No more words"
         state.current = State.no_match
      elif word == end_word:
         print "Found end word"
         state.current = State.both_match
      else:
         distance += 1
      
def state_both_match(state, word):
   global distance 
   if state.current == State.both_match:
      print "Found final word!"
      return distance

def main():
   sm = StateMachine()
   sm.register(state_no_match)
   sm.register(state_one_match)
   sm.register(state_both_match)

   some_string = "hello and welcome to you"
   initial_state = State()
   print sm.evaluate(initial_state, some_string)
   current_state = State()
   some_string_2 = "you and welcome to hello"
   print sm.evaluate(current_state, some_string_2)

if __name__=="__main__":
   main()
