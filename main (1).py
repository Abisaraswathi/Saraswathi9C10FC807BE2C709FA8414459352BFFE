def fact_rect(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rect(n - 1)


number = int(input("Enter the number:"))
res = fact_rect(number)
print("The Factorial of {} is {}".format(number, res))
