use datos;
create table clientes(
id int auto_increment primary key, 
nombre varchar(50) not null,
correo varchar(100) unique
);

create table pais(
id int auto_increment primary key,
nombre_pais varchar(50) not null,
abreviatura varchar(10) null, 
codigo_postal int(5) unique,
descripcion varchar(100) null
);

create table usuario(
id int auto_increment primary key,
nombre_usuario varchar(50) not null,
contraseña varchar(25) not null
);

create table genero(
id int auto_increment primary key,
nombre varchar(25) unique,
descripcion varchar(25) unique,
abreviatura varchar(10) not null
);

create table roles(
id int auto_increment primary key,
abreviatura varchar(10) not null,
nombre varchar(50) not null,
descripcion varchar(25) not null
);

create table factura(
id int auto_increment primary key,
descripcion varchar(255) not null,
cantidad varchar(10) not null,
precio float(10) unique,
total varchar(50) not null
);

create table empleados(
id int auto_increment primary key,
nombre varchar(100) unique,
apellidos varchar(100) unique,
telefono varchar(25) not null,
turno varchar(15) null,
puesto varchar(50) not null,
salario varchar(100) not null
);

create table proveedores(
id int auto_increment primary key,
nombre_proveedor varchar(100) not null,
decripcion varchar(255) not null,
contacto varchar(25) unique,
correo varchar(100) not null,
pais varchar(100) not null
);

