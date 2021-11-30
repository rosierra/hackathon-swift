from flask import Flask, render_template, request
from helpers import *

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/intro', methods=["GET", "POST"])
def intro():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        begin: str = request.form['begin']

        if fname == '':
            return render_template("intro.html")

        return render_template("one.html")
    return render_template("questions/intro.html")


@app.route('/one', methods=["GET", "POST"])
def one():
    if request.method == "POST":
        global points

        answer: str = request.form['one']

        question: str = q1(answer)

        return render_template("questions/two.html", question=question)
    return render_template("questions/one.html")


@app.route('/two', methods=["GET", "POST"])
def two():
    if request.method == "POST":
        global points

        answer: str = request.form['two']

        question: str = q2(answer)

        return render_template("questions/three.html", question=question)
    return render_template("questions/two.html")


@app.route('/three', methods=["GET", "POST"])
def three():
    if request.method == "POST":
        global points

        answer: str = request.form['three']

        question: str = q3(answer)

        return render_template("questions/four.html", question=question)
    return render_template("questions/three.html")


@app.route('/four', methods=["GET", "POST"])
def four():
    if request.method == "POST":
        global points

        answer: str = request.form['four']

        question: str = q4(answer)

        return render_template("questions/five.html", question=question)
    return render_template("questions/four.html")


@app.route('/five', methods=["GET", "POST"])
def five():
    if request.method == "POST":
        global points

        answer: str = request.form['five']

        question: str = q5(answer)

        return render_template("questions/six.html", question=question)
    return render_template("questions/five.html")


@app.route('/six', methods=["GET", "POST"])
def six():
    if request.method == "POST":
        global points

        answer: str = request.form['six']

        question: str = q6(answer)

        return render_template("questions/seven.html", question=question)
    return render_template("questions/six.html")


@app.route('/seven', methods=["GET", "POST"])
def seven():
    if request.method == "POST":
        global points

        answer: str = request.form['seven']

        question: str = q7(answer)

        return render_template("questions/eight.html", question=question)
    return render_template("questions/seven.html")


@app.route('/eight', methods=["GET", "POST"])
def eight():
    if request.method == "POST":
        global points

        answer: str = request.form['eight']

        question: str = q8(answer)

        return render_template("questions/nine.html", question=question)
    return render_template("questions/eight.html")


@app.route('/nine', methods=["GET", "POST"])
def nine():
    if request.method == "POST":
        global points

        answer: str = request.form['nine']

        question: str = q9(answer)

        return render_template("questions/ten.html", question=question)
    return render_template("questions/nine.html")


@app.route('/ten', methods=["GET", "POST"])
def ten():
    if request.method == "POST":
        global points

        answer: str = request.form['ten']

        question: str = q10(answer)

        return render_template("questions/eleven.html", question=question)
    return render_template("questions/ten.html")


@app.route('/eleven', methods=["GET", "POST"])
def eleven():
    if request.method == "POST":
        global points

        answer: str = request.form['eleven']

        question: str = q11(answer)

        return render_template("questions/twelve.html", question=question)
    return render_template("questions/eleven.html")


@app.route('/twelve', methods=["GET", "POST"])
def twelve():
    if request.method == "POST":
        global points

        answer: str = request.form['twelve']

        question: str = q12(answer)

        return render_template("questions/thirteen.html", question=question)
    return render_template("questions/twelve.html")


@app.route('/thirteen', methods=["GET", "POST"])
def thirteen():
    if request.method == "POST":
        global points

        answer: str = request.form['thirteen']

        question: str = q13(answer)

        return render_template("questions/fourteen.html", question=question)
    return render_template("questions/thirteen.html")


@app.route('/fourteen', methods=["GET", "POST"])
def fourteen():
    if request.method == "POST":
        global points

        answer: str = request.form['fourteen']

        question: str = q14(answer)

        return render_template("questions/fifteen.html", question=question)
    return render_template("questions/fourteen.html")


@app.route('/fifteen', methods=["GET", "POST"])
def fifteen():
    if request.method == "POST":
        global points

        answer: str = request.form['fifteen']
        album: str = all_results()

        question: str = q15(answer)

        return render_template("result.html", album=album)
    return render_template("questions/fifteen.html")


@app.route('/result', methods=["GET", "POST"])
def result():
    album: str = all_results()
    if request.method == "POST":
        return render_template('index.html')
    return render_template('result.html', album=album)


if __name__ == '__main__':
    app.run(debug=True)