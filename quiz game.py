print("**********************************")
print("welcome to Quizz Game!!")
import time
from quiz_database import question_bank
from quiz_database import options

skipped=0
attempt=0
max_attempts=3
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    return False
reattempt="YES"
while reattempt=="YES" and attempt<max_attempts:
    attempt+=1
    score=0
    print(f"\nAttempt{attempt}")
    start_time=time.time()
    for question_num in range(len(question_bank)):
        print("**********************************")
        print(question_bank[question_num]["text"])
        for i in options[question_num]:
            print(i)
        guess=input("Enter your answer(A/B/C/D or S) : ").upper()
        if guess=="S":
            print("Question Skipped")
            skipped+=1
            continue
        
        is_correct=check_answer(
            guess,
            question_bank[question_num]["answer"])
        if is_correct:
            print("correct answer")
            score+=1
        else:
            print("Incorrect answer")
            print(f"Correct Answer is {question_bank[question_num]['answer']}")
        print(f"your current score is {score}/{question_num+1}")
    print(f"your final score is {score}")
    end_time=time.time()
    total_time=end_time-start_time
    minutes=int(total_time//60)
    seconds=int(total_time%60)
    percentage=(score/len(question_bank))*100
    print(f"your score in percentage {percentage:.2f}%")
    print(f"you got {score} out of {len(question_bank)}")

    if percentage>=60:
        print("Result:pass")
    else:
        print("Result:Fail")
    print(f"Time taken: {minutes} min {seconds} sec")
    print(f"Number of questions skipped {skipped}")
    print(f"Number of times you attempted the quiz {attempt}")
    if attempt<max_attempts:
        reattempt=input("Do You Want to reattempt the quiz(YES/NO): ").upper()
    else:
        print("You have reached maximum attempts")