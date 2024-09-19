use empDB;

SELECT * FROM emp WHERE eid IN (SELECT eid FROM emp WHERE eid BETWEEN 3010 AND 3022);


SELECT * FROM Dupe;
# UPDATE Dupe SET Salary = salary + 

DELETE FROM Dupe WHERE eid in (SELECT eid FROM  (SELECT  eid FROM Dupe  WHERE salary > 50000) e1);
SELECT * FROM e1;

SELECT  MAX(emp_count) from (SELECT COUNT(EID) AS emp_count FROM emp GROUP BY dept) AS e1;
 
SELECT ename, city, salary FROM emp AS e1
WHERE salary > (SELECT AVG(salary) FROM emp WHERE city = e1.city);
 
SELECT eid, ename FROM emp e1 WHERE EXISTS (SELECT * FROM emp e2 WHERE  e2.eid = e1.eid);
 
SELECT * FROM emp WHERE LENGTH(ename) < 5;
SELECT eid FROM emp WHERE eid >= ANY  ( SELECT eid FROM emp);
SELECT eid FROM emp WHERE eid > ANY  ( SELECT eid FROM emp);

SELECT dept, SUM(salary) total_salary FROM emp GROUP BY dept HAVING total_salary >= ALL  (SELECT SUM(salary) FROM emp GROUP BY dept);
 
SELECT dept, SUM(salary) total_salary FROM emp GROUP BY dept HAVING total_salary >= ANY  (SELECT SUM(salary) FROM emp GROUP BY dept);
 
 
 