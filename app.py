from report import app
from report import db

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    db.create_all()
