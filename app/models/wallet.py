from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

BaseWallet = declarative_base()

class wallet(BaseWallet):
    __tablename__ = "Transaction"
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    income = Column(Float, nullable=False)
    expense = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Expense(id={self.id},type={self.type}, category={self.category}, amount={self.amount},date={Date},description={self.description},wallet={self.walletId})"