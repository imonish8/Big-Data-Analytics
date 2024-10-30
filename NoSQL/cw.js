show dbs;
use test;
show collections;
db.getCollection()
db.getCollectionInfos()
db.getName()
db.createCollection('Students')
db.Students.insertOne({__id:"James",name : "James William", address : { student_id : "James", street : "123, Gandhi Nagar", city : "Mumbai", state : "MH"}})
db.Students.find()
db.Students.find({"address.city" : "Mumbai"})
db.Students.insertOne({__id:"Lame",name : "Lame William", address : [{  street : "123, Gandhi Nagar", city : "Mumbai", state : "MH"}, {  street : "123, MG Road", city : "Pune", state : "MH"}] })
db.Students.find({__id : "Lame"})
db.Book.find()
db.createCollection('Publisher')
db.Publisher.insertOne({publisher : {name : "apress", location : "Mumbai", founded : 1999}});
db.Publisher.find()
db.Book.insertOne({Author: "Christopher Nolan", Genre : "Thriller", Published_year:"2023", Title: "Oppenheimer" , id : "apress" })
db.Book.insertOne({Author: "Henery Cook", Genre : "Technology", Published_year:"2024", Title: "Apache" , id : "apress" })
db.Book.insertOne({Author: "Tim Cook", Genre : "Technology", Published_year:"2024", Title: "Mac Manual" , id : "apress" })
db.Book.insertOne({Author: "Ashlee", Genre : "Biography", Published_year:"2022", Title: "Elon Musk" , id : "rocks" })
db.Book.insertOne({Author: "Benjahim", Genre : "FInance", Published_year:"2002", Title: "Intelligent Investor" , id : "rocks" })
db.Book.find()

//db.createCollection('Publisher-Book')
//db.Publisher-Book.insertOne({ id : "apress", location : "Mumbai", founded : 1999});
//db.Publisher-Book.find()

db.createCollection('publisher_book')
db.publisher_book.insertOne({ id : "apress", location : "Mumbai", founded : 1999});
db.publisher_book.insertOne({ id : "rocks", location : "Pune", founded : 2002});
db.publisher_book.find()


// $lookup
/*
Lookup

aggregate
*/
db.publisher_book.aggregate([{$lookup : {from : 'Book', localField: 'id', foreignField : "id", as : "books docs" } }])

/*

Modeling Tree Structure Data model using Parent Reference


*/

use books_db
db.createCollection('Author')
db.Author.find()
db.Author.insertOne({_id : "Practical Apache Spark", parent : "Book"})
db.Author.insertOne({_id : "Professional MongoDB", parent : "Book"})
db.Author.insertOne({_id : "WebScrapping with Python", parent : "Book"})
db.Author.insertOne({_id : "Python Complete Reference", parent : "Article"})

//db.Author.insertOne({_id : "Java 18 Complete Reference", parent : "Herbert"})

db.Author.insertOne({_id : "Article", parent : "Herbert"})
db.Author.insertOne({_id : "Book", parent : "Herbert"})
db.Author.deleteOne({_id : "Java 18 Complete Reference"})
db.Author.insertOne({_id : "Herbert", parent : "null"})
db.Author.findOne({_id : "Practical Apache Spark"}).parent
db.Author.findOne({_id : "Herbert"}).parent
db.Author.findOne({_id : "Book"}).parent
db.Author.findOne({_id : "Article"}).parent
db.Author.parent
db.Author.find({parent : "Herbert"})
db.Author.find({parent : "Article"})
db.Author.find({parent : "Book"})
// Data model done with parent references.


db.createCollection('Author_child')
db.Author_child.insertOne({ _id : "Book", children : ["Practical Apache Spark","Professional MongoDB" ]})
db.Author_child.insertOne({ _id : "NoBook", children : []})
db.Author_child.insertOne({ _id : "NoBook1", children : []})
db.Author_child.insertOne({ _id : "NoBook2", children : []})
db.Author_child.insertOne({ _id : "Article", children : ["Java 18 Complete Reference"]})
db.Author_child.insertOne({ _id : "James", children : ["Book", "Article"]})

db.Author_child.findOne({_id: "Book"}).children
db.Author_child.findOne({_id: "NoBook"}).children
db.Author_child.findOne({_id: "NoBook1"}).children
db.Author_child.findOne({_id: "NoBook2"}).children
db.Author_child.findOne({_id: "Article"}).children
db.Author_child.findOne({_id: "James"}).children
db.Author_child.find({children: "Practical Apache Spark"})

