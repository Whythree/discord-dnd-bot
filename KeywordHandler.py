
import aiohttp
import asyncio

class KeywordHandler:
    def __init__(self,session):
        self.base_url = "https://www.dnd5eapi.co/api/2014"
        self.session = session
        self.spells = None

    async def load_index(self, category:str):
        url = f"{self.base_url}/{category}"

        async with self.session.get(url) as response:
            if response.status == 200: 
                self.spells = await response.json()
            else:
                response.raise_for_status()
    


