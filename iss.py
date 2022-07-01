from turtle import Turtle, Screen

screen = Screen()
screen.addshape("images/iss.gif")


class Station(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("images/iss.gif")
        self.penup()
        self.hideturtle()


class Information(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#FFFBE7")
