CREATE KEYSPACE my_keyspace WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};
USE my_keyspace;

CREATE TABLE users (user_id UUID PRIMARY KEY,username TEXT,email TEXT,created_at TIMESTAMP);
INSERT INTO users (user_id, username, email, created_at)
VALUES (uuid(), 'James William', 'james@money.com', toTimestamp(now()));
SELECT * FROM users;
UPDATE users set username = 'Monish Nule' where user_id =c360984f-54d6-4888-8832-0ff3381600df;
SELECT * FROM USERS;

SELECT * FROM USERS WHERE USERNAME = 'Monish Nule' ALLOW FILTERING ;
CREATE INDEX ON USERS (USERNAME);
SELECT * FROM USERS WHERE USERNAME = 'Monish Nule' ;
