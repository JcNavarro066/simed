DROP TABLE tblUser;
DROP TABLE tblPatient;
DROP TABLE tblDoctor;
DROP TABLE tblReport;
DROP TABLE tbllogin;

CREATE TABLE tbllogin
(
	loginId  INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    email VARCHAR(100) NOT NULL,
    password VARCHAR(10) NOT NULL,
    PRIMARY KEY (loginId)
);


CREATE TABLE tblUser 
(
    idUser INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    f_name CHAR(30) NOT NULL,
    l_name CHAR(30) NOT NULL,
    dateOfBirth DATE NOT NULL,
    age CHAR(3) NOT NULL,
    gender CHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(4) NOT NULL,
    PRIMARY KEY (idUser)
);

CREATE TABLE tblPatient
(
    idPatient INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    civilState VARCHAR(10) NOT NULL,
    ocupation VARCHAR(30) NOT NULL,
    address VARCHAR(50) NOT NULL,
    PRIMARY KEY (idPatient)
);

CREATE TABLE tblDoctor
(
    idDoctor  INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    professionalRegister BIGINT NOT NULL,
    especialism VARCHAR(30) NOT NULL,
    PRIMARY KEY (idDoctor)
   
);

CREATE TABLE tblReport
(
    idReport INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) ,
    r_date DATE NOT NULL ,
    r_hour TIME NOT NULL ,
    symptoms CLOB,
    vital_signs CLOB,
    conclusions CLOB,
    orders CLOB,
    PRIMARY KEY (idReport)
);
