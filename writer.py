counter = 0
counter2 = 0
counter3 = 0
counter4 = ""
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
def variables(data, counter4):
     for line in data.split('\n'):
        counter4 += line
        counter4 = counter4 + ("\n")
        lineHalf = line.split("=")
        counter4 = counter4 + ("\n")
        counter4 += lineHalf[0]
        counter4 += str(len(lineHalf))
        if len(lineHalf) == 2:
            counter4 = counter4 + ("\n")
            counter4 += lineHalf[1]
     return counter4

variables(data, counter4)
with open("results.txt", "w") as fileDescriptor:
    fileDescriptor.write(str(variables(data, counter4)))
