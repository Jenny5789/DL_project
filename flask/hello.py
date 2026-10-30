from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return render_template('hello.html', name=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)