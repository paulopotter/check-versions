import os

import yaml
from flask import Flask, render_template  # NOQA
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
cache = SimpleCache()


def get_settings():
    with open('settings.yaml', 'r') as file:
        settings = yaml.load(file)

    return settings


@app.route("/")
def index():
    settings = cache.get("settings")
    return render_template('index.html', project_name=settings['PROJECT']['NAME'])


@app.route("/project")
def project():
    settings = cache.get("settings")
    return render_template('index.html', project_name=settings['PROJECT']['NAME'])


if __name__ == "__main__":
    PORT = os.getenv('PORT', 5001)
    cache.set("settings", get_settings())
    app.run(port=int(PORT), host='0.0.0.0', debug=True)
