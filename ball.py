from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_cor = 2
        self.y_cor = 2

    def move_ball(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_cor *= -1

    def bounce_paddle(self):
        self.x_cor *= 1.2
        self.x_cor *= -1

    def reset(self):
        self.home()
        self.bounce_paddle()

    def reset_ball_speed(self):
        self.x_cor = 2
