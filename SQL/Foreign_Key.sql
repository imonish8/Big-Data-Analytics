use empDB;
CREATE TABLE airlines (jobID INT, jobName VARCHAR(100), jobDesc VARCHAR(100) ,eid INT , FOREIGN KEY (eid) REFERENCES emp(eid));
INSERT INTO airlines (jobID, jobName, jobDesc) 
VALUES
(101,'Pilot', 'Flies the Plane'),
(102, 'Co-Pilot', 'Asscoiate to Captain'),
 (103, 'Hostess', 'For the Lavish Hospitality'), 
 (104, 'Technical Engineer', 'Off the plane'), 
 (105, 'Supporting Staff','Associates to Lead'),
 (107, 'Control Officer', 'Stays off- the Plane'), 
 (108, 'Command Officer', 'Off- the Plane'), 
 (109, 'Aviation Officer','Off-the Plane'),
 (109, 'Aviation Officer','Off-the Plane');
 
 SELECT * FROM airlines;
 SELECT * FROM emp;
 DELETE  FROM airlines WHERE jobID = 109;
 
 INSERT INTO airlines (jobID, jobName, jobDesc, eid) 
VALUES
(109,'Cheif', 'Decision Maker',3008 );

INSERT INTO airlines (jobID, jobName, jobDesc, eid) 
VALUES
(110,'Guard', 'Ground Staff',3009 ),
(111,'Cheif of Guard', 'Leads Guards',3010 ),
(112,'Cabin Crew', 'Hospitality boarding the plane',3011 );

# count
SELECT COUNT(*) FROM emp;