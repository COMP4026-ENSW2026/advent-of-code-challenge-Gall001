def backpack(filename):

    with open(filename, "r") as list:
        input = list.read()
        value = 0

    array = input.splitlines()

    for item in array:
      str1 = item[:len(item) // 2]
      str2 = item[len(item) // 2:]
      count = 0
      for char1 in str1:
        for char2 in str2:
          if char1 == char2 and count == 0:
            value = value + character_score(char1)
            count = 1


    return value

def character_score(char):
  if 'a' <= char <= 'z':
    return ord(char) - ord('a') + 1
  elif 'A' <= char <= 'Z':
    return ord(char) - ord('A') + 27

filename = "01-advent-of-code-challenge/03/sample.in"
print(backpack(filename))