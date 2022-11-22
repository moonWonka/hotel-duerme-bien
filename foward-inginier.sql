-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotel duerme bienk
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel duerme bienk
-- -----------------------------------------------------


CREATE SCHEMA IF NOT EXISTS `hotel duerme bienk` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_mysql500_ci ;
USE `hotel duerme bienk` ;

-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`administradores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`administradores` (
  `adm_id` INT NOT NULL,
  `adm_user` VARCHAR(45) NOT NULL,
  `pass` INT NOT NULL,
  PRIMARY KEY (`adm_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`clientes` (
  `cli_id` INT NOT NULL,
  `cli_rut` VARCHAR(45) NOT NULL,
  `cli_nombre` VARCHAR(45) NOT NULL,
  `cli_apellidoP` VARCHAR(45) NOT NULL,
  `cli_apellidoM` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cli_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`habitaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`habitaciones` (
  `hab_id` INT NOT NULL,
  `hab_numero-hab` VARCHAR(45) NOT NULL,
  `hab_ubicacion` VARCHAR(45) NOT NULL,
  `hab_capacidad` INT NOT NULL,
  `hab_tipo` VARCHAR(45) NOT NULL,
  `hab_costo` INT NOT NULL,
  PRIMARY KEY (`hab_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`encargados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`encargados` (
  `enc_id` INT NOT NULL,
  `enc_user` VARCHAR(45) NOT NULL,
  `enc_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`enc_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`detalles de reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`detalles de reserva` (
  `det_id` INT NOT NULL,
  `hab_id` INT NOT NULL,
  `cli_id` INT NOT NULL,
  `enc_id` INT NOT NULL,
  `det_fecha-reserva` VARCHAR(45) NOT NULL,
  `det_fecha-inicio` VARCHAR(45) NOT NULL,
  `det_fecha-fin` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`det_id`),
  INDEX `fk_detalles de reserva_habitaciones_idx` (`hab_id` ASC) VISIBLE,
  INDEX `fk_detalles de reserva_clientes1_idx` (`cli_id` ASC) VISIBLE,
  INDEX `enc_id_idx` (`enc_id` ASC) VISIBLE,
  CONSTRAINT `hab_id`
    FOREIGN KEY (`hab_id`)
    REFERENCES `hotel duerme bienk`.`habitaciones` (`hab_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `cli_id`
    FOREIGN KEY (`cli_id`)
    REFERENCES `hotel duerme bienk`.`clientes` (`cli_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `enc_id`
    FOREIGN KEY (`enc_id`)
    REFERENCES `hotel duerme bienk`.`encargados` (`enc_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


-- -----------------------------------------------------
-- Table `hotel duerme bienk`.`huespedes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel duerme bienk`.`huespedes` (
  `idhuespedes` INT NOT NULL,
  `cli_id` INT NOT NULL,
  `det_id` INT NOT NULL,
  PRIMARY KEY (`idhuespedes`),
  INDEX `cli_id_idx` (`cli_id` ASC) VISIBLE,
  INDEX `det_id_idx` (`det_id` ASC) VISIBLE,
  CONSTRAINT `cli_id`
    FOREIGN KEY (`cli_id`)
    REFERENCES `hotel duerme bienk`.`clientes` (`cli_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `det_id`
    FOREIGN KEY (`det_id`)
    REFERENCES `hotel duerme bienk`.`detalles de reserva` (`det_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_mysql500_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
