from flask import Flask, render_template
import csv
import os
import sqlite3

app = Flask(__name__)

os.chdir(r'C:\Users\jukil\Documents\PU21H\Arbete som programutvecklare\flask-app')

# Set the filename and columns to read
filename = 'ostolaskudata-2021-porvoon-kaupunki.csv'
columns_to_read = ['Kustannuspaikka', 'Kustannuspaikan nimi', 'EUR, brutto']

# Open the CSV file and create a reader object
with open(filename, 'r', newline='', encoding='latin-1') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS data_table
                 (id INTEGER PRIMARY KEY, kp_id TEXT, kp_nimi TEXT, euro_brutto REAL)''')

    for row in reader:
        values = []
        for col in columns_to_read:
            try:
                values.append(row[col])
            except KeyError:
                print(f"KeyError: Column {col} not found in row {row}")
        c.execute(
            "INSERT INTO data_table (kp_id, kp_nimi, euro_brutto) VALUES (?, ?, ?)", values)

    c.execute('''SELECT kp_id, kp_nimi, SUM(euro_brutto) AS total_euro_brutto
                FROM data_table
                GROUP BY kp_id, kp_nimi''')

c.execute('''SELECT kp_id, kp_nimi, SUM(euro_brutto) AS total_euro_brutto
              FROM data_table
              GROUP BY kp_id, kp_nimi
              ORDER BY total_euro_brutto DESC
              LIMIT 5''')

data = c.fetchall()  # saves the query above into an array named "data"

print(data)

conn.commit()


@app.route("/")
def home():

    labels = [row[1] for row in data]
    values = [row[2] for row in data]
    labels = []
    values = []
    for row in data:
        labels.append(row[1])
        values.append(row[2])
    # return data
    return render_template("graph.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
