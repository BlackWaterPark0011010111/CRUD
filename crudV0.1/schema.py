from assimilator.core.database.models import BaseModel

class UserSchema(BaseModel):
    username: str
    balance: float = 0