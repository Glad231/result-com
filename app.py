from flask import Flask, render_template, request

app = Flask(__name__, template_folder='project/templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    __name__ = request.args.get('__name__', 'Гость')
    
    return render_template('result.html', name=name)
    
if __name__.lower() == "глеб":
    message = "Ты лучший 💀🔥"
else:
    message = f"Привет, {__name__} ❤️"

if __name__ == '__main__':
    app.run(debug=True)
