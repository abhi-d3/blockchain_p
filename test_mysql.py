import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="ashwath",  # replace this
        db="EHR"                # replace if your DB name is different
    )
    print("✅ Connection successful!")
    db.close()
except MySQLdb.OperationalError as e:
    print("❌ Connection failed:", e)
