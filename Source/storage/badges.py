from typing import override
from . import _logic
import enum


class database(_logic.sqlite_connector_base):
    TABLE_NAME = "badges"

    class field(enum.Enum):
        USER_ID_NUM = '"user_id_num"'
        BADGE_ID = '"badge_id"'
        TIMESTAMP = '"timestamp"'

    @override
    def first_time_setup(self) -> None:
        self.sqlite.execute(
            f"""
            CREATE TABLE IF NOT EXISTS "{self.TABLE_NAME}" (
                {self.field.USER_ID_NUM.value} INTEGER NOT NULL,
                {self.field.BADGE_ID.value} INTEGER NOT NULL,
                {self.field.TIMESTAMP.value} DATETIME DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY(
                    {self.field.USER_ID_NUM.value},
                    {self.field.BADGE_ID.value}
                ) ON CONFLICT IGNORE
            );
            """,
        )

    def award(self, user_id_num: int, badge_id: int) -> None:
        self.sqlite.execute(
            f"""
            INSERT INTO "{self.TABLE_NAME}"
            (
                {self.field.USER_ID_NUM.value},
                {self.field.BADGE_ID.value}
            )
            VALUES (?, ?)
            """,
            (
                user_id_num,
                badge_id,
            ),
        )

    def check(self, user_id_num: int, badge_id: int) -> str | None:
        result = self.sqlite.fetch_results(self.sqlite.execute(
            f"""
            SELECT
            {self.field.TIMESTAMP.value}

            FROM "{self.TABLE_NAME}"
            WHERE {self.field.USER_ID_NUM.value} = {user_id_num}
            AND {self.field.BADGE_ID.value} = {badge_id}
            """,
        ))
        assert result is not None
        if len(result) > 0:
            return result[0]
        return None
