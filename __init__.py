# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from config import Config

# app = Flask(__name__)
# app.config.from_object(Config)
# app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

# from . import routes, models

# if __name__ == '__main__':
#     app.run(debug=True)





# db = SQLAlchemy()

# def create_app(config_class=Config):
#     app.config.from_object(config_class)
#     db.init_app(app)  # Using the instance to initialize with the app

#     with app.app_context():
#         from . import routes  # Import routes

#     return app



# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from config import Config

# db = SQLAlchemy()
# login_manager = LoginManager()

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#     app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

#     db.init_app(app)
#     login_manager.init_app(app)
