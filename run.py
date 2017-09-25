import os

from app import app, initialize_app

application = app

if __name__ == '__main__':
    initialize_app(app)
    PORT = os.environ.get('PORT')
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=PORT or 5000);