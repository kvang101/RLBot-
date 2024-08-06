# This file is for strategy

from util.objects import *
from util.routines import *

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    is_defending = False
    is_attacking = False
    is_kickoff = True
    current_state = None
    
    def run(self):
        # Kick off 

        if self.kickoff_flag:
            is_kickoff = True
            self.set_intent(goto(self.ball.location))
            self.set_intent(kickoff())
            return
        else:
            is_kickoff = False

        # Check Ball location and base intent off of it
        if self.ball.location.y <= 600 and self.ball.location.y >= -600:
            is_attacking = True
            is_defending = False
        else:
            is_defending = True
            is_attacking = False
        
        #print(dir(self))
        
        # Attacking Routines
        if is_attacking:
            self.set_intent(atba())


        # Defending Routines
        if is_defending:
            self.set_intent(goto(self.friend_goal.location))
        
        if is_defending == True:
            current_state = 'Defending'
        elif is_attacking == True:
            current_state = 'Attacking'
        else:
            current_state = 'Idle'
        
        print(current_state)