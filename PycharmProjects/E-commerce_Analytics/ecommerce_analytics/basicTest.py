from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

# Access the collections
users = db["users"]
transactions = db["transactions"]

# Example: Insert a new user
new_user = {
    "name": "Bob Smith",
    "email": "bob@example.com",
    "created_at": "2024-10-31T10:00:00"
}
users.insert_one(new_user)

# Example: Query users
for user in users.find():
    print(user)