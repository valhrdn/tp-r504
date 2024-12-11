CREATE DATABASE demodb;
USE demodb;
CREATE TABLE myTable (id INT AUTO_INCREMENT, name VARCHAR(45) NOT NULL, PRIMARY KEY (id));
INSERT INTO myTable (name) VALUES ('bob');
INSERT INTO myTable (name) VALUES ('alice');
INSERT INTO myTable (name) VALUES ('john');

