CREATE TABLE user_table (
    username text,
    password text,
    name text,
    age int
);

INSERT INTO user_table VALUES ('karl', 'pwd', 'Karl', 16);
INSERT INTO user_table VALUES ('krish', 'pwd2', 'Krish', 96);

SELECT * FROM user_table;

SELECT username, password FROM user_table;