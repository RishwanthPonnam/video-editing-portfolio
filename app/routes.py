from flask import render_template, request, redirect, url_for, flash
from app import app  # Import app from __init__.py

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        print(f"Message from {name} ({email}) - {subject}: {message}")
        flash("Thanks for contacting us! We'll get back to you soon.", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

