
import pandas as pd
import sqlalchemy as alch
from getpass import getpass

# password = getpass("Introduce tu contraseña del server mysql")

password = "admin"
db_name = "publications"
conec = f"mysql+pymysql://root:{password}@localhost/{db_name}"

engine = alch.create_engine(conec)



# Funcion para obtener todos los usuarios + id

def get_usu():
    query = f""" SELECT usu_id, usu_name
FROM usuarios

"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")



# Funcion para obtener todos los grupos + id


def get_group():
    query = f""" SELECT gr_id, gr_name
FROM grupos

"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")




# Funcion para obtener todos los mensajes de un grupo


def get_men_gr_id(gr_id):
    query = f""" SELECT texto, usu_id
FROM mensajes
WHERE gr_id = "{gr_id}"

"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")
   




# Función para obtener los mensajes enviados de un usuario por id 


def get_men_usu_id(usu_id):
    query = f""" SELECT texto, usu_id
FROM mensajes
WHERE usu_id = "{usu_id}"

"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")
    


# FUNCIONES PARA GET ID  - SEGURAMENTE SEA NECESARIO ACUDIR AL JUPYTER 

# Si usuario no sabe el id de su grupo pero si su nombre

def get_id_from_grname(gr_name):
    
    halo = pd.read_sql_query(
    f"""
    SELECT gr_id 
    FROM grupos
    WHERE gr_name = "{gr_name}"; 
    """, engine )
    
    gr_name_id = halo["gr_id"].tolist()
    return gr_name_id


# Si usuario no sabe su id pero si su nombre

def get_id_from_usuname(usu_name):
    
    halo = pd.read_sql_query(
    f"""
    SELECT usu_id 
    FROM usuarios
    WHERE usu_name = "{usu_name}"; 
    """, engine )
    
    usu_name_id = halo["usu_id"].tolist()
    
    return usu_name_id

# Saber id último usuario registrado


def get_lastid_usu():
    halo = pd.read_sql_query(
    f"""
    SELECT MAX(usu_id) FROM usuarios; 
    """, engine )
    last_id = halo["MAX(usu_id)"].tolist()
    return last_id

# Saber id último grupo registrado

def get_lastid_group():
    halo = pd.read_sql_query(
    f"""
    SELECT MAX(gr_id) FROM grupos; 
    """, engine )
    last_id = halo["MAX(gr_id)"].tolist()
    return last_id
