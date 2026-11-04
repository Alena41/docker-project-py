CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL DEFAULT ''
);

INSERT INTO notes (title, content) VALUES
    ('Первая заметка', 'Привет, Docker!'),
    ('Вторая заметка', 'сборка работает');