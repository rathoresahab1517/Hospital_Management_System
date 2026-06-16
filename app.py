from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)


@app.route('/')
def logi():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def logi():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            if user.role == 'admin':
                return render_template('addash.html')
            elif user.role == 'doctor':
                return render_template('drdash.html')
            elif user.role == 'patient':
                return render_template('ptdash.html')
        flash('Invalid username or password.', 'error')
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        phone = request.form.get('phone')

        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('register.html')
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return render_template('register.html')

        user = User(username=username, email=email, name=name, phone=phone, role='patient')
        # user.set_password(password)
        # db.session.add(user)
        # db.session.commit()

        patient = Patient(user_id=user.id)
        # db.session.add(patient)
        # db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return render_template('login.html')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
