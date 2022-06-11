
from ast import Num
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)






@app.route('/play/<int:num>')
def level_one(num):
    return render_template("index.html",num=num)	# notice the 2 new named arguments!


@app.route('/play/<int:num>/<string:color>')
def level_two(num,color):
    return render_template("index.html",num=num, color=color)	# notice the 2 new named arguments!


if __name__=="__main__":
    app.run(debug=True)

