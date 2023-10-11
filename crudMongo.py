import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["kumar"]
collection = db["mycoll1"]

def add_document():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    new_document = {
        "name": name,
        "age": age,
        "city": city
    }
    collection.insert_one(new_document)
    print("Document added successfully!")

def view_documents():
    documents = collection.find()
    print("\nAll Documents:")
    for document in documents:
        print(document)
    print("\n")

def update_document():
    name = input("Enter name of the document to update: ")
    update_query = {"name": name}
    document = collection.find_one(update_query)
    if document:
        new_age = int(input("Enter new age: "))
        new_city = input("Enter new city: ")
        new_values = {"$set": {"age": new_age, "city": new_city}}
        collection.update_one(update_query, new_values)
        print("Document updated successfully!")
    else:
        print("Document not found!")

def delete_document():
    name = input("Enter name of the document to delete: ")
    delete_query = {"name": name}
    result = collection.delete_one(delete_query)
    if result.deleted_count > 0:
        print("Document deleted successfully!")
    else:
        print("Document not found!")

while True:
    print("\nMenu:")
    print("1. Add Document")
    print("2. View Documents")
    print("3. Update Document")
    print("4. Delete Document")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        add_document()
    elif choice == "2":
        view_documents()
    elif choice == "3":
        update_document()
    elif choice == "4":
        delete_document()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the MongoDB connection
client.close()
