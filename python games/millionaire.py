#create a quiz show using list and display final amounts the winner gets  

questions = [
    ["Which Democratic party Representative became Republican during the US election 2024?",
     "Tulsi Gabbard", "JD Vance", "Vivek Ramaswamy", "Kamala Harris", 1],
    
    ["Date of Nova festival massacre is?",
     "OCT 7, 2024", "OCT 7,2023", "JAN 7, 2024", "JAN 7, 2023", 2],
    
    ["Where did the assassination attempt of Trump take place?",
     "Chicago", "San Francisco", "Massachusetts", "Pennsylvania", 4],
    
    ["Which country declared war against Israel recently?",
     "Iran", "Palestine", "Jordan", "Egypt", 1],
    
    ["Consider the following statements about the Chief Justice of India:\n"
     "The Chief Justice of India is appointed by the President of India.\n"
     "The Chief Justice of India has a fixed tenure of 5 years.\n"
     "The Chief Justice of India has the power to appoint judges to the Supreme Court.\n"
     "How many of the statements given above are correct?",
     "Only one", "Only two", "All three", "None", 1]
]

money = 0
levels = [1000, 3000, 5000, 80000, 320000]

for i in range(0, len(questions)):

    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}\n")
    print(question[0], "\n")

    print(f"a. {question[1]}                b. {question[2]}")
    print(f"c. {question[3]}                d. {question[4]}")
    print("\n")

   
    while True:
        try:
            reply = int(input("Enter the answer (option: 1/2/3/4): "))
            if reply not in [1, 2, 3, 4]:
                print("Invalid input. Please choose between 1, 2, 3, or 4.")
            else:
                break  
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    
    if i == 0 and reply != question[5]:
        print("Wrong answer on the first question! You lost this round.")
        money = 0
        break

    
    if reply == question[5]:
        print(f"Right answer! You won Rs {levels[i]}")
        if i < 3:
            money += levels[i]
        else:
            money = 80000
    else:
        print("Wrong answer! You lost this round.")
        break 

print(f"Total money won: Rs {money}")
