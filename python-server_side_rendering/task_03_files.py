#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_data(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return [dict(row, id=int(row["id"]), price=float(row["price"])) for row in reader]

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    products = []
    error = None

    if source == 'json':
        products = read_json_data('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if id_param:
        try:
            product_id = int(id_param)
            product = next((item for item in products if item['id'] == product_id), None)
            if product:
                products = [product]
            else:
                error = "Product not found"
                products = []
        except ValueError:
            error = "Invalid ID format"
            products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
