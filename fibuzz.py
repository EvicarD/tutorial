def fizz_buzz(num):
  try:
    assert num == int(num)
    for i in range(1, num):
      if i % 2 == 0:
        print(i, "fizz")
      elif i % 2 == 1:
        print(i, "buzz")
  except AssertionError:
    print("enter number")
  finally:
    print("try again")

fizz_buzz("100")