""" import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Exemplo: Apagar uma linha com id igual a 10
cursor.execute("DELETE FROM doctors_openagenda WHERE id = 13")
cursor.execute("DELETE FROM doctors_openagenda WHERE id = 12")
cursor.execute("DELETE FROM doctors_openagenda WHERE id = 11")
# Salvar as alterações
conn.commit()

# Fechar a conexão
conn.close() """
