import sqlite3 as sql

def createDB():
    conn = sql.connect("Barberia.db")
    conn.commit()
    conn.close()

def createTables():

    conn = sql.connect("Barberia.db")
    cursor = conn.cursor()

    cursor.execute(
        """ CREATE TABLE clientes(
            telefono text primary key, 
            name text no null
        )"""
    )

    cursor.execute(
       """CREATE TABLE barberos(
            id bigint primary key generated always as identity,
            id_turno bigint references turno (id),
            name text not null,
            telefono int
       )""" 
    )

    cursor.execute(
        """CREATE TABLE turno(
            id bigint primary key generated always as identity,
            telefono_cliente text references clientes (telefono),
            barbero_id bigint references barberos (id),
            servicio_id bigint references servicio (id),
            fecha_Agenda bigint reference agenda (fecha),
            estado text default 'programado'
        )"""
    )
    
    cursor.execute(

        """CREATE TABLE Usuario(
            id bigint primary key generated always as identity,
            username text not null, 
            password text not null,
            role text not null 
         )"""
    )

    cursor.execute(
        """CREATE TABLE servicios(
            id bigint primary key generated always as identity,
            name text not null
            descripcion text 
            precio numeric(10,2) not null
        )"""
    )

    cursor.execute(
        """CREATE TABLE agenda(
            fecha date primary key, 
            id_turno bigint references turno (id),  
            hora_inicio time not null,
            hora_fin time not null
        )"""
    )

    cursor.execute(
        """CREATE TABLE productos(
            codigo bigint primary key generated always as identify,
            name text not null,
            precio numeric(10,2) not null,
            stock int not null
        )"""
    )

    cursor.execute(
        """CREATE TABLE ventas(
            fecha_venta date primary key,
            codigo_producto bigint references productos (codigo), 
            telefono_cliente text references cliente (telefono),
            cantidad int not null,
            ingreso_totales int not null
        )"""
    )

    cursor.execute(
        """CREATE TABLE proveedores(
            id bigint primary key generated always as identify,
            codigo_producto bigint references productos (codigo),
            name text not null,
            telefono text not null 
        )"""
    )

    cursor.execute(
        """CREATE TABLE ganancias(
            id_turno bigint references productos (id),
            fecha_venta date references productos (fecha_venta),
            fecha date not null,
            total int not null,
            tipo text not null

        )"""
    )

    cursor.execute(
        """CREATE TABLE compras(
            fecha_compra date primary key,
            codigo_producto bigint references productos (codigo),
            id_proveedor bigint references proovedores (id),
            cantidad int not null,
            costo_total numeric(10,2) not null
        )"""
    )

    cursor.execute(
        """CREATE TABLE widgets(
            fecha_agenda date references agenda (fecha),
            tipo_widget text not null,
            datos 
        )"""
    )