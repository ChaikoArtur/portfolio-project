import turtle


def draw_logo():
    screen = turtle.Screen()
    screen.title("Arthur Portfolio Logo")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)

    colors = ["#00FFFF", "#00FF00", "#FF00FF", "#FFD700"]

    # КРУГОВОЙ НЕОН-ДИЗАЙН
    for i in range(36):
        t.color(colors[i % 4])
        t.circle(100)
        t.right(10)

    # ИМЯ В ЦЕНТРЕ
    t.penup()
    t.goto(0, -20)
    t.color("white")
    t.write("ARTUR", align="center", font=("Arial", 28, "bold"))

    t.goto(0, -60)
    t.write("PORTFOLIO PROJECT", align="center", font=("Arial", 12, "normal"))

    t.hideturtle()
    turtle.done()


if __name__ == "__main__":
    draw_logo()