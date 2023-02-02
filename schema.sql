-- -----------------------------------------------------
-- Schema djangoblog;
-- -----------------------------------------------------
/*borra schema si existeix*/
DROP SCHEMA IF EXISTS djangoblog;

CREATE SCHEMA IF NOT EXISTS djangoblog DEFAULT CHARACTER SET utf8mb4 ;
USE djangoblog ;

/*user*/
DROP USER IF EXISTS 'djangoblog'@'%';
CREATE USER 'djangoblog'@'%' IDENTIFIED BY '1234';

/*GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';*/

GRANT ALL PRIVILEGES ON djangoblog.* TO 'djangoblog'@'%' with grant option;
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'djangoblog'@'%';