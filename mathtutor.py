""" CREATE APPLICATION TO PRACTICE MULTIPLICATION TABLES. """
import random, time
print("Math Tutor")

def tutor(number):
    correct=0
    answer_list=[]
    question_list=[]
    time_taken = []
    
    table=int(input("How High should the table be? :"))
    
    for i in range(number):
        
        num1 = random.randint(1, table+1)
        num2 = random.randint(1, table+1)
        answer=num1*num2
        ques=f"What is {num1} x {num2} = ?: "
        
        start = time.time()
        guess=int(input(ques))
        end = time.time()
        
        timetaken = end - start
        print("Time Taken: ", round(timetaken))
        time_taken.append(round(timetaken))
        
        if guess == answer:
            correct+=1
            
        answer_list.append(answer)
        question_list.append(ques)
        
    print("Thank You For Playing!")
    print(f"Your Score: {correct}/{number}")
    per=(correct/number)*100
    print(f"Your percent: {per}%")
    qna=[(q, a) for q, a in zip(question_list, answer_list)]
    print("Question and Correct Answers: ", qna)
    print("Total Time Consumed (in seconds): ", sum(time_taken))

n=int(input("Enter the number of test questions you want: "))
tutor(n)
        
