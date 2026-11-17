from database import get_connection

conn = get_connection()
for u in conn.execute("SELECT id, name, email, role, password FROM users"):
    print(u["id"], u["name"], u["email"], u["role"], u["password"][:25] + "...")
conn.close()