from datetime import datetime
import uuid

class Note:
    def __init__(self, title, content):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f"Note: id:{self.id}\n title:{self.title}\n content:{self.content}\n fecha de creacion:{self.created_at}"

nota1 = Note("mi vida" , "la vida es bonita ls verdas es que es demasiado introspectiva tener que ver todo de una manera estratewgica y sensible ")
print(nota1)

