create database black_stone;
use black_stone;
create table emp (eid int , ename varchar(100), city varchar(100));
desc emp;
select * from emp;

insert into emp values(3008, 'Edward Snowden', 'Mumbai');
insert into emp values(3009, 'Putin', 'Beed');
insert into emp values(3010, 'George Bush', 'Dadar');
insert into emp values(3011, 'Rajendra', 'Delhi');
insert into emp values(3012, 'Bittu', 'Satara');


alter table emp add column dept varchar(40);
alter table emp add column salary float;

update emp set salary = 55000.59 where eid =3008;
update emp set salary = 53900 where eid =3009;
update emp set salary = 34000 where eid =3010;
update emp set salary = 345000 where eid =3011;
update emp set salary = 34200 where eid =3012;

select * FROM emp;
SELECT ename, salary FROM emp;
SELECT ename, salary FROM emp WHERE salary < 80000;
SELECT ename, salary FROM emp WHERE salary > 80000;
SELECT ename, salary FROM emp WHERE salary BETWEEN 40000 AND 60000;
SELECT ename, salary FROM emp WHERE ename LIKE 'M%';
SELECT ename, salary FROM emp WHERE city LIKE 'D%';
SELECT ename, salary FROM emp WHERE city LIKE 'M%';
SELECT ename, salary FROM emp WHERE city NOT IN ('Chennai','Hyderbad', 'DeLhi');


CREATE TABLE dupe AS SELECT  * FROM emp;
SELECT * FROM dupe;

DROP TABLE dupe;
TRUNCATE TABLE dupe;
DELETE FROM  dupe WHERE city = 'Delhi';

ALTER TABLE dupe RENAME dupe2;
DESCRIBE dupe;
DESCRIBE dupe2;


#MODIFY TABLE COLUMN
ALTER TABLE dupe2 MODIFY salary int;
ALTER TABLE dupe2 RENAME COLUMN eid TO empid;
ALTER TABLE dupe2 DROP COLUMN city;

# SELECT NAMES STARTS WITH SOMETHING USING LIKE KEYWORD
SELECT * FROM emp WHERE city LIKE 'D%' AND  Salary > 0;
SELECT * FROM emp WHERE city LIKE 'M%' AND salary > 50000;

# WHAT ARE NULL VALUES ?
CREATE TABLE T1 ( tid INT NOT NULL, tname VARCHAR(100) NOT NULL);
INSERT INTO T1 VALUES (23, ' ');
SELECT * FROM T1;
INSERT INTO T1 VALUES( 25, NULL);

# UNIQUE CONSTRAINTS.
ALTER TABLE T1 CHANGE eid empid INT UNIQUE NOT NULL;
DELETE FROM T1 WHERE ename LIKE tid = 25;

CREATE TABLE T2 (eid int unique, ename varchar (20)not null );
INSERT into T2 values (23, 'Rajesh');
INSERT into T2 values(23, 'Romi');
INSERT into T2 values(18, 'Bobby');
INSERT into T2 values(20, 'Sunny');
INSERT into T2 values(19, 'Bunny');
INSERT into T2 values (NULL, 'jimm');
SELECT* from T2;
DELETE from T2 where ename like '%J';
ALTER table T2 change eid empid int unique NOT NULL;

# constraint DEFAULT UNIQUE CHECK 

# CREATE TABLE voterlist (vid INT NOT NULL CHECK (vid > 18), vname VARCHAR (20) NOT NULL);
ALTER TABLE T2 ADD CHECK (empid >= 18);

ALTER TABLE emp  CHANGE Salary sal INT DEFAULT 50000;
INSERT INTO emp (eid, ename, city,dept) VALUES(3013, 'Devanada','Mumbai','IT');

# PRIMART CONSTRIANTS.

CREATE TABLE T3 (tid INT PRIMARY KEY, tname VARCHAR(30));
# primary wont allow null, unique will allow it
INSERT INTO T3 VALUES (NULL, 'Vaishnav');
INSERT INTO T3 VALUES (11, 'Vaishali');

# auto)increment

CREATE TABLE T4 (tid INT PRIMARY KEY AUTO_INCREMENT, tsal INT);
INSERT INTO T4 (tsal) VALUES (43000),(33389),(33422);
ALTER TABLE T4 AUTO_INCREMENT =40;
SELECT * FROM T4;
INSERT INTO T4 (tsal) VALUES (44000);

# foreign key demo

CREATE TABLE departments (deptID VARCHAR(40), deptName VARCHAR(100), eid INT, FOREIGN KEY (eid) REFERENCES emp(eid) );
INSERT INTO departments VALUES ('HR','Human Resource'), ('IT','Information Technology'), ('Mgmt', 'Management'),('Admin','Adminstration');
INSERT INTO departments VALUES('Stores', 'Stores Dept',24008);
SELECT * FROM departments;
ALTER TABLE departments ADD PRIMARY KEY (deptID);
ALTER TABLE departments ADD CONSTRAINT F_DEPT FOREIGN KEY  (deptID) REFERENCES emp(dept); 



ALTER TABLE emp ADD PRIMARY KEY (eid);


