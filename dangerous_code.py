# Python script with dangerous function

import sys

def calculate(expression):
  # This use of eval is dangerous!
  result = eval(expression) # Medium severity expected
  print(f"Result: {result}")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    calculate(sys.argv[1])
  else:
    print("Please provide an expression.")
