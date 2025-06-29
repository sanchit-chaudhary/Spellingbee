"""
WSGI entry point for Spelling Bee Adventure Game
This file is required for proper Flask deployment on Replit
"""

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)