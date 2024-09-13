CREATE TABLE admins (
  id INT PRIMARY KEY,
  username VARCHAR(50),
  password_hash VARCHAR(1500), 
  salt VARCHAR(300),
  hash_algo VARCHAR(30),
  iterations INT
);