print(">>> RUN.PY STARTED <<<")

from app import app  # Import app from __init__.py

if __name__ == '__main__':
    print(">>> FLASK APP RUNNING <<<")
    app.run(debug=True, host='0.0.0.0', port=5000)  # Explicitly set host and port

