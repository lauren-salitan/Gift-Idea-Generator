from flask import render_template, redirect, url_for, flash, request, jsonify, current_app, Flask, session, g
from models import User, RecipientProfile, connect_db, db
from forms import LoginForm, RegistrationForm, RecipientProfileForm
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from utils import generate_gift_ideas
import os

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

login_manager=LoginManager()
login_manager.init_app(app)

with app.app_context():
    connect_db(app)
    db.create_all()

# @login_manager.user_loader()
# def load_user(self, user_id):
#     return User.query.get(int(user_id))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""
#     if current_user in session:
#         g.user = User.query.get(session[current_user])
#     else:
#         g.user = None

# def do_login(user):
#     """Log in user."""
#     session[current_user] = user.id
#     login_user(user)
#     return redirect("/")

# def do_logout():
#     """Log out user."""
#     if current_user in session:
#         del session[current_user]
#     logout_user()


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    """Log in user."""
    session[CURR_USER_KEY] = user.id
    login_user(user)
    return redirect("/")

def do_logout():
    """Log out user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    logout_user()

# @app.route('/logout')
# def logout():
#     """Handle logout of user."""
#     do_logout()
#     flash('You have successfully logged out.', 'success')
#     return redirect(url_for('login'))


@app.route('/')
#@login_required
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

@app.route('/logout')
def logout():
    do_logout()
    flash('You have successfully logged out.', 'success')
    return redirect(url_for('login'))

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
        try:
            db.session.add(profile)
            db.session.commit()
            return redirect(url_for('search'))
        except Exception as e:
            print("Failed to add profile:", e)
            db.session.rollback()
    
    profile = RecipientProfile() 
    return render_template('profile.html', form=form, profile=profile)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    profiles = current_user.recipient_profiles.all()
    return render_template('search.html', profiles=profiles)

@app.route('/view_profiles')
@login_required
def view_profiles():
    profiles = RecipientProfile.query.filter_by(user_id=current_user.id).all()
    return render_template('view_profiles.html', profiles=profiles)


# @app.route('/generate_ideas', methods=['POST'])
# @login_required
# def generate_ideas():
#     profile_id = request.form.get('profile_id')
#     profile = RecipientProfile.query.get_or_404(profile_id)
    
#     if profile.user_id != current_user.id:
#         return jsonify({'error': 'Unauthorized'}), 403

#     description = f"Generate gift ideas for a {profile.occasion.lower()} for someone interested in {profile.interests.lower()}."
#     ideas = generate_gift_ideas(description, current_app.config['OPENAI_API_KEY'])
    
#     if ideas:
#         return jsonify({'ideas': ideas})
#     else:
#         return jsonify({'error': 'Failed to generate ideas'}), 500

@app.route('/generate_ideas', methods=['POST'])
@login_required
def generate_ideas():
    profile_id = request.form.get('profile')
    profile = RecipientProfile.query.get_or_404(profile_id)
    
    if profile.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    description = f"Generate gift ideas for a {profile.occasion.lower()} for someone interested in {profile.interests.lower()}."
    ideas = generate_gift_ideas(description, OPENAI_API_KEY)
    
    print('********************')
    print(ideas)

    if ideas:
        return jsonify({'ideas': ideas})
    else:
        return jsonify({'error': 'Failed to generate ideas'}), 500

