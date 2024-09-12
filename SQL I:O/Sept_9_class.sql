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

ALTER TABLE dupe2 MODIFY salary int;
ALTER TABLE dupe2 RENAME COLUMN eid TO empid;
ALTER TABLE dupe2 DROP COLUMN city;

SELECT * FROM emp WHERE city LIKE 'D%' AND  Salary > 0;
SELECT * FROM emp WHERE city LIKE 'M%' AND salary > 50000;