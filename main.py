from app.service.ImportTransaction import ImportTrnsaction
from app.utils.database import database
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <csv_file_path>")
    sys.exit(1)

csv_file = str(sys.argv[1])
print(csv_file)
db = database()
db.init_db()
readStatement = ImportTrnsaction()
readStatement.readCSV(csv_file)
