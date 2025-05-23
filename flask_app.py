from flask import Flask, render_template_string, request, redirect
import os

app = Flask(__name__)

LOG_FILE = 'server.log'


@app.route('/')
def index():
    return render_template_string("""
    <html>
      <head><title>Welcome</title></head>
      <body>
        <h1>Welcome!</h1>
        <a href="/logs"><button>View Logs</button></a>
      </body>
    </html>
    """)


@app.route('/logs', methods=['GET', 'POST'])
def show_logs():
    if request.method == 'POST':
        with open(LOG_FILE, 'w'):
            pass
        return redirect('/logs')

    if not os.path.exists(LOG_FILE):
        return "Log file not found."

    with open(LOG_FILE, 'r') as f:
        logs = f.readlines()

    return render_template_string("""
    <html>
      <head><title>Server Logs</title></head>
      <body>
        <form method="post">
          <button type="submit">Clear Logs</button>
        </form>
        <h2>Server Logs (last 100 lines)</h2>
        <pre>{{ logs }}</pre>
      </body>
    </html>
    """, logs='\n'.join(logs[-100:]))


if __name__ == '__main__':
    app.run(debug=True)
