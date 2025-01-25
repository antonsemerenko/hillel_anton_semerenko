user_input = input("Please enter any 4-digit integer: ")
number = int(user_input)
x=100
left,right = (divmod(number,x))
y=10
left,right = (divmod(number,y))
print(left)
print(right)
z=10
up,down = (divmod(right,z))
print(up)
print(down)

