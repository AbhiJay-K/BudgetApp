from sqlalchemy import create_engine
from app.models.Transaction import BaseTransaction
from app.models.wallet import BaseWallet
from sqlalchemy.orm import sessionmaker


class database():

    DATABASE_URL = "sqlite:///./db/budget.db"

    engine = create_engine(DATABASE_URL,echo=True)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    def __init__(self):
        pass

    def init_db(self):
        BaseTransaction.metadata.create_all(bind=self.engine)
        BaseWallet.metadata.create_all(bind=self.engine)
