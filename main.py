from __init__ import app
import seed_database as sd

if __name__ == "__main__":
    with app.app_context():
        sd.seed_database()
    app.run(debug=True)
