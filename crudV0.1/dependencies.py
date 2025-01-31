from assimilator.internal.database import InternalRepository, UnitOfWork, InternalUnitOfWork
from sqlalchemy.orm import sessionmaker
from assimilator.core.services import CRUDService
from dependencies import get_uow

 
from database import engine, User
from schema import UserSchema, Userschema 

DatabaseSession = sessionmaker(engine)

def get_repository() -> InternalRepository:
    return InternalRepository(
        session=DatabaseSession(),
        model=UserSchema
    )


def get_uow() -> UnitOfWork:
    return InternalUnitOfWork(repository=get_repository())


def get_crud() -> CRUDService:
    return CRUDService(uow=get_uow())