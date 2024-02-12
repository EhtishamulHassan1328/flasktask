-- Some commands that were used to create flasktaskdb in Flask
-- And a user named hassan with the password 'pass'

create database flasktask

use flasktask

CREATE USER 'hassan'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON flasktask.* TO 'hassan'@'localhost';
FLUSH PRIVILEGES;


show tables;


select * from user


select * from subject_grade