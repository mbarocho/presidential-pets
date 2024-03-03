from dataclasses import dataclass
from flask import Flask, render_template

app = Flask(__name__, template_folder='pages');

@dataclass
class Pet:
    name: str
    age: int
    animal: str
    platform: str

@app.route('/')

def index():
    Ada = Pet("Ada", 5, "Dog", "A hardworking corgi who studies Computer Science!")
    Lucy = Pet("Lucy", 13, "Cat", "A loyal and caring gray cat!")
    return render_template('test.html', ada=Ada, lucy=Lucy)

if __name__ == '__main__':
    app.run(debug=True)
    