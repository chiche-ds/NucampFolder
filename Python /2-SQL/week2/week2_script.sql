
CREATE TABLE divisions (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    home_color TEXT NOT NULL,
    away_color TEXT,
    division_id INT
);