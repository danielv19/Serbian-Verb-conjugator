def accessible(a):
  return a.replace(" ", "").lower()

def firstPersonPresent(stem, number):
  result = ""
  if number == 1:
    result = stem + "m"
  else:
    result = stem + "mo"
  print(result)
  return result

def secondPersonPresent(stem, number):
  result = ""
  if number == 1:
    result = stem + "s"
  else:
    result = stem + "te"
  print(result)
  return result

def thirdPersonPresent(verb, wordext, stem, number):
  result = ""
  if number == 1:
    if original[wordext] == ('e'):
      stem = original [0:wordext]
      result = stem + "i"
    else:
      result = stem
  else:
    if original[wordext] == ('a'):
      result = stem + "ju"
    else:
      stem = original [0:wordext]
      result = stem + "e"
  print(result)
  return result

def future(stem, tense, number):
  stem = stem + "c"
  if tense == 1:
    if number == 1:
      stem =  stem + "u"
      print(stem)
    else:
      stem =  stem + "e"
      firstPersonPresent(stem, number)
  stem =  stem + "e"
  if tense == 2:
    secondPersonPresent(stem, number)
  elif tense == 3:
    print(stem)

def biti (tense, number):
  if tense == 1:
    if number == 1:
      return "sam"
    else:
      return "smo"
  if tense == 2:
    if number == 1:
      return "si"
    else:
      return "ste"
  if tense == 3:
    if number == 1:
      return "je"
    else:
      return "su"

def past_gender(stem, number, gender):
  if number == 1:
    if gender == "m":
      return stem + "o"
    elif gender == "f":
      return stem + "la"
    else:
      return stem + "lo"
  else:
    if gender == "m":
      return stem + "li"
    elif gender == "f":
      return stem + "le"
    else:
      return stem + "la"
    
def past(tense, number, gender, stem):
  return past_gender(stem, number, gender) + " " + biti(tense, number)


    

original = input("Type BCS (Bosnian-Serbian-Croatian) Verb: ")
org = len(original)
original = accessible(original)
stem = original [0:(org - 2)]
wordext = (org) - 3

if org >= 4 and original.isalpha():
  num = input ("Singular or Plural?")
  pers = input ("First, Second, or Third Person?")
  num = accessible(num)
  pers = accessible(pers)
  number = 1
  tense = 1

  if num[0] == "s":
    if pers[0] == "f" or pers[0] == "1":
      firstPersonPresent(stem, number)
    elif pers[0] == "s" or pers[0] == "2":
      secondPersonPresent(stem, number)
      tense = 2
    else:
      thirdPersonPresent(original, wordext, stem, number)
      tense = 3
  else:
    number = 2
    if pers[0] == "f" or pers[0] == "1":
      firstPersonPresent(stem, number)
    elif pers[0] == "s" or pers[0] == "2":
      secondPersonPresent(stem, number)
      tense = 2
    else:
      thirdPersonPresent(original, wordext, stem, number)
      tense = 3

  past_permission = input ("Do you want the past tense?")
  past_permission = accessible(past_permission)
  if past_permission[0] == "y":
    gender = input ("Which gender for the past tense?")
    gender = accessible(gender)
    print(past(tense, number, gender[0], stem))

  future_permission = input ("Do you want the future tense?")
  future_permission = accessible(future_permission)
  if future_permission[0] == "y":
    future(stem, tense, number)

print("Thank you for using this BCS verb conjugator")
exit()
