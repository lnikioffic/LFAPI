from typing import Annotated, Any
from time import time
import secrets
import uuid
from fastapi import APIRouter, status, Depends, HTTPException, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix='/auth', tags=['Auth'])

security = HTTPBasic()

"""
Annotated используется для группировки несольких аннотаций
"""
@router.get('/basic-auth')
async def demo_basic_auth_cred(cred: Annotated[HTTPBasicCredentials, Depends(security)]):

    return {
        'message': 'Hi',
        'username': cred.username,
        'password': cred.password
    } 


username_passwd = {
    'admin': 'admin',
    'john': 'password'
}


def get_auth_username(cred: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid username or password',
        headers={'WWW-Authenticate': 'Basic'},
    )
    cor_pass = username_passwd.get(cred.username)
    if cor_pass is None:
        raise unauthed_exc
    
    if not secrets.compare_digest(
            cred.password.encode('utf-8'),
            cor_pass.encode('utf-8'),
        ):
        raise unauthed_exc
    
    return cred.username


@router.get('/basic-auth_username')
async def demo_basic_auth_username(auth_username: str = Depends(get_auth_username)):
    return {
        'message': 'Hi',
        'username': auth_username,
    } 


static_auth_token_username = {
    'a0787852e766b02e87f6dd15e4c3d1f1': 'admin',
    'a14f178e75dee69fa66ff3fad9db0daa': 'john'
}


def get_auth_username_token(token: str = Header(alias='auth-token')) -> str:
    if tk := static_auth_token_username.get(token):
        return tk
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Toke invalid',
        )


@router.get('/some-http-header-auth')
async def some_http_header_auth(username: str = Depends(get_auth_username_token)):
    return {
        'message': 'Hi',
        'username': username,
    } 


COOKIES: dict[str, dict[str, Any]] = {}
SESSION_COOKIE_KEY = 'web-app'


def gen_session_id() -> str:
    return uuid.uuid4().hex


@router.post('/login-cookie')
async def login_cookie_auth(response: Response, username: str = Depends(get_auth_username_token)):
    session_id = gen_session_id()
    COOKIES[session_id] = {
        'username': username,
        'time_login': int(time())
    }
    response.set_cookie(SESSION_COOKIE_KEY, session_id)
    return {'result': 'ok'}


def get_session_data(session_id: str = Cookie(alias=SESSION_COOKIE_KEY)):
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Cookie invalid',
        )
    
    return COOKIES[session_id]


@router.get('/check-cookie')
async def get_cookie(user_session_data: dict = Depends(get_session_data)):
    user = user_session_data['username']
    return {
            'username': user,
            **user_session_data
        }


@router.get('/logout-cookie')
async def logout_cookie(
        response: Response, 
        session_id: str = Cookie(alias=SESSION_COOKIE_KEY),
        user_session_data: dict = Depends(get_session_data)
    ):
    COOKIES.pop(session_id)
    response.delete_cookie(SESSION_COOKIE_KEY)
    user = user_session_data['username']
    return {
            'username': f'Buy {user}',
        }