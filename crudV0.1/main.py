from assimilator.core.services import CRUDService
from fastapi import FastAPI, Depends
from dependencies import get_crud, create_repository, create_uow
from schema import UserSchema


 
app = FastAPI() 

@app.get("/users")
async def list_users(crud: CRUDService = Depends(get_crud)):
    return crud.list()
 
@app.get("/users/{id}")
async def get_user(id: int, crud: CRUDService = Depends(get_crud)):
    return crud.get(id=id)

@app.post("/users")
async def create_user(
    user: UserSchema, crud: CRUDService = Depends(get_crud)
):
    return crud.create(user.dict())
 
@app.delete("/users/{id}")
async def delete_user(id: int, crud: CRUDService = Depends(get_crud)):
    return crud.list()


@app.put("/users/{id}")
async def update_user(id: int, user_data: UserSchema, crud: CRUDService =  Depends(get_crud),):
    return crud.update(id=id, update_data= user_data.dict())