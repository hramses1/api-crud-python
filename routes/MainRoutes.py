#--------------------------------------------#
from fastapi import APIRouter
from starlette.status import HTTP_200_OK,HTTP_204_NO_CONTENT
#--------------------------------------------#
from services.MainServices import MainServices
from models.user_model import InsertUserModel,UserCiModel
#--------------------------------------------#
##uvicorn app:app --reload
main = APIRouter(prefix="/api/main")
#-----------------------------------------------------#
@main.post(
    "/insertData",
    status_code=HTTP_200_OK,
    description="Insertar Usuarios a la Base de Datos",
    tags=['Usuarios'],
)
async def insertData(usuario: InsertUserModel):
    main_service = MainServices()
    return main_service.InsertUser(usuario)
#-----------------------------------------------------#
@main.post(
    "/seartUser",
    status_code=HTTP_200_OK,
    description="Obtiene el Usuario por CI",
    tags=['Buscar'],
)
async def SeartData(usuario: UserCiModel):
    main_service = MainServices()
    return main_service.SearchUser(usuario)
#-----------------------------------------------------#
@main.delete(
    "/deleteUser/{user_id}",
    status_code=HTTP_204_NO_CONTENT,
    description="Eliminar un usuario por ID",
    tags=['Eliminar'],
)
async def delete_user(user_id: int):
    main_service = MainServices()
    return main_service.DeleteUser(user_id)
#-----------------------------------------------------#
@main.put(
    "/updateUser/{user_id}",
    status_code=HTTP_200_OK,
    description="Actualizar un usuario por ID",
    tags=['Update'],
)
async def update_user(user_id: int,updated_user: InsertUserModel):
    main_service = MainServices()
    user = main_service.UpdateUser(user_id, updated_user)
    return user
#-----------------------------------------------------#