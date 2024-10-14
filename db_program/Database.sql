create database sampledb;

use sampledb;

create table userinfo
(
	id int primary key auto_increment,
	username varchar(100) not null,
	password varchar(10) not null,
	emailaddress varchar(100) not null
);

insert into userinfo(username, password, emailaddress) values('Suresh','test@123', 'suresh@gmail.com');
