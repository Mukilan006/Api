from typing import List
from pydantic import BaseModel, StrictInt, StrictStr, constr


class UserDetails:
    id: int
    first_name: str
    status: bool

    def __init__(self, id: int, first_name: str, status: bool) -> None:
        self.id = id
        self.first_name = first_name
        self.status = status

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "status": self.status,
        }


class LoginResponse:
    access_token: str
    refresh_token: str
    id: str
    first_name: str
    status: bool

    def __init__(
        self,
        access_token: str,
        refresh_token: str,
        id: str,
        first_name: str,
        status: bool,
    ) -> None:
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.id = id
        self.first_name = first_name
        self.status = status

    def to_json(self) -> dict:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "id": self.id,
            "first_name": self.first_name,
            "status": self.status,
        }



