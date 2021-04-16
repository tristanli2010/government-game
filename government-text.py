print('Are you sure you want to start? y/n')
if input() == 'y':
    print('You wake up in a strange building. It looks very fancy, like a billionare\'s house\n. Oh wait. You know where this is. You are in the white house!')
    print('A person walks up to you. You have no idea who this person is. He asks, "Why are you in the white house? You don\'t even know anything about the government! Oh really? You know a lot about the government? Well lets see!"')
    print('Which branch of the government is the most powerful?')
    print('A. The executive branch')
    print('B. The legislative branch')
    print('C. The judicial branch')
    print('D. None of the above')
    x = input()
    if x == 'D' or x == 'd' or x.lower() == 'none of the above':
        print('"AHAHAHAHAHA... you got it incorrect! I guess you have to go home now."')
        print('"Just kidding... you got it correct."')
        print('*this person quitely plays classical music and you\'re asleep again*')
        print('You wake up again. This time, you are in a different building. It looks somewhat like the White House, but not really.')
        print('You find yourself in a weird room. It looks really fancy, so this must be the U.S capitol building right?')
        print('The guy walks up to you again and says "Ah, you finally woke up. That question was only a warm up. Time for the real thing now."')
        print('What branch mainly uses the U.S capitol building to work?')
        print('This question will be open-ended!')
        if 'legislative' in input().lower().split(): #this checks if the answer includes "legislative"
    
            print('Nice. But that was easy. Let\'ts move on.')
            print('I\'ll give you a lot questions. Let\'s see how many you get correct.')
            print('If you get a lot right, you\'ll get to stay.')
            print('What does the executive branch do?')
            questions_correct = 0
            print('A. Makes laws')
            print('B. Approve laws')
            print('C. Explain laws')
            print('D. Decide if a law follows the constitution')
            print('E. None of the above')
            if input().lower() == 'b':
                questions_correct += 1
            print('"I\'ll tell you if that answer was correct later"')
            print('"What does the legislative branch do?"')
            print('A. Make laws')
            print('B. Approve laws')
            print('C. Explain laws')
            print('D. Decide if a law follows the constitution')
            print('E. None of the above')
            if input().lower() == 'a':
                questions_correct += 1
                print('Good job!')
            print('What does the judicial branch do?')
            print('A. Makes laws')
            print('B. Approve laws')
            print('C. Explain laws')
            print('D. Decide if a law follows the constitution')
            print('E. Both C and D')
            print('F. Both C and A')
            if input().lower() == 'e':
                questions_correct +=1
            print('The legislative branch is made by which of the following:')
            print('A. The House of Representatives and the Senate')
            print('B. The Senate and the Supreme Court')
            print('C. The president')
            print('D. The cabinet')
            if input().lower() == 'a':
                questions_correct += 1
            print('Nice. You got all the questions correct. Or did you?')
            if questions_correct == 4:
                print('You\'ll probably get to stay. If you get the next 10 questions correct, that is')

            elif questions_correct > 1:
                print('Go home. There\'s almost no chance you\'ll stay')
            print('I\'m the president. I rule the world. Or do I? y/n')
            if input().lower() == 'y':
                print('You actually got that correct... how smart of you!')
                questions_correct += 1
            else:
                print('I don\'t rule the world. You probably didn\'t learn about the balance of the government haha.')
                
            print('How many people are members of congress?')
            print('Open ended this time!')
            if '535' in input().split():
                questions_correct += 1
            if questions_correct == 6:
                print('Congratulations!')
                print('You found the path everyone dreams to find. A government expert!')
            if questions_correct == 5 or questions_correct == 4:
                print('Nice try.')
                print('You aren\'t exactly a master at the government, but you\'re pretty good. I guess.')
            if questions_correct <4:
                print('You\'d better study. I hope one day you will become the president, just like me!')
                
        else:
            print('I understand. That was very hard. Hopefully you can get it right next time.')
    else:
        print('"Wow, you got it correct! Go home now, why would you ever get that easy question wrong?"')
        
        
else:
    print('Ok, hopefully you are ready next time!')
