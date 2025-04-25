def The_multiplication_game():
    
    # Importing the random library: the numbers used to generate the exercises will be random    import random
    willingness = 0
    
    # Selecting the level
    questions = int(input('As many questions as you like? '))
    level = int(input('Choose a level from 1-3. '))
    
    # Based on the selected level, define the numbers
    if level == 1:
        level_1 = 2
        level_2 = 5
    elif level == 2:
        level_1 = 5
        level_2 = 10       
    elif level == 3:
        level_1 = 10
        level_2 = 20    
    print (' ')
    
    for q in range(0,questions):
        num_1 = random.randint(level_1,level_2)
        num_2 = random.randint(level_1,level_2)   
        print ('Question number', q+1)
        print (num_1, "X", num_2, '= ?')
        answer = int(input())

    # Define the response based on the answer the user provided

        # If the user's answer is correct, several responses will be defined and randomly selected
        if answer == num_1 * num_2 :
            willingness = willingness +1
            op = random.randint(1,3)
            if op == 1:
                print ('very good!')
            elif op == 2:
                print('excellent!! ')
            else:    
                print('Amazing :-)')
            print ('')

        # If the user's answer is incorrect, several responses will be defined and randomly selected    
        else:
            op = random.randint(1,3)
            if op == 1:
                print('Incorrect :-(')
            elif op == 2:
                print('wrong!! ')
            else:    
                print('very bad')
        
        print ('')

    # Print the number of correct answers given
    print('You have', willingness ,'correct answers Out of',questions)

The_multiplication_game()    
