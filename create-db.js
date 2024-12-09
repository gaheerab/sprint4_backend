const sqlite3 = require('sqlite3').verbose();

// Create a new SQLite database file
const db = new sqlite3.Database('./user_profiles.db', (err) => {
    if (err) {
        console.error('Error opening database:', err.message);
    } else {
        console.log('Database created or opened successfully!');
    }
});

// Create a table for user profiles
const createTableQuery = `
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    artists TEXT,
    profile_picture TEXT
);
`;

db.run(createTableQuery, (err) => {
    if (err) {
        console.error('Error creating table:', err.message);
    } else {
        console.log('Profiles table created successfully!');
    }
});

// Close the database connection
db.close((err) => {
    if (err) {
        console.error('Error closing the database:', err.message);
    } else {
        console.log('Database connection closed.');
    }
});

