from flask import Flask, render_template

app = Flask(__name__)


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

if __name__ == "__main__":
	app.run()

 

