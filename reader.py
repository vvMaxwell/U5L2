counter = 0
counter2 = 0
counter3 = 0
with open("sample.ini") as fileDescriptor:
        data = fileDescriptor.read()
for letter in data:
    if letter in ["a","e","i","o","u"]:
        counter += 1
        print(f"total vowel count is {counter}")
for number in data:
    if number.isdigit():
         counter2 += 1
         print(f"total numbers count is {counter2}")
for words in data:
     if words in data.split():
          counter3 += 1
          print(f"total word count is {counter3}")
def variables(data):
     for line in data.split('\n'):
        print(line)
        lineHalf = line.split("=")
        print(lineHalf[0])
        print(len(lineHalf))
        if len(lineHalf) == 2:
             print(lineHalf[1])
variables(data)

