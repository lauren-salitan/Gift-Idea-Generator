from flask import render_template, redirect, url_for, flash, request, jsonify, current_app
from app import app, db
from models import User, RecipientProfile
from forms import LoginForm, RegistrationForm, RecipientProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from utils import generate_gift_ideas

@app.route('/')
@login_required
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)
        if user:
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# @app.route('/create_profile', methods=['GET', 'POST'])
# @login_required
# def create_profile():
#     form = RecipientProfileForm()
#     if form.validate_on_submit():
#         profile = RecipientProfile(
#             name=form.name.data,
#             birthday=form.birthday.data,
#             gender=form.gender.data,
#             relationship=form.relationship.data,
#             interests=form.interests.data,
#             occasion=form.occasion.data,
#             budget=form.budget.data,
#             additional_details=form.additional_details.data,
#             author=current_user
#         )
#         db.session.add(profile)
#         db.session.commit()
#         return redirect(url_for('dashboard'))
#     else:
#         print(form.errors) 
#     return render_template('profile.html', form=form)
@app.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():
    form = RecipientProfileForm()
    if form.validate_on_submit():
        profile = RecipientProfile(
            name=form.name.data,
            birthday=form.birthday.data,
            gender=form.gender.data,
            relationship=form.relationship.data,
            interests=form.interests.data,
            occasion=form.occasion.data,
            budget=form.budget.data,
            additional_details=form.additional_details.data,
            author=current_user
        )
        db.session.add(profile)
        db.session.commit()
        flash('Profile created successfully!')
        return redirect(url_for('dashboard'))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                flash(f'{fieldName}: {err}')
        return render_template('profile.html', form=form, profile=RecipientProfile())

    

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    profiles = current_user.recipient_profiles.all()
    if request.method == 'POST':
        profile_id = request.form['profile']
        profile = RecipientProfile.query.filter_by(id=profile_id).first_or_404()
        return redirect(url_for('dashboard'))
    return render_template('search.html', profiles=profiles)

@app.route('/generate_ideas', methods=['POST'])
@login_required
def generate_ideas():
    profile_id = request.form.get('profile_id')
    profile = RecipientProfile.query.get_or_404(profile_id)
    
    if profile.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    description = f"Generate gift ideas for a {profile.occasion.lower()} for someone interested in {profile.interests.lower()}."
    ideas = generate_gift_ideas(description, current_app.config['OPENAI_API_KEY'])
    
    if ideas:
        return jsonify({'ideas': ideas})
    else:
        return jsonify({'error': 'Failed to generate ideas'}), 500
