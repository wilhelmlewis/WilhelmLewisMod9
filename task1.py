import turtle

class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def __drawHead(self):
        turtle.penup()
        turtle.goto(0,-100)
        if self.isHappy():
            turtle.setheading(0)
            turtle.color("yellow")
        else:
            turtle.setheading(0)
            turtle.color("red")
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()

    def __drawEyes(self):
        turtle.penup()
        turtle.goto(-45,45)
        if self.isDarkEyes():
            turtle.color("black")
        else:
            turtle.color("blue")
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(45,45)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()

    def __drawMouth(self):
        turtle.penup()
        if self.isSmile():
            turtle.goto(-60,-60)
            turtle.setheading(-48)
        else:
            turtle.goto(60,-60)
            turtle.setheading(132)
        turtle.width(10)
        turtle.pendown()
        turtle.color("black")
        turtle.circle(90,90)
        turtle.penup()
        turtle.width(1)

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()

def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isHappy() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
            face.isSmile
        elif menu == 2:
            face.changeEmotion()
            face.isHappy
        elif menu == 3:
            face.isDarkEyes
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()

main()