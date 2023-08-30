x = int(input("Enter x: "))
y = int(input("Enter y: "))

if (x + y) != 0:
  res = abs(x - y) / (x + y)
  print(res)
else:
  print("x + y can't be 0!")
