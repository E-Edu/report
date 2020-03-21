from flask import Flask, jsonify
from report.ticket import main_page

app = Flask(__name__)
app.register_blueprint(main_page)

@app.errorhandler(404)
def handle_404_error(e):
    return {'error':'Page not found'},404

@app.errorhandler(405)
def handle_405_error(e):
    return jsonify({'error':'Method not allowed'}),404

if __name__ == '__main__':
    app.run(debug=True)