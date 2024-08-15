def NoteEntity(item) -> dict :
    return {
        "name": str(item['name']),
        "email": item['email'],
        "contact": item['contact'],
        
    } 

def NotesEntity(items) -> list:
    return [NoteEntity(item) for item in items]