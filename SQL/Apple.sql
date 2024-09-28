use black_stone;
CREATE TABLE Apple (ID INT PRIMARY KEY AUTO_INCREMENT, Products VARCHAR(100), Latest_Model VARCHAR(300),Price_Range INT);
DESCRIBE Apple;
INSERT INTO Apple (ID, Products, Latest_Model, Price_Range)
VALUES 
(1,'Macintosh', 'MacBook 15inch M3', 1200),
(2,'iPhones', 'iPhone 16 Pro Max', 1200 ),
(3,'Apple TV', 'TV4K', 300 ),
(4,'Home', 'HomePod', 699 ),
(5,'iPads', '13in iPad Pro', 1200 ),
(6,'Watch', 'Watch 10 Thinastic', 598 ),
(7,'AirPods', 'AirPods 4', 200 ),
(8,'Subscription based', 'Apple One', 2 ),
(9,'Accessories', 'All Models', 50  ),
(10,'Wallets', 'Apple Pay', 0 ),
(11,'Air Tags', 'Air Tag 3',20 ),
(12,'Vision', 'Vision Pro', 5000 );

SELECT * FROM Apple;
update Apple SET Products = 'Macintosh Books' WHERE ID =1; 

SELECT AVG(Price_Range) FROM Apple;

SELECT Price_Range,COUNT(*) FROM Apple GROUP BY Price_Range;
SELECT Products, COUNT(*) FROM Apple GROUP BY Products;

SELECT Price_Range,COUNT(*) FROM Apple WHERE Price_Range > 400 GROUP BY Price_Range;
SELECT ID, COUNT(*) FROM Apple WHERE ID > 6 GROUP BY ID;
SELECT Products, COUNT(*) FROM Apple WHERE Products IN ('Air Tags', 'Accessories', 'Home') GROUP BY Products;
# HAVING KEY IS FOR CONDITION 
# LIKE 
SELECT ID, Price_Range, COUNT(*) FROM Apple GROUP BY ID, Price_Range HAVING COUNT(*) > 1;

# BIGGEST COMMAND OF ALL TIME 
SELECT Products, COUNT(*) FROM Apple WHERE  Products LIKE '%A' GROUP BY Products HAVING COUNT(*)=i;


SELECT DISTINCT * FROM Apple;
SELECT DISTINCT Products FROM Apple;
SELECT DISTINCT ID,Price_Range FROM Apple WHERE Price_Range > 300;
SELECT MIN(Price_Range) FROM Apple;
SELECT MAX(Price_Range) FROM Apple;
SELECT MIN(Price_Range) FROM Apple WHERE Price_Range > 300;
SELECT MIN(Price_Range) FROM Apple WHERE Products LIKE '%H' AND Price_Range > 300;
SELECT MAX(Price_Range) FROM Apple WHERE Products LIKE '%M' AND Price_Range > 100;

