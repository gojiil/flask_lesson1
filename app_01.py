from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category')
def category():
    return render_template('category.html', category_name='Одежда')

@app.route('/product')
def product():
    return render_template('product.html', product_name='Куртка')

if __name__ == '__main__':
    app.run(debug=True)
