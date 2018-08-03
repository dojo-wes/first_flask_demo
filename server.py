from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
  list_of_dicts = [
    {
      'favorite_fruit': "mango",
      'favorite_language': "Python",
      'favorite_artist': "Vanilla Ice"
    },
    {
      'favorite_fruit': "apple",
      'favorite_language': "JavaScript",
      'favorite_artist': "Enya"
    },
    {
      'favorite_fruit': "banana",
      'favorite_language': "CSharp",
      'favorite_artist': "Limp Bizkit"
    },
  ]
  return render_template('index.html', title="Home", jinj_list=list_of_dicts)

@app.route('/other')
def other():
  return render_template('other.html')

@app.route('/process_form', methods=['POST'])
def process():
  print "*" * 80
  print request.form['favorite_artist'], request.form['favorite_fruit']
  return redirect('/')

app.run(debug=True)