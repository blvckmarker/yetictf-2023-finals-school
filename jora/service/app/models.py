from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: int
    username: str
    password: str
    info: str


class RegistrationModel(BaseModel):
    username: str
    password: str
    info: str


class CredentialModel(BaseModel):
    username: str
    password: str


class AccessTokenModel(BaseModel):
    token: str


class ProjectModel(BaseModel):
    project_id: int
    name: str
    description: str


class NewProjectModel(BaseModel):
    name: str
    description: str


class AccessToUsersModel(BaseModel):
    usernames: list


class FullTaskModel(BaseModel):
    task_id: int
    name: str
    description: str
    # attachments: list
    responsible: str


class TaskModel(BaseModel):
    task_id: int
    name: str
    # description: str
    # attachments: list
    responsible: str


class NewTaskModel(BaseModel):
    name: str
    # description: str
    # attachments: list
    responsible: str
