USE empDB;


CREATE TABLE Dupe3 AS SELECT * FROM emp;
SELECT * FROM Dupe3;
SELECT * FROM emp;
SELECT * FROM emp UNION SELECT * FROM Dupe3;
INSERT INTO Dupe3 VALUES (3022, "Maya", "Mumbai", "HR",200000),(3023, "laya", "Mumbai", "IT",900000);
# SELECT * FROM emp INTERSECT  SELECT * FROM Dupe3;

# SELECT * FROM Dupe3 EXCEPT SELECT * FROM emp;

SELECT * FROM Dupe3 CROSS JOIN  emp;

# Catesian Product
-- SELECT * FROM emp INNER JOIN department on emp.Dept = Department.Dept;Companies
SELECT * FROM Department INNER JOIN emp ON Department.Dept = emp.Dept;
SELECT * FROM emp;
SELECT * FROM Department;
SELECT * FROM emp NATURAL JOIN Department;

ALTER TABLE my_first_db.Department RENAME COLUMN Dept_id TO dept;

INSERT INTO my_first_db.Department VALUES (4,"Finance", "Financial Dept","Mumbai"),(5,"Training", "Training Dept","Chennai");
DESC Department;

CREATE TABLE Department (ID INT PRIMARY KEY AUTO_INCREMENT, dept VARCHAR(100), Dept_Name VARCHAR(100));

 # INSERT INTO Department VALUES (1,"Finance", "Financial Dept"),(2,"Training", "Training Dept");
INSERT INTO Department (dept,Dept_Name) VALUES ("MLE", "Machine Learning Engineer"),("QA", "Automation"),("SE2", "Software engineer");
