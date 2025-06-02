from app.database import init_db, insert_summary

init_db()
insert_summary("This is a test input.", "This is the summary.", tags="test,cli")
print("Database test passed!")

