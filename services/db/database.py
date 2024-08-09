import asyncpg
from datetime import datetime, timedelta
from typing import Optional, Iterable

from .models import User, SubscribeChannel, Exchange

class ConnectionsFactory:
    """ This class creates connection to the db and returns it. """
    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    async def create(self) -> asyncpg.Connection:
        """ Creates database connection and returns it. """
        conn = await asyncpg.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return conn

class DatabaseController:
    """ Class with the all methods to working with db. """
    def __init__(self, connection):
        self._conn = connection

    async def create_db(self) -> None:
        await self._conn.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id bigint,
        username varchar,
        subscribe int DEFAULT 0,
        date_subscribe TIMESTAMP 
        )""")

    async def add_user(self, user_id: int, username: str) -> None:
        await self._conn.execute("INSERT INTO users VALUES ($1, $2)", user_id, username)

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        resp = await self._conn.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        res = None if not resp else User(user_id=resp.get("user_id"), username=resp.get("username"))
        return res

    async def get_all_users(self) -> Optional[Iterable[User]]:
        resp = await self._conn.fetch("SELECT * FROM users WHERE subscribe > 0")
        res = None if not resp else [User(user_id=u.get("user_id"), username=u.get("username")) for u in resp]
        return res

    async def disconnect(self) -> None:
        await self._conn.close()

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE