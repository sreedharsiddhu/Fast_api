from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()



    

@app.get("/")
def welcome():
    return {"message": "Welcome to FastAPI"}


@app.get("/sreedhar")
def about():
    return{"about" :"hi my name is sreredhar ejknfhkdjs nfekhfhdskjr kdfhdfj kjndfkhfk knsdfnjdf "}

@app.get("/devi")
def about_devi():
    return{"about devi" : "bdhadshjhb dvfjadsjf jadsvfvjdbjds,jhasvhfhddh,j jhbfgdashgf jhadhahdsbvcjh jzsbdcdj, hjbvhbf"}


# Define the Pydantic model for a ToDo item
class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool

@app.post("/todos")
def create_todo(todo: TodoItem):
    if not todo.title or not todo.description:
        raise HTTPException(status_code=400, detail="Title and description cannot be empty")
    return {"message": todo.dict()}

# Define the Pydantic model for a ToDo item
class chicken_biryani(BaseModel):
    bir_type: int

@app.post("/biryani")
def get_biryani(biryani: chicken_biryani):
    people = [
        {"names": "sree", "age": 25},
        {"names": "sai", "age": 23}
    ]
    
    age_limit = biryani.bir_type # Extract the age from the biryani input model
    result = []
    
    for i in people:
        # No need for dict() as 'person' is already a dictionary
        if i['age'] >= age_limit:
            result.append(i)  # Use append, not push
    
    return result