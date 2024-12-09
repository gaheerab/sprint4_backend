const sqlite3 = require('sqlite3').verbose();

// Create the SQLite database file
const db = new sqlite3.Database('./db/profiles.db', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Database created or opened successfully.');
  }
});

// Create the user_profiles table
const createTableSQL = `
CREATE TABLE IF NOT EXISTS user_profiles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  bio TEXT,
  favorite_artists TEXT,
  profile_picture TEXT
);
`;

db.run(createTableSQL, (err) => {
  if (err) {
    console.error('Error creating table:', err.message);
  } else {
    console.log('Table created or exists already.');
  }
});

// Close the database connection
db.close();
