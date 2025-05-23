from flask import Flask, render_template_string, request, redirect, jsonify
import os

app = Flask(__name__)

LOG_FILE = 'server.log'


@app.route('/')
def index():
    return render_template_string("""
    <html>
      <head><title>Welcome</title></head>
      <body style="font-family: Arial, sans-serif; background-color: #f0f4f8; text-align: center; padding-top: 100px;">
        <h1 style="color: #2c3e50;">Welcome!</h1>
        <a href="/logs"><button style="padding: 10px 20px; font-size: 16px; background-color: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer;">View Logs</button></a>
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

    return render_template_string("""
    <html>
      <head><title>Server Logs</title></head>
      <body style="font-family: monospace; background-color: #1e1e1e; color: #dcdcdc; padding: 20px;">
        <h2 style="color: #00bcd4;">Server Logs (last 100 lines)</h2>
        <form method="post" style="margin-bottom: 10px;">
          <button type="submit" id="clearBtn" style="padding: 8px 16px; background-color: #e74c3c; color: white; border: none; border-radius: 4px; cursor: pointer;">Clear Logs</button>
        </form>
        <pre id="logOutput" style="background-color: #2d2d2d; padding: 15px; border-radius: 6px; overflow-x: auto;"></pre>

        <script>
          function fetchLogs() {
            fetch('/get_logs')
              .then(response => response.json())
              .then(data => {
                document.getElementById('logOutput').innerHTML = data.logs.map(line => {
                  if (line.includes("ERROR")) {
                    return '<span style="color:red; font-weight:bold;">' + line + '</span>';
                  } else if (line.includes("WARNING")) {
                    return '<span style="color:orange; font-weight:bold;">' + line + '</span>';
                  } else if (line.includes("INFO")) {
                    return '<span style="color:green;">' + line + '</span>';
                  } else {
                    return line;
                  }
                }).join('<br>');
              });
          }

          // Load logs immediately, then every 3 seconds
          fetchLogs();
          setInterval(fetchLogs, 3000);
        </script>
      </body>
    </html>
    """)


@app.route('/get_logs')
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify(logs=[])

    with open(LOG_FILE, 'r') as f:
        logs = f.readlines()

    return jsonify(logs=[line.rstrip('\n') for line in logs[-100:]])


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
