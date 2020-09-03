# we will import this at the top of whatever file we desire to use pymongo with to save us time on connecting to the db and specific collections
import pymongo
client = pymongo.MongoClient("mongodb+srv://QuhusVqw9WqyszTs:QuhusVqw9WqyszTs@mabinyogi.8pehk.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.Mabinyogi
#All collections are set here and may be imported as needed to various files 
mage_collection = db.Mage
warrior_collection = db.Warrior
rogue_collection = db.Rogue
