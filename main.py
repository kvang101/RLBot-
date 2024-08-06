# This file is for strategy

from util.objects import *
from util.routines import *

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    
    def run(self):
        if self.intent is not None:
            return
        
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_in_front_of_ball = d1 > d2

        df1 = abs(self.ball.location.y - self.friend_goal.location.y)
        df2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_defending = df1 < 200

        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        if is_defending:
            ball_x = self.ball.location.x
            ball_z = self.ball.location.z
            destination = Vector3(ball_x,df1-df2,ball_z)
            self.set_intent(goto(destination))
        if is_in_front_of_ball:
            self.set_intent(goto(self.friend_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))
        print(is_defending)

        