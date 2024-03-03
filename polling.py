from dataclasses import dataclass
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='pages');

@dataclass
class Pet:
    name: str
    age: int
    animal: str
    Description: str

score = 0

@app.route('/')
def index():
    Oliver = Pet("Oliver", 10, "Cat", "The Best")
    Lucy = Pet("Lucy", 13, "Cat", "A loyal and caring gray cat!")
    return render_template('index-test.html', oliver=Oliver, lucy=Lucy, score=score)

@app.route('/submit', methods=['POST'])
def submit():
    candidate = Pet("Oliver", 10, "Cat", "The Best")
    user_guess = request.form['user_guess']
    # Do something with candidate_name
    if (user_guess == ('name="' + candidate.name + '"')):
        feedback = "That's right!"
    else:
        feedback = "Not Quite."
    
    # Return feedback as JSON
    return jsonify({"feedback": feedback})



if __name__ == '__main__':
    app.run(debug=True)