db.createCollection('Author_Ancestors')
db.Author_Ancestors.insertOne({ _id : "Professional Apache Spark", ancestors : ['James', 'Book'], parent: 'Book'})
db.Author_Ancestors.insertOne({ _id : "Professional MongoDB", ancestors : ['James', 'Book'], parent: 'Book'})
db.Author_Ancestors.insertOne({ _id : "Book", ancestors : ['James'], parent: 'James'})
db.Author_Ancestors.insertOne({ _id : "Java 18 Complete Reference ", ancestors : ['James', 'Article'], parent: 'Article'})
db.Author_Ancestors.insertOne({ _id : "James", ancestors : [], parent: 'null'})

db.Author_Ancestors.findOne({_id : "Professional Apache Spark"}).ancestors
db.Author_Ancestors.findOne({_id : "Java 18 Complete Reference "}).ancestors
db.Author_Ancestors.findOne({_id : "James"}).ancestors

db.Author_Ancestors.find({ancestors: "James"})
db.Author_Ancestors.find()


use University;
db.createCollection("Students")
db.createCollection("Courses")

db.Students.insertOne({sid:"B01", fname : "James", lname: "William", age : 22, major: "Electronics" })
db.Students.insertOne({sid:"B01", fname : "Suresh", lname: "William", age : 23, major: "Electronics" })
db.Students.insertOne({sid:"B02", fname : "Dev", lname: "Patel", age : 22, major: "Electronics" })
db.Students.insertOne({sid:"B04", fname : "Mukesh", lname: "Patel", age : 21, major: "Computer Science" })
db.Students.find()

db.Courses.insertOne({cid: 101, cname : "Data Science" , instructor : "James W.", Credits : 4})
db.Courses.insertOne({cid: 102, cname : "Data Mining" , instructor : "Rasputin C.", Credits : 8})
db.Courses.insertOne({cid: 103, cname : "Digital Marketing" , instructor : "G. Bush", Credits : 2})
db.Courses.insertOne({cid: 104, cname : "Hacking" , instructor : "Edward Snowden", Credits : 10})
db.Courses.find()


// aggregate(grouping)
db.Students.aggregate({$group : {_id : "$sid"}})
db.Courses.aggregate({$group : {_id : "$cid"}})
db.Courses.aggregate({$group : {_id : "$cid", total_Credits : {$sum : "$Credits"}}})
db.Courses.aggregate({$group : {_id : "null", Total_credits :{$sum : "$Credits"}}})
db.Courses.aggregate([ { $group : { _id : null, count : {$sum : 1}}}])


show dbs;
use E-Commerce;
show collections;
db.Orders.find()
db.Orders.insertOne({_id: 1, cid : "C001", date : "2023-10-01", items : [{productID : "P001", quantity : 2, price : 20 }, {productID : "P002", quantity : 3, price : 30 }]})
db.Orders.insertOne({_id: 2, cid : "C002", date : "2023-10-03", items : [{productID : "P003", quantity : 40, price : 40 }, {productID : "P004", quantity : 5, price : 60 }]})
db.Orders.insertOne({_id: 3, cid : "C003", date : "2023-10-11", items : [{productID : "P005", quantity : 4, price : 60 }, {productID : "P006", quantity : 10, price : 50 }]})
db.Orders.insertOne({_id: 4, cid : "C004", date : "2023-10-15", items : [{productID : "P007", quantity : 7, price : 60 }, {productID : "P008", quantity : 15, price : 70 }]})

db.Orders.aggregate({$group : {_id : "null", REVENUE : {$sum : "$price"}}})

db.Orders.aggregate( [{$group : {_id : null}, Total_Revenue : {$sum : {$multiply : ["$items.quantity", "$items.price"]}}}])

db.Orders.aggregate([ { $unwind: "$items" }, { $group: {_id: "$cid", Total_Revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }} }]);
db.Orders.aggregate([ { $unwind: "$items" }, { $group: {_id: "null", Total_Revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }} }]);
db.Orders.aggregate([ { $unwind: "$items" }, { $group: {_id: "$items.productID", Total_Revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }} }]);


db.Orders.aggregate([ { $unwind: "$items" }, { $group: {_id: "$cid", order_revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }} },
  { $group: {_id: null,total_revenue: { $sum: "$order_revenue" },  orderCount: { $sum: 1 }}},
  //{$group: {_id: null,averageRevenue: { $divide: ["$total_revenue", "$orderCount"]}}} ]);



