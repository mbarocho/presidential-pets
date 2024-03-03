from dataclasses import dataclass
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='pages');

@dataclass
class Pet:
    name: str
    age: int
    is_in_cat_party: bool
    income: float
    address: str

@dataclass
class Question:
    def __init__(self, answer):
        self.answer = answer


# Runs on webpage startup
@app.route('/')
def index():
    return render_template('slide-1.html')

# Brute force navigation between pages

@app.route('/page-2')
def page_2():
    return render_template('slide-2.html')

@app.route('/page-3')
def page_3():
    return render_template('slide-3.html')

@app.route('/page-4')
def page_4():
    return render_template('slide-4.html')

@app.route('/page-5')
def page_5():
    return render_template('slide-5.html')

@app.route('/page-6')
def page_6():
    return render_template('slide-6.html')

@app.route('/page-7')
def page_7():
    return render_template('slide-7.html')

@app.route('/page-8')
def page_8():
    return render_template('slide-8.html')

@app.route('/page-9')
def page_9():
    return render_template('slide-9.html')

@app.route('/page-10')
def page_10():
    return render_template('slide-10.html')

@app.route('/page-11')

def page_11():
    # Use link "http://localhost:5000/?reset_score=1" for score reset for now
    Mabel = Pet("Mabel", 73, True, 72902.43, "45 Meow Way")
    return render_template('slide-11.html', mabel=Mabel)

@app.route('/page-12')
def page_12():
    return render_template('slide-12.html')

@app.route('/page-13')
def page_13():
    return render_template('slide-13.html')

@app.route('/page-14')
def page_14():
    return render_template('slide-14.html')

@app.route('/page-15')
def page_15():
    return render_template('slide-15.html')

@app.route('/page-16')
def page_16():
    return render_template('slide-16.html')

@app.route('/page-17')
def page_17():
    return render_template('slide-17.html')

score = 0

# Sample Questions
questions = [
    Question('name="Mabel"'),
]

progress = 0

@app.before_request
def reset_score():
    global score
    # Reset the score on each page reload
    if request.endpoint and request.endpoint != 'static':
        score = 0

# Runs on webpage startup
@app.route('/')


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
        feedback = "Not quite, try again!"

    if progress < len(questions):
        next_question = questions[progress]
        return jsonify({"feedback": feedback, "score": score, "question": next_question.text})
    else:
        return jsonify({"feedback": feedback, "score": score})

# App Initiation
if __name__ == '__main__':
    app.run(debug=True)