from flask import Flask, render_template

# app object
app=Flask(__name__)

# url rout decorator: home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Dashboard/')
def dash():
    return render_template('dash.html')

if __name__ == "__main__":
    app.run(debug=True)
