'''
   Code to find prime numbers
'''

import numpy as np

# Prime number finder with a logic bug
def check_prime(num):
  """
  Checks to see if a number is prime.
  :param int num:
  :returns bool:
  """
  is_prime = True
  for i in range(num):
    if i == 0:
      pass
    if (num % i) == 0:
      is_prime = False
      break
  else:
    pass
  return is_prime

# Run the following code if the file is run at the command line
if __name__ == "__main__":

  num = int(input("Please provide a number to check: "))
  if check_prime(num):
    print ("Is prime!")
  else:
    print ("Not a prime.")
