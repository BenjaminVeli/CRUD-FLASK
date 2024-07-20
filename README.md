### CRUD FLASK

### DATABASE MySQL :

```sh
CREATE DATABASE estudiante;

USE estudiante;

CREATE TABLE estudiante (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono INT(9),
    apellido VARCHAR(100),
    edad INT,
    carrera VARCHAR(100),
    pais VARCHAR(100)
);

