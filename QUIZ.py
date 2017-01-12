# quiz4fun
#Trivia quiz
print("This is a quiz that tests your knowledge of History and Space")
name = input("Enter your name: ")

print("Hello " + name + " are you ready to take this quiz?")

print("I will ask 10 questions and three choices for each question.")
print("Select the right answer by pressing A, B or C.")

print("______________________________________________________________")

#set the quiz score to 0.
score = 0
score = int(score) #convert the 0 into a number

print("Question 1")
print("Who was the first president of the United States?")
print("A. George Washington")
print("B. Thomas Jefferson")
print("C. Alexander Hamilton")
Q1answer = 'a'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="a":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("THAT IS INCORRECT YOU FOOL!")

print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 2")
print("Who was the first human on the moon?")
print("A. John F Kennedy")
print("B. Neal Armstrong")
print("C. Pete Normstrong")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("u stupid")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 3")
print("What year did the American Civil War start?")
print("A. 1944")
print("B. 1850")
print("C. 1861")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="C" or Q1response =="c":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Come on man this isin't even that hard...")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 4")
print("Which is the first known human civiliztion?")
print("A. England")
print("B. Mesopotamia")
print("C. Egypt")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("wrong...")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 5")
print("Which English writer is known for his famous Sonets?")
print("A. Shakespheare")
print("B. Orwell")
print("C. King George III")
Q1answer = 'a'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="A":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("This was not that difficult, and yet you somehow failed, good job.")

print("Your current score is " + str(score) + " out of 10.")
print("__________________________________")
print("Question 6")
print("Which nation first got a satalite in orbit?")
print("A. Soviet Union")
print("B. USA")
print("C. Canada")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Think of the Sputnik, INCORRECT.")
print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 7")
print("Which European discovered America in 1492?")
print("A. Colombus")
print("B. America")
print("C. Washington")
Q1answer = 'a'
Q1response = input('your answer: ')
if Q1response =="A" or Q1response =="A":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("Incorrect")

print("Your current score is " + str(score) + " out of 10.")

print("__________________________________")
print("Question 8")
print("Who is the current POTUS of the United States?")
print("A. Obama")
print("B. Trump")
print("C. King George III")
Q1answer = 'b'
Q1response = input('your answer: ')
if Q1response =="B" or Q1response =="b":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("This was not that difficult, and yet you somehow failed, good job.")
print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 9")
print("How many planets are there in our solar system? (not including dwarf planets)")
print("A. 9")
print("B. 8")
print("C. Unknown")
Q1answer = 'c'
Q1response = input('your answer: ')
if Q1response =="C" or Q1response =="c":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("While there are 8 known planets, astronomers beleive in the possibility that there could be another planet beyond the Kuiper Belt.")

print("Your current score is " + str(score) + " out of 10.")


print("__________________________________")
print("Question 10")
print("Why did the chicken cross the road?")
print("A. To get to the other side.")
print("B. To go to KFC")
print("C. Because he was happy he was done with this damn quiz")
Q1answer = 'c'
Q1response = input('your answer: ')
if Q1response =="C" or Q1response =="c":
    print("Well done " + name + " your response is correct!")
    score = score +1

else:
    print("woulden't you be happy if you were done with this too?")

print("Congrats! You finished the quiz, your final score is " + str(score) + " out of 10.")
