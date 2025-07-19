from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
