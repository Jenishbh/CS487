@acts_as_state_machine
class Process:
    # define 4 states
    checkout = State(initial=True)
    payment=State()
    pending=State()
    confirmd=State()
    canceled=State()
  
    # define transitions
    paymentInfo = Event(from_states=(checkout), to_state=payment)
    submit = Event(from_states=payment,to_state=pending)
    canceled = Event(from_states=confirmd,to_state=canceled)
    disapprove = Event(from_states=pending,to_state=checkout)
    
    

    def __init__(self, name):
        self.name=name