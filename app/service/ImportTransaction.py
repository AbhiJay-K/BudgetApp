import csv
import argparse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import datetime
import app.models
from app.models.Transaction import Transaction
import uuid
from app.utils.database import database
import hashlib

class ImportTrnsaction():

    def __init__(self):
        pass

    def readCSV(self, filename):
        with open(filename,newline='') as transactionstatement:
            reader = csv.reader(transactionstatement)
            db = database.SessionLocal()
            try:
                for row in reader:
                    print(row)
                    if row[0] != 'Date':
                        hash_object = hashlib.sha256(str(row).encode())
                        hex_digest = hash_object.hexdigest()
                        txn =  Transaction(
                            id=str(hex_digest),
                            date=datetime.strptime(row[0], "%m/%d/%Y").date(), 
                            type="",
                            category = "",
                            amount = float(row[2]),
                            description = str(row[1]),
                            walletId = ""
                        )
                       
                        db.add(txn)
                        db.commit()
                        db.refresh(txn)
            except IntegrityError as e:
                db.rollback()
                print("Integrity error:", e.orig)
            except SQLAlchemyError as e:
                db.rollback()
                print("SQLAlchemy error:", e)
            finally:
                db.close()
                print(txn)
                db.close()
    