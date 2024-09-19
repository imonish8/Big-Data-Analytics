use empDB;

SELECT ename, dept_Name FROM emp JOIN Department ON emp.dept = Department.dept;
#NO NULL VALUES WHEN USING SIMPLE JOIN

SELECT ename, dept_Name FROM emp, Department WHERE emp.dept = Department.dept;
# NO NULL, THAT IS IT IS TAKING MATCH IDs with values, droping the values which has no corresponding values

SELECT ename, dept_Name FROM emp LEFT JOIN Department ON emp.dept = Department.dept;
#lect join taking all emp values ignoring match in departments

SELECT ename, dept_Name FROM emp RIGHT JOIN Department ON emp.dept = Department.dept;
# right join taking all department values of the table, ignoring emp .







