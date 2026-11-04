import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=None)

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "secret"),
        dbname=os.getenv("DB_NAME", "appdb"),
    )

@app.route("/")
def index():
    return send_from_directory(os.getenv("STATIC_DIR", "/app/static"), "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(os.getenv("STATIC_DIR", "/app/static"), path)

@app.route("/api/notes", methods=["GET"])
def list_notes():
    with get_db() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT id, title, content FROM notes ORDER BY id")
        return jsonify(cur.fetchall())

@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    with get_db() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING id, title, content",
            (data["title"], data.get("content", "")),
        )
        return jsonify(cur.fetchone()), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("HTTP_PORT", "8080")))