from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    name = request.args.get('name', 'Гость')
    return render_template('result.html', name=name)
    
    return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
