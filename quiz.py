name = input("enter your name:")
score = 0

ans1 = input("Ques 1 : What is the capital of Australia?:")
if ans1.lower() == "canberra":
    print("correct")
    score +=1

else:
    print("incorrect")

ans2 = input("Ques 2 : Who wrote the play Romeo and Juliet?:")
if ans2.lower() == 'william shakespeare':
    print("correct")
    score +=1

else:
    print("incorrect")

ans3 = input("Ques 3 : Which planet is known as the Red Planet?:")
if ans3.lower() == 'mars':
    print("correct")
    score +=1

else:
    print("incorrect")

ans4 = input("Ques 4 : Who invented the telephone?:")
if ans4.lower() == 'alexander graham bell':
    print("correct")
    score +=1

else:
    print("incorrect")

ans5 = input("Ques 5 : Which kanguage is used for machine learning?:")
if ans4.lower() == 'python':
    print("correct")
    score +=1

else:
    print("incorrect")

print(f"Your score for the quiz iz : {score}/5")
if score == 5:
    print("excellent job!")
elif score == 4:
    print("good work!")
elif score == 3:
    print("Can do better!")
elif score == 2:
    print("Need practise.")
elif score == 1:
    print("Very poor.")
else:
    print("Fail")




