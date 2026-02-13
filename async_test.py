import asyncio


async def slow_api_call():
    print("Calling API")
    await asyncio.sleep(2)
    return {"Spell":"Fireball","Level":"3"}

print(asyncio.run(slow_api_call()))

