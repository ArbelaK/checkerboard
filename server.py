from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:num>/<int:num2>/<string:color>/<string:color2>')
def cheeckerboard4(num, num2, color, color2):
    return render_template('index.html', num=num, num2=num2, color=color, color2=color2)


if __name__=="__main__":
    app.run(debug=True)