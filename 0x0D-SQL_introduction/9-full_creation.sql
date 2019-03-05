-- create table with rows
DROP TABLE IF EXISTS `second_table`;
CREATE TABLE second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO `second_table` (id, name, score)
<<<<<<< HEAD
VALUES(1, 'John', 10),(2, 'Alex', 3),(3, 'Bob', 14),(4, 'George', 8);
=======
VALUES('1', 'John', '10'),('2', 'Alex', '3'),('3', 'Bob', '14'),('4', 'George', '8');
>>>>>>> cf6972816ce1c158a429d884b5b006f2a73e3847
