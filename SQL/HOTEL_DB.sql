CREATE DATABASE HOTEL_DB;
USE HOTEL_DB;
CREATE TABLE mgmt (ID INT PRIMARY KEY AUTO_INCREMENT,Designation VARCHAR(100),experience VARCHAR(50), type_Cuisine VARCHAR(100));
INSERT INTO mgmt (ID, Designation, experience, type_cuisine) VALUES (1,'Sr.Chef', '8-10 years','Thai');
SELECT * FROM mgmt;

INSERT INTO mgmt (ID, Designation, experience, type_cuisine) 
VALUES
(2,'Mid Sr. Chef', '3-7 years','Chinese'),
(3, 'Jr.Chef','1- 2years', 'Indian'),
(4, 'Asscoiate Jr. Chef','1.5 years','Indian'),
(5, 'Fresher','0 year','No Speciality');
