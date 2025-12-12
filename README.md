🎯 Computer Knowledge Quiz Game (KBC Style)
-----------📌 Project Overview------------

This project is a console-based quiz game inspired by Kaun Banega Crorepati (KBC), developed using Python.
The game tests basic Computer, Java, and Python knowledge, offering prize money, guaranteed levels, lifelines, and quit options.

--------------🎮 Game Features----------------

✅ Multiple-choice questions (MCQs)

✅ Prize money increases with each correct answer

✅ Guaranteed money levels (Safe checkpoints)

✅ Quit option at any point

✅ Lifelines:

f->50-50

s->Skip Question

p->Audience Poll

✅ Wrong answer penalty with secured amount

✅ KBC-style dramatic flow

-----------🛠 Technologies Used------------

Language: Python 3

Libraries: random

----------Concepts Used:--------------

Lists & Dictionaries

Functions

Loops & Conditionals

User Input Handling

--------------🧩 Question Structure---------------

Each question follows this format:

["Question", "Option1", "Option2", "Option3", "Option4", correct_option_number]

-----------💰 Prize Money Structure--------------

Prize money increases level-wise

Guaranteed levels ensure minimum winnings even after a wrong answer

Example:

Guaranteed Levels:
Q5  ➜ ₹10,000
Q9  ➜ ₹1,60,000
Q13 ➜ ₹25,00,000

--------------🆘 Lifelines Rules-----------------

Each lifeline can be used only once

50-50 removes two incorrect options

Skip lifeline skips the question

Audience poll shows percentage-based hints

---------------❌ Wrong Answer Rule--------------

If the player answers incorrectly:

Game ends immediately

Player receives the last secured guaranteed amount

---------------------🚪 Quit Rule-----------------

Player can quit anytime

Winnings = prize money of last correctly answered question

----------------▶️ How to Run----------------

Install Python 3

Save the file as quiz_game.py

Run using:

python quiz_game.py

-----------📈 Future Enhancements-------------

Timer-based questions

GUI version (Tkinter / PyQt)

Difficulty levels

Player score leaderboard

------------✅ Conclusion------------

This project demonstrates strong fundamentals of Python programming and logical flow design.
