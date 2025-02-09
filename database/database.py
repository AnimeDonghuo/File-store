import motor.motor_asyncio
from config import DB_URI, DB_NAME, ADMINS

dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']
req_one = database['requested_users']  # Define the collection for requested users

default_verify = {
    'is_verified': False,
    'verified_time': 0,
    'verify_token': "",
    'link': ""
}

def new_user(id):
    return {
        '_id': id,
        'verify_status': default_verify
    }

async def present_user(user_id: int):
    found = await user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user = new_user(user_id)
    await user_data.insert_one(user)

async def db_verify_status(user_id):
    user = await user_data.find_one({'_id': user_id})
    if user:
        return user.get('verify_status', default_verify)
    return default_verify

async def db_update_verify_status(user_id, verify):
    await user_data.update_one({'_id': user_id}, {'$set': {'verify_status': verify}})

async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] async for doc in user_docs]
    return user_ids

async def del_user(user_id: int):
    await user_data.delete_one({'_id': user_id})

async def is_requested_one(message):
    user = await get_req_one(message.from_user.id)
    if user or message.from_user.id in ADMINS:
        return True
    return False

async def add_req_one(user_id):
    try:
        if not await get_req_one(user_id):
            await req_one.insert_one({"user_id": int(user_id)})
    except:
        pass
        
async def get_req_one(user_id):
    return await req_one.find_one({"user_id": int(user_id)})

async def delete_all_one():
    await req_one.delete_many({})
    
