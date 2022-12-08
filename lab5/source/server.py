#!/usr/bin/env python3
from flask import Flask



app = Flask(__name__)
# --- main ---
if __name__ == '__main__':
    PORT = 4080

    print(f'Starting: http://localhost:{PORT}')
    app.run(debug=False, host='0.0.0.0', port=PORT)