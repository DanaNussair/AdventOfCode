from .data import input_string

# Prepare data
arr = input_string.split("\n")
passRules = []

for passRule in arr:
    chars = passRule.split(":")
    passRules.append((chars[0], chars[1]))

# Perform passcode check
def perform_part_one_pass_check(passRules):
  valid = 0
  for passRule in passRules:
    rule, char = passRule[0].split(' ')
    min, max = rule.split('-')
    count = passRule[1].count(char)
    if count >= int(min) and count <= int(max):
      valid += 1

  return valid

def perform_part_two_pass_check(passRules):
  valid = 0
  for passRule in passRules:
    rule, char = passRule[0].split(' ')
    first, last = rule.split('-')
    passcode = passRule[1]
    if (passcode[int(first)] == char or passcode[int(last)] == char) and not (passcode[int(first)] == char and passcode[int(last)] == char):
      valid += 1

  return valid 


print("Part One: {}".format(perform_part_one_pass_check(passRules)))
print("Part Two: {}".format(perform_part_two_pass_check(passRules)))