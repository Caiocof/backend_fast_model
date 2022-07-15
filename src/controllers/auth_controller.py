from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from src.controllers.base import BaseController
from src.db.cruds.auth_crud import AuthCRUD
from src.db.settings.config import get_db
from src.settings.providers.hash_provider import verify_password
from src.settings.providers.token_provider import create_access_token, decode_token

from src.schemas.auth.auth_schema import LoginData, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthController(BaseController):

    def __init__(self):
        super(AuthController, self).__init__(AuthCRUD)

    def handle_login(self, db: Session, user_data: LoginData):
        user = AuthCRUD().find_by_user_name(db=db, user_name=user_data.username)
        if not user or not verify_password(user_data.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='username or password invalid!')
        token = create_access_token({'sub': user.username})

        return {'username': user.username, 'access_token': token}

    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
        try:
            username: str = decode_token(token=token)

            if username is None:
                raise exception
            token_data = TokenData(username=username)
        except JWTError:
            raise exception
        user = AuthCRUD().find_by_user_name(db=db, user_name=token_data.username)
        if user is None:
            raise exception
        return user
