import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-RQUEMQT;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
#CREATE
def create(VendasId, NomeProduto, Valor):
    #We wrote f and {} for formatting reasons, taking data from python to DB.
    command = f"INSERT INTO Test.Vendas VALUES ({VendasId}, '{NomeProduto}', {Valor})"
    cursor.execute(command)
    print("The product was inserted.")
    conn.commit() #Run whenever the database is modified.

#READ
def read():
    cursor.execute("SELECT * FROM Test.Vendas")
    result = cursor.fetchall() #Run whenever the database is queried.
    print("Result: "+result)

#UPDATE:
def update(Valor, NomeProduto):
    command = f"UPDATE Test.Vendas SET Valor = {Valor} WHERE NomeProduto = '{NomeProduto}'"
    cursor.execute(command)
    print("Product updated.")
    conn.commit()

#DELETE
def delete(NomeProduto):
    command = f"DELETE FROM Test.Vendas WHERE NomeProduto = '{NomeProduto}'"
    cursor.execute(command)
    conn.commit()


cursor.close()
conn.close()

# create(4, 'Oleo', 7)
# read()
# update(1, 'Waffer')
# delete('Waffer')