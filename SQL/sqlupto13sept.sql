Create database empaug24;
use empaug24;
create table emp(
empid int,
ename varchar(30),
city varchar(20)
);
desc emp;
select * from emp;
insert into emp values
(24001,'Lalit','Delhi'),
(24002,'Pandit','Noida'),
(24003,'Sheebha','Chennai'),
(24004,'Anshika','Mumbai');
select * from emp;
alter table emp
add dept varchar(10);
alter table emp
add column salary float;
update emp set dept='IT';
update emp set dept='HR' where eid=24002;
alter table emp add column dept varchar(10);
update emp set dept='IT' where empid=24001;
update emp set salary=5000.0;
alter table emp drop dept;
alter table emp add column dept varchar(10) ;
update emp set dept='IT';
update emp set dept='HR' where empid=24001;
update emp set dept='civil' where empid=24002;
update emp set salary=30000 where ename='Anshika';
update emp set salary=40000 where dept='civil';
update emp set salary=35000 where ename='Sheebha';
alter table emp add column phno int ;
-- getting error
alter table emp modify phno  double;
insert into emp (phno) values
(1234567890),
(2345678901),
(3456789012),
(4567890123);
select ename, salary from emp where salary <30000;
select ename,salary from emp where ename like 'A%';
select ename,salary from emp where city like 'C%';
select ename,city from emp where city like 'i%';
select ename ,city from emp where city in ('Chennai','Delhi');
select ename ,city from emp where city not in ('Chennai','Delhi');
select * from emp;
select ename ,city from emp where empid between 24002 and 24004;
-- copying table without data
create table dupemp like emp;
select * from dupemp;
-- copying table with data
create table dupemp1 as select * from emp;
select * from dupemp1;
-- deleting only the data
truncate table dupemp1;
-- deleting the entire table
drop table dupemp;

create table dupemp as select * from emp;
# delele command
delete from dupemp; -- deletes the entire data
delete from dupemp where city='Delhi';
alter table dupemp rename  dupemp2;
alter table dupemp2 modify salary int;
select * from dupemp2;
-- rename a column
alter table dupemp2 rename column empid to eid;
-- drop a column
alter table dupemp2 drop column city;
delete from emp where ename=NULL;
select * from emp;
delete from emp where phno=1234567890;
delete from emp where phno=2345678901;
delete from emp where phno=3456789012;
delete from emp where phno=4567890123;
select * from emp where city like 'D%' and salary >30000;
select * from emp where city like 'D%' and salary <30000;
select * from emp where city like 'D%' or salary <30000;
update emp set phno=1234567890 where empid=24001;
update emp set phno=2345678901 where empid=24002;
update emp set phno=3456789012 where empid=24003;
update emp set phno=4567890123 where empid=24004;

# 10.9.2024
-- NOT NULL constraint
desc emp;
use empaug24;
select * from emp;
insert into emp (ename,city) values('Latha','Delhi');
delete from emp where ename='Latha';
alter table emp change salary salary int NOT NULL;
alter table emp change empid empid int NOT NULL;
insert into emp (ename,city) values('Latha','Delhi'); -- error

create table T1(tid int NOT NULL,tname varchar(20) NOT NULL);
insert into T1 values(23,'');
insert int T1 values(45);        -- get error

-- unique constraint
create table T2 (
eid int unique,
ename varchar(20));
insert into T2 values (23,'Poppu');
insert into T2 values(23,'Kavin');
insert into T2 values(NULL,'Jim');   -- allows null values
delete from T2 where ename ='Jim';     -- or ename like J%
alter table T2 change eid empid int unique NOT NULL;
select * from T2;
insert into T2 values(34,'Kavin');
insert into T2 values(NULL,'Jim');      -- not allowing NULL
alter table T2 add column salary int;
alter table T2 change column ename ename varchar(20) primary key;
alter table T2 change salary salary  float;

-- check constraint

create table voterlist(vid int NOT NULL check (vid >18), vname varchar(20));
insert into voterlist values(23,'Teena'),(45,'Kayal'),(35,'Srimayi');
insert into voterlist values (17,'Tom');       -- error

select * from emp;
alter table emp add column age int NOT NULL check (age>=22);

alter table emp add column age int;
alter table emp change column age age int  check (age>22);
-- default constraint
create table E1(eid int unique not null, ename varchar(20),dept varchar(10) default 'IT');
insert into E1(eid,ename) values (25,'Pallavi');

alter table emp change salary salary int default 40000;
insert into emp(empid,ename,city,dept,phno) values(24005,'Jerry','Pune','Admin',5678901234);

-- primary key
create table T3(tid int primary key,tname varchar(20));
insert into T3 values (Null,'Kevin');  -- error
insert into T3 values (23,'kevin');
insert into T3 values (23,'Mickey');  -- error
select * from T3;

select * from emp;
alter table emp add primary key(empid);
insert into emp values (empid,ename,city,salary,dept,phno,age)(24001,'Mickey','Delhi',55000,'IT',467678668,34);

