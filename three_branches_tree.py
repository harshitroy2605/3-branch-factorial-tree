import turtle

# sent by: ahmedbird97@gmail.com

def tree(i):
	if i<30:
		return
	else:
		# ---------- angle = 45 degrees ----------

		hr.forward(i)
		hr.left(45)
		tree(3*i/4)
		hr.right(45)
		tree(3*i/4)
		hr.right(45)
		tree(3*i/4)
		hr.left(45)
		hr.backward(i)

		# ---------- angle = 50 degrees ----------

		# hr.forward(i)
		# hr.left(50)
		# tree(3*i/4)
		# hr.right(50)
		# tree(3*i/4)
		# hr.right(50)
		# tree(3*i/4)
		# hr.left(50)
		# hr.backward(i)

		# ---------- angle = 70 degrees ----------

		# hr.forward(i)
		# hr.left(70)
		# tree(3*i/4)
		# hr.right(70)
		# tree(3*i/4)
		# hr.right(70)
		# tree(3*i/4)
		# hr.left(70)
		# hr.backward(i)

hr = turtle.Turtle()

hr.left(90)
hr.penup()
hr.backward(150)
hr.pendown()
hr.speed(150)
tree(100)

turtle.done()
