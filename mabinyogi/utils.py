#handles creating char data in NOSQL format
from mabinyogi.cluster import warrior_collection, rogue_collection, mage_collection

#seperated functions in case we want to make use of this data for debugging
def create_char(form):
    char_data = {
        "_id": form.char_name.data,
        "race": form.char_race.data,
        "stature": form.char_stature.data,
    }
    return char_data

def add_char(form):
    char_data = create_char(form)
    char_class = form.char_class.data
    if char_class == 'Warrior':
        warrior_collection.insert_one(char_data)
    elif char_class == 'Rogue':
        rogue_collection.insert_one(char_data)
    elif char_class == 'Mage':
        mage_collection.insert_one(char_data)
    else:
        return 0 #if 0 is returned we have in issue
