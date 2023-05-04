from flask import Flask, render_template #added render_template!

app = Flask(__name__)

@app.route('/')
def index():
    # Instead of returning a string,
    # we'll return the result of the render_template method, passing in the same of our HTML file
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)