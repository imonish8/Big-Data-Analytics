use empDB;
SELECT * FROM emp;
SELECT * FROM departments;
SELECT dept, sum(salary) as totalsal FROM  emp GROUP BY dept;
SELECT dept, sum(salary) as totalsal FROM  emp GROUP BY dept having sum(salary) < 20000;
SELECT * FROM emp ORDER BY ename;
SELECT * FROM emp ORDER BY ename ASC;
SELECT * FROM emp ORDER BY ename DESC;