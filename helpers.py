from random import randint

points: int = 0
album: str = ""

def q1(answer: str) -> str:
    """Question One."""
    global points
    if answer == 'Going to the club with your best friends':
        points += 1
    elif answer == 'Reading a book on the porch with your cat on your lap':
        points += 2
    else:
        points += 3

def q2(answer: str) -> str:
    """Question Two."""
    global points
    if answer == 'Blue/Pink':
        points += 1
    elif answer == 'Black/Yellow':
        points += 2
    else:
        points += 3
        
        
def q3(answer: str) -> str:
    """Question Three."""
    global points
    if answer == 'Horse':
        points += 1
    elif answer == 'Lion':
        points += 2
    else:
        points += 3
        
        
def q4(answer: str) -> str:
    """Question Four."""
    global points
    if answer == 'Coffee':
        points += 1
    elif answer == 'Whiskey':
        points += 2
    else:
        points += 3
        
        
def q5(answer: str) -> str:
    """Question Five."""
    global points
    if answer == 'Polaroid':
        points += 1
    elif answer == 'Phone camera':
        points += 2
    else:
        points += 3
        
        
def q6(answer: str) -> str:
    """Question Six."""
    global points
    if answer == 'Extremely!!!':
        points += 1
    elif answer == 'Everyone knows everything about you':
        points += 2
    else:
        points += 3
        
        
def q7(answer: str) -> str:
    """Question Seven."""
    global points
    if answer == 'Kissing my love under the mistletoe':
        points += 1
    elif answer == 'Opening the first gift on the eve':
        points += 1
    else:
        points += 3
        
        
def q8(answer: str) -> str:
    """Question Eight."""
    global points
    if answer == 'Person born and raised in the city!':
        points += 1
    elif answer == 'Strong and independent individual':
        points += 2
    else:
        points += 3
        
        
def q9(answer: str) -> str:
    """Question Nine."""
    global points
    if answer == 'NYC':
        points += 1
    elif answer == 'Paris':
        points += 2
    else:
        points += 3
        
        
def q10(answer: str) -> str:
    """Question Ten."""
    global points
    if answer == 'Beyonce':
        points += 1
    elif answer == 'Kris Jordan':
        points += 2
    else:
        points += 3
        
        
def q11(answer: str) -> str:
    """Question Eleven."""
    global points
    if answer == 'Be the boss of a big company':
        points += 1
    elif answer == 'Who knows?! Life is an adventure!':
        points += 2
    else:
        points += 3
        
        
def q12(answer: str) -> str:
    """Question Twelve."""
    global points
    if answer == 'The Office':
        points += 1
    elif answer == 'Law & Order: SVU':
        points += 2
    else:
        points += 3
        
        
def q13(answer: str) -> str:
    """Question Thirteen."""
    global points
    if answer == 'Kit-Kats and Snickers':
        points += 1
    elif answer == 'Skittles':
        points += 2
    else:
        points += 3
        
        
def q14(answer: str) -> str:
    """Question Fourteen."""
    global points
    if answer == 'Ice Cream':
        points += 1
    elif answer == 'Revenge':
        points += 2
    else:
        points += 3
        
        
def q15(answer: str) -> str:
    """Question Fifteen."""
    global points
    if answer == 'Scottish Fold':
        points += 1
    elif answer == 'Ragdoll':
        points += 2
    else:
        points += 3


def all_results(result: int) -> str:
    """Count up all the points for an album."""
    global points
    if points <= 15:
        return cat_one
    elif points in range(16, 30):
        return cat_two
    else:
        return cat_three


def cat_one() -> None:
    """First three albums."""
    album: int = int(randint(1, 3))
    if album == 1:
        print("You got 'Taylor Swift'! You're a classic! Good ol' country gal who loves love! <3 You do have a feisty side so don't let trouble into your life!")
    if album == 2:
        print("You got '1989'! HELLO PARTY ANIMAL!!! You are shaking what your mama gave you, and having a good time doing it. Keep on dreaming, beacuse they're all going to come true.")
    if album == 3:
        print("You got 'Lover'! You met a British boy, love. And you couldn't be happier for it. You had to kiss a lot of frogs to get to your prince, but you know he's worth it. (And if you haven't met your British boy yet, don't worry, Harry Styles will be single again someday).")
        

def cat_two() -> None:
    """Second three albums."""
    album: int = int(randint(1, 3))
    if album == 1:
        print("You got 'Fearless'! Well hello there popular! You're the friend who's always a bridesmaid, never a bride. You just can't seem to find the right one but everyone comes to you for advice!")
    if album == 2:
        print("You got 'Reputation'! You are the baddest out there! ;) Don't let anyone kill your vibe because you are the best that you can be. You fight fire with an even bigger fire and there's absolutely nothing wrong with that.")
    if album == 3:
        print("You got 'Evermore'! You're what they call a chronic daydreamer. Always thinking up your perfect day, perfect love, perfect crime. You aren't taking what the universe gives you anymore; you're throwing it right back and carving your own path.")


def cat_three() -> None: 
    """Third three albums."""
    album: int = int(randint(1, 3))
    if album == 1:
        print("You got 'Speak Now'! Uhhh... how are you really feeling right now...? Don't worry, heartbreak doesn't last forever. You're better on your own! Pick up your crown, QUEEN!!!!")
    if album == 2:
        print("You got 'Red'! Now I don't want to assume you're going through a breakup... But you're always the one that's down for a good time even when you're sad! Don't forget to check in on yourself from time to time.")
    if album == 3:
        print("You got 'Folklore'! How does it feel creating fictional scenarios in your mind 24/7? It's okay, don't worry! Most of us do this but ours will never be as clever. You're a modern day Shakespeare. Keep on writing!!!")





# #class user:
#     id: int
#     first_name: str
    
#     def __init__(self, id: int, fname: str):
#         self.id = id
#         self.first_name = fname