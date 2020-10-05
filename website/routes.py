from website import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title='Reviews')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/services')
def services():
    return render_template('services.html', title='Services')


if __name__ == '__main__':
    app.run(debug=True)
