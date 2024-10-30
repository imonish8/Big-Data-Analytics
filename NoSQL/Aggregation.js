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

/*
db.Orders.aggregate([ { $unwind: "$items" }, { $group: {_id: "$cid", order_revenue: { $sum: { $multiply: ["$items.quantity", "$items.price"] } }} },{ $group : {orderCount: { $sum: 1 }}},{ Total_avg : {$divide : ["$order_revenue", "$orderCount"]}} ]);
  //{ $group: {_id: null,total_revenue: { $sum: "$order_revenue" },  orderCount: { $sum: 1 }}},
  //{$group: {_id: null,averageRevenue: { $divide: ["$total_revenue", "$orderCount"]}}} ]);
db.Orders.aggregate([ { $unwind : "$items"}, { $group : {id : "_id", orderTotal : {$sum :{ $multiply :  ["$items.quantity", "$items.price"]}}}},{$group :  {_id: null, averageOrder: {}}}

])
*/
db.Orders.aggregate([{$unwind:"$items"},{ $group: { _id: null,  totalRevenue: { $sum: { $multiply: ["$items.quantity", "$items.price"]  } }, orderCount:{$sum: 1} } }, {$project: {_id:0, avgOrderRevenue: {$divide: ["$totalRevenue", "$orderCount"]}}}]);
db.Orders.aggregate([{$unwind:"$items"},{ $group: { _id: null,  totalRevenue: { $sum: { $multiply: ["$items.quantity", "$items.price"]  } }, orderCount:{$sum: 1} } }, {$addFields: {_id:0, $addFields: {averageRevenue: { $divide: ["$totalRevenue", "$orderCount"] }}}}  ]);

var activity1 = function(){var pipeline= []; db.Orders.aggregate(pipeline).forEach(printjson);};
activity1();

db.movies.insertOne(

 {
    "_id" : ObjectId("573a1390f29313caabcd4135"),
    "plot" : "Three men hammer on an anvil and pass a bottle of beer around.",
    "genres" : ["Short"],
    "runtime" : 1,
    "cast" : ["Charles Kayser","John Ott"],
    "num_mflix_comments" : 1,
    "title" : "Blacksmith Scene",
    "fullplot" : "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
    "countries" : ["USA"],
    "released" : ISODate("1893-05-09T00:00:00Z"),
    "directors" : ["William K.L. Dickson"],
    "rated" : "UNRATED",
    "awards" : {
            "wins" : 1,
            "nominations" : 0,
            "text" : "1 win."
    },
    "lastupdated" : "2015-08-26 00:03:50.133000000",
    "year" : 1893,
    "imdb" : {
            "rating" : 6.2,
            "votes" : 1189,
            "id" : 5
    },
    "type" : "movie",
    "tomatoes" : {
            "viewer" : {
                    "rating" : 3,
                    "numReviews" : 184,
                    "meter" : 32
            },
            "lastUpdated" : ISODate("2015-06-28T18:34:09Z")
    }
}) ;

db.movies.find()