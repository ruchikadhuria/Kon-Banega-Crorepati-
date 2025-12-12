import random
import time

# ----------Questions-----------
# ["Question", "Option1", "Option2", "Option3", "Option4", correct_option_number]
questions = [
    ["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Program Unit", 2],
    ["Which language is known as platform independent?", "C", "C++", "Java", "Assembly", 3],
    ["Which symbol is used for comments in Python?", "//", "/* */", "#", "<!-- -->", 3],
    ["Who developed Python?", "Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", 2],
    ["Which keyword is used to define a class in Java?", "class", "struct", "define", "object", 1],
    ["Which data type is used to store True/False in Python?", "int", "bool", "str", "float", 2],
    ["Which of these is NOT a programming language?", "Python", "Java", "HTML", "Windows", 4],
    ["What is the extension of Java bytecode files?", ".java", ".class", ".exe", ".js", 2],
    ["Which keyword is used to print output in Python?", "echo", "cout", "print", "printf", 3],
    ["Which company developed Java?", "Microsoft", "Apple", "Sun Microsystems", "Google", 3],
    ["Which loop is guaranteed to run at least once in Java?", "for", "while", "do-while", "foreach", 3],
    ["What does IDE stand for?", "Integrated Development Environment", "Internal Development Engine", "Integrated Design Editor", "Internal Design Environment", 1],
    ["Which operator is used for exponentiation in Python?", "^", "**", "//", "%", 2],
    ["Which keyword is used to define a function in Python?", "method", "function", "def", "func", 3],
    ["Which data structure stores key-value pairs in Python?", "list", "tuple", "dictionary", "set", 3],
    ["Which keyword is used to inherit a class in Java?", "implements", "inherits", "extends", "super", 3],
    ["Which symbol is used to end a statement in Java?", ".", ",", ";", ":", 3],
    ["Which of these is mutable in Python?", "tuple", "string", "list", "int", 3],
    ["Which loop is best when number of iterations is known?", "while", "do-while", "for", "infinite", 3],
    ["Which method is the entry point of a Java program?", "start()", "run()", "main()", "init()", 3],
]

#  ------------------------Prize Money ----------------
prize_money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,
               1250000,2500000,5000000,10000000,20000000,30000000,40000000,50000000,60000000]

# ----------------Guaranteed Levels ---------------
guaranteed_levels = {5: 10000, 9: 160000, 13: 2500000}

# ------------Lifelines---------
lifelines = {"50-50": True,"skip":True,"audience poll":True}

# -------Functions---------
def wrongAnswer(qno):
    secured = 0
    for level in guaranteed_levels:
        if qno >= level:
            secured = guaranteed_levels[level]
    return secured

def fifty_fifty(question):
    correct = question[5]
    options = [1,2,3,4]
    options.remove(correct)
    wrong = random.choice(options)
    return [correct, wrong]

def audiencePoll(correctAns):
    poll = {correctAns: random.randint(60,80)}
    remaining = 100 - poll[correctAns]
    for i in range(1,5):
        if i != correctAns:
            poll[i] = random.randint(0, remaining)
            remaining -= poll[i]
    return poll

# ---------Starting Game-------
print("🙏 Greetings! Welcome to the Computer Knowledge Quiz! 🙏\n")
time.sleep(1)
print("Answer correctly to climb the prize ladder.")
time.sleep(1)
print("A wrong answer will secure your last guaranteed amount.")
time.sleep(1)
print("\nSystem and lifelines are ready. Let's begin!\n")
time.sleep(1)

i = 0

for question in questions:
    print(f"\nQ{i+1}. {question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    time.sleep(0.5)

    print("\nChoose:")
    print("a/b/c/d ➜ Answer")
    print("Q ➜ Quit")
    print("f/s/p ➜ Lifelines (f: 50-50 / s: Skip / p: Audience Poll)")

    choice = input("Your choice: ").lower()

    # ----------Quit----------
    if choice == "q":
        final_amount = prize_money[i-1] if i > 0 else 0
        print(f"\nYou have chosen to quit. Your final winnings are: Rs{final_amount}")
        break

    # ----------Lifelines----------
    if choice in ["f","s","p"]:
        if choice == "f" and lifelines["50-50"]:
            lifelines["50-50"] = False
            options_to_show = fifty_fifty(question)
            print("50-50 Options:")
            for o in options_to_show:
                letter = chr(96 + o)  # 1->a, 2->b, etc
                print(f"{letter}. {question[o]}")
            valid_answers = [chr(96+o) for o in options_to_show]
            choice = input("Choose your answer: ").lower()
            while choice not in valid_answers:
                print("Please choose only between the displayed options!")
                choice = input("Your answer: ").lower()

        elif choice == "s" and lifelines["skip"]:
            lifelines["skip"] = False
            print("This question is skipped. Moving to the next one.")
            i += 1
            continue

        elif choice == "p" and lifelines["audience poll"]:
            lifelines["audience poll"] = False
            poll = audiencePoll(question[5])
            print("Audience Poll Results:")
            for k in poll:
                letter = chr(96+k)
                print(f"{letter}: {poll[k]}%")
            choice = input("Choose your answer: ").lower()

        else:
            print("Invalid or already used lifeline.")
            continue

    # --------Answer check----------
    letters = {'a':1,'b':2,'c':3,'d':4}
    if choice not in letters:
        print("Invalid choice. Please select a/b/c/d.")
        continue

    ans = letters[choice]

    if ans == question[5]:
        print("✅ Correct Answer! Well done.")
        print(f"You won Rs {prize_money[i]}")
        i += 1
        time.sleep(1)
    else:
        print(f"❌ Incorrect. The correct answer was option {chr(96+question[5])}.")
        print("You are receeded to secured guaranteed level")
        money = wrongAnswer(i)
        print(f"You take home Rs {money}")
        break

print("\nEnd of Quiz. Thank you for participating! 🙏")
