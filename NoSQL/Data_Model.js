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









