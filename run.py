from market import app
from market import create_app
# from market import db
# with app.app_context():
#     db.create_all()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


