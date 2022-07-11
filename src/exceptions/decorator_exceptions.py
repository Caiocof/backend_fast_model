from fastapi import HTTPException, status


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error)

        except NameError as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

        except TypeError as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)

    return wrapper
