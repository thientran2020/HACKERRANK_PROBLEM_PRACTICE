# check if x and y can form s
# exactly match <=> len(s) = len(x) + len(y)
# for example: x = "1011", y = "000" and s = "100011"
def CheckInterweaving(x, y, s):
  # Base case 1: all empty string --> exactly match
  if x == "" and y == "" and s == "":
    return True
  
  # Base case 2: s is empty but at least x or y is not
  if s == "":
    return False
  
  # Recursively calls for smaller length
  # Case 1: first letter of x matches first letter of s
  if len(x) > 0 and s[0] == x[0]:
    return CheckInterweaving(x[1:], y, s[1:])

  # Case 2: first letter of y matches first letter of s
  if len(y) > 0 and s[0] == y[0]:
    return CheckInterweaving(x, y[1:], s[1:])  
  return False

def isInterweaving(x, y, s):
  # Edge case 1: s's length is not long enough to have x and y
  if len(s) < len(x) + len(y):
    return False
  
  # Edge case 2: s doesn't have all characters in x and y
  if not all([ch in s for ch in set(x)]) and not all([ch in s for ch in set(y)]):
    return False
  
  # Define max number of repetitions can exist for x and y
  max_number_of_repetitions_for_x = (len(s) - len(y)) // len(x)
  max_number_of_repetitions_for_y = (len(s) - len(x)) // len(y)

  # Generate some repetitions of x and y: x' and y'
  # Generate substring s' of s such that: len(s') = len(x') + len(y') 
  # and use CheckInterweaving to check
  for k_x in range(1, max_number_of_repetitions_for_x + 1):
    for k_y in range(1, max_number_of_repetitions_for_y + 1):
      generated_repetition_of_x = x * k_x
      generated_repetition_of_y = y * k_y
      expected_length_of_s = len(generated_repetition_of_x) + len(generated_repetition_of_y)
      if expected_length_of_s > len(s):
        continue
      for i in range(len(s) - expected_length_of_s + 1):
        # only take a substring of s <=> discard symbols in the beginning or at the end of s
        # len(generated_s) = len(generated_repetition_of_x) + len(generated_repetition_of_y)
        # satisfy condition for CheckInterweaving()
        generated_s = s[i:i+expected_length_of_s] 
        result = CheckInterweaving(generated_repetition_of_x, generated_repetition_of_y, generated_s)
        if result:
          print(generated_s, " <===>", generated_repetition_of_x, generated_repetition_of_y)
          return True
  return False

def main():
  testcases = [("101", "0", "100010101"), ("101", "0", "1100010101"), ("1011", "10", "1100010101")]
  for testcase in testcases:
    x, y, s = testcase
    print("_________Test Case________")
    print("x = {}\ny = {:20s}\ns = {}".format(x, y, s))
    if isInterweaving(x, y, s):
      print("s = {} is an interweaving of {} and {}\n".format(s, x, y))
    else:
      print("s = {} is NOT an interweaving of {} and {}\n".format(s, x, y))
  
main()