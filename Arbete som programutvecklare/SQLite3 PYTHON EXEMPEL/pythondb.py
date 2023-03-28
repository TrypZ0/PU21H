import sqlite3

# Skapa en databasanslutning och en cursor
conn = sqlite3.connect('exempeldatabas.db')
c = conn.cursor()

# Skapa en tabell med namnet Användare
c.execute('''CREATE TABLE Användare
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Namn TEXT,
              Ålder INTEGER,
              Email TEXT,
              Skapad DATE)''')

# Lägg till en ny användare i tabellen
c.execute("INSERT INTO Användare (Namn, Ålder, Email, Skapad) VALUES (?, ?, ?, ?)", ('Anna', 25, 'anna@example.com', '2023-03-27'))
conn.commit()

# Hämta alla kolumner för alla användare i tabellen och skriv ut dem på skärmen
c.execute("SELECT * FROM Användare")
rows = c.fetchall()
for row in rows:
    print(row)

# Stäng databasanslutningen
conn.close()
