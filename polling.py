from dataclasses import dataclass
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='pages');

@dataclass
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

score = 0

# Sample Questions
questions = [
    Question("What is the constituent's name? Please format your answer as a Python string variable.", 'name="Oliver"'),
    Question("What is this candidate's platform? You may answer this in plain text.", "The Best")
]

progress = 0

@dataclass
class Pet:
    name: str
    age: int
    animal: str
    Description: str

@app.before_request
def reset_score():
    global score
    # Reset the score on each page reload
    if request.endpoint and request.endpoint != 'static':
        score = 0

# Runs on webpage startup
@app.route('/')
def index():
    global score, progress
    # Use link "http://localhost:5000/?reset_score=1" for score reset for now
    if 'reset_score' in request.args:
        score = 0
    Oliver = Pet("Oliver", 10, "Cat", "The Best")
    if progress < len(questions):
        current_question = questions[progress]
        return render_template('index.html', oliver=Oliver, score=score, question=current_question)


# Runs when user submits an answer
@app.route('/submit', methods=['POST'])
def submit():
    global score, progress
    candidate = Pet("Oliver", 10, "Cat", "The Best")
    user_guess = request.form['user_guess']
    current_question = questions[progress]
    # Do something with candidate_name
    if (user_guess == current_question.answer):
        feedback = "That's right!"
        score += 1
        progress += 1
    else:
        feedback = "Not Quite."

    if progress < len(questions):
        next_question = questions[progress]
        return jsonify({"feedback": feedback, "score": score, "question": next_question.text})
    else:
        return jsonify({"feedback": feedback, "score": score})

    
    # Return feedback as JSON
    # return jsonify({"feedback": feedback, "score": score})



if __name__ == '__main__':
    app.run(debug=True)