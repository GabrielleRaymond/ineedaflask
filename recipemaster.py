from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/recipes/')
def recipe_list():
  return 'list goes here'

#@app.route('/recipes/<recipe>')
@app.route('/recipes/recipe')
def display_recipe():
  #return 'Recipe %d', recipe
  return render_template('recipes/recipe.html')

if __name__ == '__main__':
  app.run()
