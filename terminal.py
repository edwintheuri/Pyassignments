import random 
grading = 0 # tracking the score of user

# creating a list with a dictionary



Exam = [
   {
       "Question":"What is the capital of Kenya",
       "Choice":["A: Africa","B: Nairobi", "C: Mombasa", "D: None"],
       "Answer":"B"
   },
   {
       "Question":"What is the capital of Uganda",
       "Choice":["A: Kampala","B: Nairobi", "C: Mombasa", "D: None"],
       "Answer":"A"
   },
   {
       "Question":"What is the capital of Tanzania",
       "Choice":["A: Africa","B: Nairobi", "C: Mombasa", "D: None"],
       "Answer":"D"
   }
]

random.shuffle(Exam)

#Looping the questions

for Chapter in Exam:
    print (Chapter['Question'])
    for Options in Chapter['Choice']: #going through the choices
        print(Options)
    print("-"*20)

    try:
        answer = input('Enter your answer, A , B , C or D : ')
        #check user input 
        if answer == Chapter['Answer']:
            grading += 5
            print(f'Correct, {grading} Added')
        else:
            print('Fail, answer is', Chapter['Answer'] )
    except:
        print('Enter either A, B, C, or D')

print("-"*20)
print(f'You have , {grading} marks')


 
    

 
 



 