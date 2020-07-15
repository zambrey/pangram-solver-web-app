from flask import Flask, request, render_template
from pangramsolver import pangramgame
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    letters = request.args.get('letters')
    required = request.args.get('required')

    if letters:
        return solutionpage(letters, required)
    else:
        return homepage()


def homepage():
    return render_template('home.html')


def solutionpage(letters, required):
    game = pangramgame(list(letters), list(
        required if required else ""), (4, 10))
    words = game.solve()
    # return massagewordslist(words, letters))
    return render_template('solution.html', words=massagewordslist(words, set(letters)))


def massagewordslist(words, letters):
    words.sort(key=lambda word: (-len(word), word))
    d = {}
    for word in words:
        d.setdefault(len(word), []).append(
            (word, len(set(word)) == len(letters)))
    return d
