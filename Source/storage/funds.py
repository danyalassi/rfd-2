from typing import override
from . import _logic
import enum


class database(_logic.sqlite_connector_base):
    TABLE_NAME = "funds"

    class field(enum.Enum):
        USER_ID_NUM = '"user_id_num"'
        FUNDS = '"funds"'

    @override
    def first_time_setup(self) -> None:
        self.sqlite.execute(
            f"""
            CREATE TABLE IF NOT EXISTS "{self.TABLE_NAME}" (
                {self.field.USER_ID_NUM.value} INTEGER NOT NULL,
                {self.field.FUNDS.value} INTEGER NOT NULL,
                PRIMARY KEY(
                    {self.field.USER_ID_NUM.value}
                ) ON CONFLICT IGNORE
            );
            """,
        )

    def add(self, user_id_num: int, delta: int) -> None:
        self.sqlite.execute(
            f"""
            UPDATE "{self.TABLE_NAME}"
            SET {self.field.FUNDS.value} = {self.field.FUNDS.value} + {delta}
            WHERE {self.field.USER_ID_NUM.value} = {user_id_num}
            """
        )

    def first_init(self, user_id_num: int, value: int) -> None:
        self.sqlite.execute(
            f"""
            INSERT INTO "{self.TABLE_NAME}"
            VALUES (?, ?)
            """,
            (
                user_id_num,
                value,
            ),
        )

    def set(self, user_id_num: int, value: int) -> None:
        self.sqlite.execute(
            f"""
            UPDATE "{self.TABLE_NAME}"
            SET {self.field.FUNDS.value} = {value}
            WHERE {self.field.USER_ID_NUM.value} = {user_id_num}
            """
        )

    def check(self, user_id_num: int) -> int | None:
        result = self.sqlite.fetch_results(self.sqlite.execute(
            f"""
            SELECT
            {self.field.FUNDS.value}

            FROM "{self.TABLE_NAME}"
            WHERE {self.field.USER_ID_NUM.value} = {user_id_num}
            """,
        ))
        assert result is not None
        if len(result) > 0:
            return result[0]
        return None
