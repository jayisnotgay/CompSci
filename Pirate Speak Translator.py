print("Welcome to pirate speak translator! (Please enter non-capital letters)")
translate = str(input("What do you want to translate? "))
print("Translated= " + translate.replace("ing","in'").replace("and","an'").replace("hi","ahoy")\
      .replace("you","ye").replace("my","me").replace("friend","matey").replace("buddy","matey")\
      .replace("hey","'ay").replace("are","be").replace("is","be").replace("am","be").replace("have","'ave") + "!")