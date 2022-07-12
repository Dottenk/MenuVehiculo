import cx_Oracle


conn = cx_Oracle.connect(
    user='seccion_8_mdy',
    password='seccion_8_mdy',
    dsn= 'localhost:1521/XEPDB1'
)

c = conn.cursor()
c.execute('select * from detallefactura')
for row in c:
    print(list(row))