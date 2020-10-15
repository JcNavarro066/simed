CREATE TABLE tblUser 
(
    idUser BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name CHAR(30) NOT NULL,
    lastName CHAR(30) NOT NULL,
    dateOfBirth DATE NOT NULL,
    age CHAR(3) NOT NULL,
    gender CHAR(3) NOT NULL,
    schoolGrade VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE tblPatient
(
    idPatient BIGINT NOT NULL PRIMARY KEY,
    civilState VARCHAR(10) NOT NULL,
    ocupation VARCHAR(30) NOT NULL,
    cellphone CHAR(10) NOT NULL,
    address VARCHAR(50) NOT NULL
);

CREATE TABLE tblDoctor
(
    idDoctor BIGINT NOT NULL PRIMARY KEY ,
    professionalRegister BIGINT NOt NULL
);
