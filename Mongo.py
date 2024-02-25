import pymongo

# MongoDB connection details
mongo_uri = "mongodb+srv://quinteroalf:Teclado02_@cldw.igp2bgz.mongodb.net/"
database_name = "sample_supplies"
collection_name = "sales"
#mongodb+srv://quinteroalf:Teclado02_@cldw.igp2bgz.mongodb.net/
# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri,tlsAllowInvalidCertificates=True)
database = client[database_name]
collection = database[collection_name]

# Example Query: Find all documents in the collection
cursor = collection.find({"purchaseMethod":"Phone"})

# Print the results
for document in cursor:
    print(document)

# Close the MongoDB connection
client.close()