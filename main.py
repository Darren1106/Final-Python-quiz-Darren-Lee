import tkinter as tk
from tkinter import messagebox
questions = [
    {
        "question": "What is Python?",
        "options": ["Programming language", "Food", "Snake"],
        "correct_answer": "Programming language",
        "attempts": 3
    },
    {
        "question": "What is the command to print out a message in Python?",
        "options": ["Print", "Execute", "Command"],
        "correct_answer": "Print",
        "attempts": 3
    },
    {
      "question": "How do you execute the same chunk of code over and over?",
      "options": ["Over", "For loops", "Repeat"],
      "correct_answer": "For loops",
      "attempts": 3
    },
    {
    "question": "How do you define a function in python?",
    "options": ["funtion", "f define", "def"],
    "correct_answer": "def",
    "attempts": 3
    },
    {
    "question": "What does a boolean represent?",
    "options": ["True or False", "Balloons", "Scores"],
    "correct_answer": "True or False",
    "attempts": 3
    },
    {
      "question": "In order to make everything lowercase in Pythin what command would be used?",
      "options": [".lowerall()", ".lower()", ".alllowercase()"],
      "correct_answer": ".lower()",
      "attempts": 3
    },
    {
      "question": "Which of the following is an int?",
      "options": ["numbers", "6", "3.14159"],
      "correct_answer": "6",
      "attempts": 3
    },
    {
      "question": "What can appear as the highest number from 'random.randint(6,50)'?",
      "options": ["49", "0", "50"],
      "correct_answer": "50",
      "attempts": 3
    },
    {
    "question": "In order to create a comment in python what symbol should be used?",
    "options": ["#", "/comment", "*"],
    "correct_answer": "#",
    "attempts": 3
    },
    {
    "question": "Which of the following is true?",
    "options": ["'if' is not a command in python", "This quiz was made using scratch", "You have 3 attempts to answer this question"],
    "correct_answer": "You have 3 attempts to answer this question",
    "attempts": 3
    }
]
# Time limit for question
time_limit = 30000  # Remember that the timer will be in milliseconds
current_question = 0
score = 0
remaining_attempts = 0
quiz_window = None
timer = None
var = None
def check_answer():
    global current_question, score, remaining_attempts
    selected_option = var.get()
    if selected_option == questions[current_question]["correct_answer"]:
        score += 1
        current_question += 1
        if current_question < len(questions):
            remaining_attempts = questions[current_question]["attempts"]
            display_question()
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {score}/{len(questions)}!")
            quiz_window.destroy()
    else:
        remaining_attempts -= 1
        if remaining_attempts > 0:
            messagebox.showinfo("Incorrect answer", f"Wrong answer! You have {remaining_attempts} attempts remaining.")
        else:
            messagebox.showinfo("Incorrect answer", "Game Over!")
            current_question += 1
            remaining_attempts = 0  # Reset remaining attempts
            if current_question < len(questions):
                restart_quiz()  # Call restart_quiz() function when user runs out of attempts
            else:
                messagebox.showinfo("Quiz Complete", f"You scored {score}/{len(questions)}!")
                quiz_window.destroy()
def display_question():
  question_label_text = f"{questions[current_question]['question']} (Timer: {time_limit/1000} seconds)"
  question_label.config(text=question_label_text)
  for i, option in enumerate(questions[current_question]["options"]):
      option_radio_buttons[i].config(text=option, value=option)
  var.set(None)  # Reset the selected option
  # Start the timer using after
  global timer
  timer = quiz_window.after(time_limit, times_up)
def times_up():
    messagebox.showinfo("Time's Up!", "Time ran out for the question.")
    current_question += 1
    remaining_attempts = 0  # Reset remaining attempts
    if current_question < len(questions):
        restart_quiz()  # Call restart_quiz() function when time runs out for a question
    else:
        messagebox.showinfo("Quiz Complete", f"You scored {score}/{len(questions)}!")
        quiz_window.destroy()
def start_quiz():
    global quiz_window, var, remaining_attempts
    start_window.destroy()
    quiz_window = tk.Tk()
    quiz_window.title("Timed Quiz")
    global question_label, option_radio_buttons
    question_label = tk.Label(quiz_window, text="", padx=10, pady=10)
    question_label.pack()
    var = tk.StringVar()
    option_radio_buttons = []
    for i in range(len(questions[0]["options"])):
        option_radio_buttons.append(tk.Radiobutton(quiz_window, text="", variable=var))
        option_radio_buttons[i].pack()
    submit_button = tk.Button(quiz_window, text="Answer", command=check_answer)
    submit_button.pack()
    remaining_attempts = questions[current_question]["attempts"]
    display_question()
def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0
    display_question()
# Create the starting window
start_window = tk.Tk()
start_window.title("Start Python Quiz")
start_label = tk.Label(start_window, text="Press play!")
start_label.pack()
start_button = tk.Button(start_window, text="Play", command=start_quiz)
start_button.pack()
# Start the Tkinter main loop for the starting window
start_window.mainloop()