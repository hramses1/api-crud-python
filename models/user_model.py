from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    nombre : str
    apellido: str
    direccion:str
    ci: int
    estado_civil:str
    fecha_nac: str
    
class UserCiModel(BaseModel):
    ci:int
class InsertUserModel(BaseModel):
    nombre : str
    apellido: str
    direccion:str
    ci: int
    estado_civil:str
    fecha_nac: str