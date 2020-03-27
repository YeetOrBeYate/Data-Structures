

yeet = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

yoot = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]



def yate(array):

    divisible = []

    for x in array:
        if x % 3 == 0:
            divisible.append(x)

    return divisible

print(yate(yeet))
        