
import pandas as pd
import sqlalchemy as alch
from getpass import getpass

# password = getpass("Introduce tu contraseña del server mysql")

password = "admin"
db_name = "publications"
conec = f"mysql+pymysql://root:{password}@localhost/{db_name}"

engine = alch.create_engine(conec)



# Función Meter mensaje

def text_gr_usu(texto, gr_id, usu_id):
    engine.execute(
        f"""
        
        INSERT INTO mensajes (texto, gr_id, usu_id)  VALUES
        ("{texto}", {gr_id}, {usu_id}); 
        
    
        """
    )


# Creates a user 


def create_user(usu_name):
    engine.execute(
        f"""
       
        INSERT INTO usuarios (usu_name)
        VALUES ('{usu_name}');
        
        """
    )


# Creates a chat 
#(POST) /chat/<chat_id>


def create_group(gr_name):
    engine.execute(
        f"""
       
        INSERT INTO grupos (gr_name) VALUES
        ('{gr_name}');
        """
           )






    
#  Función adds a user to a chat. 


def create_conexion(gr_id, usu_id ):
    engine.execute(
        f"""
       
        INSERT INTO conexion (gr_id, usu_id) VALUES
        ({gr_id}, {usu_id});
        """
    )
    
    
