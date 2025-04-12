from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

BaseTransaction = declarative_base()

class Transaction(BaseTransaction):
    __tablename__ = "Transaction"
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    walletId = Column(String, nullable=False)

    def __repr__(self):
        return f"<Expense(id={self.id},type={self.type}, category={self.category}, amount={self.amount},date={Date},description={self.description},wallet={self.walletId})"