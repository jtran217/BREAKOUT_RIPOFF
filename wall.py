from turtle import Turtle


class WallManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_wall = []
        self.x_pos = 275
        self.y_pos = 100
        self.count = 0
        self.layer = 0
        self.label = {}


    def create_wall(self):
        while self.count < 96:
            wall = Turtle()
            wall.shape('square')
            if self.count < 24:
                wall.color('yellow')
            elif self.count >= 24 and self.count < 48:
                wall.color('green')
            elif self.count >= 48 and self.count < 72:
                wall.color('orange')
            elif self.count >= 72:
                wall.color('red')
            wall.penup()
            wall.shapesize(stretch_wid=1,stretch_len=2)
            wall.goto(self.x_pos,self.y_pos)
            self.x_pos -= 50
            self.count += 1
            self.all_wall.append(wall)

            #NEXT LAYER
            if self.count%12 == 0:
                self.y_pos += 25
                self.x_pos = 275




