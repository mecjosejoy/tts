from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>File System</title>
  </head>
  <body>
    <div class="container">
      <h1>File System</h1>
      <ul>
        {% for item in items %}
          <li>
            {% if item.is_dir %}
              <a href="/browse/{{ item.name }}">{{ item.name }}/</a>
            {% else %}
              <a href="/download/{{ item.name }}">{{ item.name }}</a>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  </body>
</html>
'''

@app.route('/')
@app.route('/browse/<path:subpath>')
def browse(subpath=''):
    directory = os.path.join(os.getcwd(), subpath)
    items = [{'name': name, 'is_dir': os.path.isdir(os.path.join(directory, name))} for name in os.listdir(directory)]
    return render_template_string(TEMPLATE, items=items)

@app.route('/download/<path:filename>')
def download(filename):
    directory = os.getcwd()
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
