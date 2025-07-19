#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_from_json(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def load_from_csv(filename='products.csv'):
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        return []
    return products

def load_from_sqlite(db_path='products.db'):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        for row in cursor.fetchall():
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error:
        return []
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')
    id_str = request.args.get('id', None)

    if source == 'json':
        products = load_from_json()
    elif source == 'csv':
        products = load_from_csv()
    elif source == 'sql':
        products = load_from_sqlite()
    else:
        return render_template('product_display.html', products=None, error="Wrong source")

    if not products:
        return render_template('product_display.html', products=None, error="Failed to load data")

    if id_str:
        try:
            product_id = int(id_str)
            products = [p for p in products if p['id'] == product_id]
        except ValueError:
            products = []

        if not products:
            return render_template('product_display.html', products=None, error="Product not found")

    return render_template('product_display.html', products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True)
