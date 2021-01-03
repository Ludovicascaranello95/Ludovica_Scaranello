#!/usr/bin/env python
# coding: utf-8

# In[3]:




"""    DocString:   

A) Introduction:   

This game is based on my dog, it  has 3 levels and with different endings: 

1) Chase revenge   
2) Fight    
3) Make a new friend

You win if Bombo make it throu the day.

B) Known Bugs and/or Errors:    

Coming back to the starting point once failed."""




#game introduction 
#importing external tools 
from sys import exit

#defining the game and print the introduction statement
def game_start():
    print("""


    The birds are singing and the sun is about to rise: it's a new day in the big house garden. 
    Bombo,a white and red English setter, is so thrilled to begin another day getting into 
    trouble and drive Mr.Bubble, his owner, crazy!\n""") 

#first quest and imput prompt 
    print("\n Are you ready for this adventure?\n") 

    input(prompt= "press enter to continue")
    
#user name and capitalization of first letter 
    user_name = input(prompt = "What's your name? ").capitalize()
    
    user_country = input(prompt = "Where are you originally from? ").capitalize()
    
    print(f"""\n\n Welcome {user_name} from {user_country} it's nice to meet you!\n\n """)

#game explication and first variable 
    print(f"""

    You have to know that Bombo gets excited over scaring the birds that live in the garden
    but mostly he loves giving a rough time to Solero, Miss Bigfoot's annoying black cat that
    steals Bombo's food and dares to take naps on the top of his doghouse!

    When TallyHo, a fox that likes to have a walk across the garden, come over,  
    Bombo enjoys chasing after her to play hunt. 

    But {user_name} watch out to Scar, the old badger does not like to have Bombo around and he might fight him 
    if he invades his territory again!



    """)

#second quest 

    print ("""
                    A Yes
                    B No 
                """)
#defining the loop and conditional statement
    A=1
    while A == 1 :

        user_answer= input("\n\n Are you ready to get Bombo into troubles today?\n\n").lower()
        
            
        if user_answer == "yes" or user_answer == "a" :

            print ("\nGreat! Let's play!\n")
            A=0 

        elif user_answer == "no" or user_answer == "b" : 

            print ("\n\n IMPOSSIBLE\n\n This would be the first time ever...Let's play!\n\n") 
            A=0
        else: 
            print("\n\n Try again!\n\n ")



#end intro   

    print("\n Get Ready For The Adventure!\n")



#Round_1  

    print("""\n Bombo is running into the garden while he smells some interesting trails. 
    While he was following it, he heard Solero eating his breakfast:\n""")


    #Second loop and nested conditional statement  

    A=1 
    while A==1: 

        print ("""

        A) Bombo decide to chase after Solero to cast him out from the garden. 

        B) Bombo decide to leave Solero and keep following the trail's path. 

        """) 

        user_answer = input ("\n\n What would Bombo do?\n\n").lower()
        
#fail function for answer A and GAME OVER, second loop

        if user_answer == "a" or user_answer == "chase the cat or Solero or garden" :
            print ("\n\n Bombo is in Miss Bigfoot's garden!\n\n") 
            print ("\n\n OH NO! Bombo got stuck in the old grandma's garden,Mr.Bubble is coming to take him home\n\n")
            A=0
            fail()

        elif user_answer == "b" or user_answer =="leave Solero or follow trail's path" : 
            print ("\n\n For this time Solero is safe\n\n")
            A=0 
            room_1()

        else: 
            print("\n\n Bombo, the trail is disapperiring: you have to make a decision!\n\n ")



#Round_2 
#defining the first room
        
def room_1():  
    
    print("""
    While following the trails, TallyHo the fox appeared in front of Bombo: 
    they decided to play chasing when Bombo find himself in Scar's territory! 
    The old Badger awared the dog that he would incur in a fight 
    if they ever meet again!""")

    print ( """\n\n What's about to happen?\n\n""")

#third loop and conditional statement 
    A=1 
    while A==1 :

        print( """
        A) Bombo decide to fight Scar. 
        B) Bombo decide to run away and get back following the trail's path. 
        """)  

        user_answer = input(prompt= "What's about to happen?").lower()

#fail function and Game Over for answer A, third loop 

        if user_answer == "a" or user_answer == "fight Scar" : 
            print("\n\n OH NO! Bombo got injured!\n\n")
            fail ()
            A=0 



        elif user_answer == "follow the path" or user_answer == "b": 
            print("\n\n Keep on going, Bombo\n\n")
            A=0
            room_2()
            
        else: 
            print("\n\n Again, what's about to happen?\n\n ")
#Round_3 

#defining the second room 
def room_2(): 
    
    print ("""\n Bombo finally discovers where's the trail's path comes from: 
    a hedgehog appears from the hydrangeas bushes!\n """)
    
    print("\n\n What's after? \n\n ")
     
#third loop and countdown         
    B=1
    while B==1:
    
        print("""\n 
        A) Bombo decide to smell the hedgehog to say HI and be his friend.
        B) Bombo decide to follow the hedgehog to find where he lives. 
        """)
    
        user_answer=input(prompt=("What's after?")).lower()                   
        if user_answer == "a" or user_answer == "smell the hedgehog": 
            count=3 
            while count > 0: 
                print("\n Snuff\n ")
                count=count -1 
                input("\n\n < Press enter to smell the hedgehog>\n\n ")
                print ("\n\n Bombo's made a new friend! \n\n ")
                B=0
                win()
                      
        elif user_answer== "b" or "follow the hedgehog":
                print("\n\n Bombo got stucked in the hydrangeas bushes, silly dog! \n\n")
                B=0 
                win()
                      
    input(prompt="press any keys to continue")            

#definition of Fail finction and EXIT

def fail():
    print("\n\n Poor Bombo, GAME OVER\n\n")
    exit()
    
#definition of Win function and EXIT
def win():
    print("\n\n WELL DONE! Bombo had fun today!\n\n")
    print("\n\n\n The sun is going down the hill, it's time for Bombo to going home to Mr.Bubble!\n\n\n ")
    exit()
    
#closure of the game
game_start() 


# In[ ]:




