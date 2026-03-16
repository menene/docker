import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "/data/teams.db"


def query(sql, params=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/teams")
def get_teams():
    return query("SELECT * FROM teams ORDER BY name")


@app.get("/teams/{team_id}")
def get_team(team_id: int):
    results = query("SELECT * FROM teams WHERE id = ?", (team_id,))
    return results[0] if results else {}
