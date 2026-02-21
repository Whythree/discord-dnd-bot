# Was will ich mit der Klasse noch machen?
# Ich will eigentlich  alle namen haben.
# Diese Namen sind in einem dict. Also: spells: list aller spell namen
# Das machen wir für alle kategorien.
# Dann checken wir jede nachricht, ob darin eines dieser wörter ist.
# wenn ja haben wir die kategorie und anhand des worts die entity
# wir können dann also base_url/category/entity callen und eine Antwort ausgeben.
# Wobei die api ja auch eine url mitgibt. 

class KeywordHandler:
    def __init__(self, session):
        self.base_url = "https://www.dnd5eapi.co/api/2014"
        self.session = session
        self.data = {}
        
        
    async def setup(self):
        categories = [
            "spells",
            "alignments",
            "backgrounds",
            "classes",
            "conditions",
            "damage-types",
            "equipment",
            "feats",
            "features",
            "languages",
        ]
        
        for category in categories: 
            self.data[category] = None
            
        for category in categories: 
            await self.load_index(category)
    
    
    async def load_index(self, category):
        url = f"{self.base_url}/{category}"

        async with self.session.get(url) as response:
            if response.status == 200:
                returned_data = await response.json()
                # wir wollen nur die index speichern
                
                self.data[category] = returned_data
            else:
                print(response.status)
