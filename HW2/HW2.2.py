print('Mr.Oleg')
number=int(input("Please enter any 5-digit integer:  "))
y=10000
a,b = (divmod(number,y))
y=1000
c,d = (divmod(b,y))
y=100
e,f = (divmod(d,y))
y=10
g,h = (divmod(f,y))
number2=(h*10000)+(g*1000)+(e*100)+(c*10)+(a*1)
print(number2)

