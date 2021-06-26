from flask import Flask, render_template

app = Flask(__name__)
import os
...
port = int(os.environ.get('PORT', 5000))
...
app.run(host='0.0.0.0', port=port, debug=True)

# Create Index Page
@app.route('/')
def index():
	first_name = "Tim"
	favorite_pizza = ["Pepperoni", "Cheese", "Supreme", "Mushroom"]
	return render_template('index.html', 
		f_name = first_name,
		favorite_pizza = favorite_pizza)

# Create About Page
@app.route('/test')
def about():
	return render_template('test.html')



