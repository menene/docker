import sqlite3

DB_PATH = '/data/teams.db'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name     TEXT NOT NULL,
        city     TEXT NOT NULL,
        stadium  TEXT NOT NULL,
        founded  INTEGER NOT NULL
    )
''')

teams = [
    ('Real Madrid',         'Madrid',        'Santiago Bernabéu',         1902),
    ('FC Barcelona',        'Barcelona',      'Spotify Camp Nou',          1899),
    ('Atlético de Madrid',  'Madrid',        'Cívitas Metropolitano',     1903),
    ('Sevilla FC',          'Sevilla',        'Ramón Sánchez-Pizjuán',    1890),
    ('Real Betis',          'Sevilla',        'Benito Villamarín',         1907),
    ('Valencia CF',         'Valencia',       'Mestalla',                  1919),
    ('Athletic Club',       'Bilbao',         'San Mamés',                 1898),
    ('Real Sociedad',       'San Sebastián',  'Reale Arena',               1909),
    ('Villarreal CF',       'Villarreal',     'Estadio de la Cerámica',   1923),
    ('Getafe CF',           'Getafe',         'Coliseum Alfonso Pérez',    1983),
    ('Rayo Vallecano',      'Madrid',         'Estadio de Vallecas',       1924),
    ('Celta de Vigo',       'Vigo',           'Abanca-Balaídos',           1923),
    ('RCD Mallorca',        'Palma',          'Visit Mallorca Estadi',     1916),
    ('UD Las Palmas',       'Las Palmas',     'Estadio Gran Canaria',      1949),
    ('Real Valladolid',     'Valladolid',     'José Zorrilla',             1928),
    ('Espanyol',            'Barcelona',      'RCDE Stadium',              1900),
    ('Osasuna',             'Pamplona',       'El Sadar',                  1920),
    ('Alavés',              'Vitoria-Gasteiz','Mendizorroza',              1921),
    ('Leganés',             'Leganés',        'Estadio Municipal de Butarque', 1928),
    ('Real Zaragoza',       'Zaragoza',       'La Romareda',               1932),
]

c.executemany(
    'INSERT OR IGNORE INTO teams (name, city, stadium, founded) VALUES (?, ?, ?, ?)',
    teams
)

conn.commit()
conn.close()
print(f"Seeded {len(teams)} teams into {DB_PATH}")
