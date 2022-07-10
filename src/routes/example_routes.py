from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.db.settings.config import get_db
from src.schemas.example import ExampleBase

v1_example = APIRouter(prefix='/v1', tags=['Example'])


@v1_example.get('/example', response_model=List[ExampleBase])
async def list_example(db: Session = Depends(get_db)):
    try:
        return {'Msg': 'API run'}
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Erro ao listar. {error}'
        )
    except NameError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Erro ao listar. {error}'
        )
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao listar. {error}'
        )
