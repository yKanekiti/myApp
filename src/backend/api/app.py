import sys

sys.path.append("/src/backend/")

from flask import Flask, render_template
from node_list import node_router
from common.database import init_db
from main import main
import time


app = init_db()
app.register_blueprint(node_router)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/learn')
def learn():
    main()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
