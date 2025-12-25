import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def run():
  try:
    con = await asyncpg.create_pool(
      user=os.getenv('DB_TASKS_USER'), 
      database=os.getenv('DB_TASKS_NAME'), 
      password=os.getenv('DB_TASKS_PASSWORD'),
      host='localhost',
      port=5432
      )
    
    print("Connected to db")
    value = await con.fetchval("SELECT 1;")
    print ("Query result: ", value)

    await con.close()
    print("Connection closed")
  except Exception as e:
    print("Connection failed:")
    print(e)

print("DB_TASKS_USER =", os.getenv("DB_TASKS_USER"))

asyncio.run(run())