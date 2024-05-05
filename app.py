from flask import Flask, request, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from forms import UserLoginForm
from flask_wtf import CSRFProtect


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = ']apokf;a;sr9324i'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)