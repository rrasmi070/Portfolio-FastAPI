from . import connection_client


try:
    connection_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



client = connection_client.list_database_names()
print("Listing databases",client)
res = connection_client.my_portfolio
val = res.get_collection("test_database")

dicts = {'name': 'Ranjan', 'age':'40'}