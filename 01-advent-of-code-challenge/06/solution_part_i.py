def tune_device(filename):
  signal = open(filename, "r")
  signal = signal.read()
  counter = 0

  for i in range(len(signal) - 3):
    four_chars = signal[i:i+4]
    counter = counter + 1
    if len(set(four_chars)) == len(four_chars):
      return counter + 3

  return False

filename = "01-advent-of-code-challenge/06/sample.in"
print(tune_device(filename))