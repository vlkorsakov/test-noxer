from sqlalchemy import BigInteger, Column, MetaData, Table

metadata = MetaData(
    naming_convention={
        "ix": "ix__%(column_0_label)s",
        "uq": "uq__%(table_name)s__%(column_0_name)s",
        "ck": "ck__%(table_name)s__%(constraint_name)s",
        "fk": "%(table_name)s_%(column_0_name)s_fkey",
        "pk": "pk__%(table_name)s",
    },
)

user_table = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True),
)
