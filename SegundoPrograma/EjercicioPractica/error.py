import pyodbc  #Esto es para trabajar con SQL

server = 'localhost'
bd = 'TestTB'
user = 'soporte'
password = '123'

try:
    conexion = pyodbc.connect('DRIVER={OBDC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='
                              +user+';PWD'+password)
    print('conexion exitosa')

except:
    print("Erro al intentar conectarse")