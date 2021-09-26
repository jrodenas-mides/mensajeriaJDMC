from fastapi import status, HTTPException
import psycopg2
from .conexion import credenciales

def crear_conexion():
    try:
        str_conexion = "host={server} dbname={database} port={puerto} user={usuario} password={password}"
        conn = psycopg2.connect(str_conexion.format(**credenciales))
        return conn
    except:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail= "exception:invalid.connection" )

def query_all(con, sql_query: str):
    try:
        cur = con.cursor()
        cur.execute(sql_query)
        results = cur.fetchall()
        cur.close()
        return results
    except:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "exception:invalid.query")


def query_one(con, sql_query: str):
    try:
        cur = con.cursor()
        cur.execute(sql_query)
        result = cur.fetchone()
        cur.close()
        return result[0]
    except Exception as exc:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "exception:invalid.query")


def insert_one(con, sql_query: str, data: dict = None, post_sql_query: str = None):
    try:
        cur = con.cursor()
        cur.execute(sql_query.format(**data))
        con.commit()
        cur.close()
        return query_one(con, post_sql_query) if post_sql_query is not None else True
    except:
        con.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="exception:invalid.insert")


def count_rows(con, table_name: str, indexed_column_name: str = '*'):
    toReturn = query_one(con, f"SELECT COUNT({indexed_column_name}) FROM {table_name}")
    return int(toReturn)

def update_one(con, sql_query: str, data: dict = None, post_sql_query: str = None):
    try:
        cur = con.cursor()
        cur.execute(sql_query.format(**data))
        con.commit()
        cur.close()
        return query_one(con, post_sql_query) if post_sql_query is not None else True
    except:
        con.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="exception:invalid.updated")