-- auto increment
create table T4 (tid int primary key auto_increment,tsal int);
insert into T4 (tsal) values (35000);
select * from T4;
insert into T4 (tsal)values (34000),(78000),(56000);
alter table T4 auto_increment=40;
insert into T4 (tsal)values(20000),(65000);

-- foreign key
create table department (deptid varchar(10) primary key,deptname varchar(10));
insert into department values('IT','Informatio'),('Admin','Adminis'),('HR','Human');
select * from department;
alter table department add primary key(deptid);
alter table department add constraint f_dept foreign key (deptid) references emp(dept);
alter table department modify deptname varchar(25);
drop table department;
select * from emp;
select * from emp where empid=24001;
select empid,ename,salary from emp where empid=24001;
select avg(salary) from emp;
select * from emp where salary<43800;
select count(salary) where salary<43800;
select * from emp;
insert into emp values
(24006,'Krishna','Bangalore',50000,'ECE',6789012345,25);
insert into emp values
(24007,'Radha','Chennai',43000,'EEE',7890123456,34),
(24008,'Haritha','Rajasthan',80000,'Finance',8901234567,56),
(24009,'Akhil','Hyderabad',75000,'Admin',9012345678,45),
(24010,'Srimayi','Pune',40000,'EEE',8234567892,23);

create table empcommunication(
comn_id int,
empid int , foreign key (empid) references emp (empid)
On delete cascade
on update cascade,
address varchar(25),
zip_code int);

insert into empcommunication values
(101,24001,'Venus Colony,Velachery',600001),
(102,24002,'Bharathi Street',600002),
(103,24003,'Shakthi Street',600003),
(104,24004,'Kumaran Street',600004),
(105,24005,'Kambar Street',600005),
(106,24006,'Baba Garden',600006),
(107,24007,'Little Street', 600007),
(108,24008,'VGP Street',600008),
(109,24009,'Selva Colony',600009),
(110,24010,'Star Colony',600010);

select * from emp;

update emp set age=20 where empid=24001;
update emp set age=24 where empid=24001;
update emp set age=36 where empid=24002;
update emp set age=38 where empid=24003;
update emp set age=46 where empid=24004;
update emp set age=28 where empid=24005;

select * from empcommunication where empid=24001;
select count(*) from empcommunication;
select * from emp;
select count(*) from emp where salary>20000;
select * from emp where salary>20000;

select sum(salary) from emp where salary<20000;
select sum(salary) from emp where salary<40000;
select count(*) from emp where salary<40000;
select * from emp where salary<40000;

select avg(salary) from emp;
select count(*) from emp where salary<43800;
select count(*)from emp where salary>(select avg(salary) from emp);
use empaug24;

select salary,count(*) from emp group by salary;
select * from emp;
select dept,count(*) from emp group by dept;
select salary,count(*) from emp where salary>40000 group by salary;
select dept,count(*) from emp where dept in ('IT','ECE') group by dept;
select age,count(*) from emp where age>30 group by age;
select dept,count(*) from emp group by dept having count(*) >1;
select city,count(*) from emp group by city having count(*)>1;
select ename,city,count(*) from emp group by ename,city having count(*)=1;
select ename,count(*) from emp where ename like 'a%' group by ename having count(*)=1;
select ename,count(*) from emp where city in ('Chennai','Pune') group by ename;
select distinct * from emp;
select distinct city from emp;
select distinct city from emp where age>20;
select distinct dept from emp;
select min(age) from emp;
select max(age) from emp;
select min(age) from emp where dept='IT';
select min(age) from emp where salary>50000;
select max(age) from emp where city in ('Delhi','Hyderabad');
select max(age) from emp where ename like 'A%' and salary>5000;
select max(age) from emp where ename like 'A%' and salary>5000;
select * from emp;
select max(salary) from emp where age<30;
select upper(ename) from emp;
select lower(ename) from emp where age>25;
select length(phno) from emp;
select ename, length(ename) from emp;
select ename,upper(city) from emp where city in ('Pune','Chennai');
select upper(ename),upper(city) from emp where city in ('Pune','Chennai');
select concat(ename,' ',dept) as namedept from emp;
select concat(ename,' ',phno) as nameph from emp;
select concat(empid,' ',ename) as idname from emp where age<40;
select age,concat(empid,' ',ename) as idname from emp where age<40;
select ename from emp where length(ename)<10;
select ename from emp where length(ename<=5);
select ename from emp where length(phno)<10;
select concat(ename,age,'@','gmail.com') as email from emp;
select dept,avg(salary) from emp group by dept;
select dept from emp group by city,dept;
select concat(dept,' ',city) as deptcity from emp;
select city,concat(dept,' ',city)as deptcity from emp group by city,deptcity;
select city,count(*) from emp group by city,length(ename)>5;
select * from emp;
select city,avg(length(ename)) from emp group by city;
select city,sum(length(phno)) from emp group by city;
select city,count(*) from emp  where length(ename)>5 group by city;
