CREATE TABLE `cloud_service_cpsc449`.`user` (
    `id` INT NOT NULL AUTO_INCREMENT , 
    `username` VARCHAR(100) NOT NULL , 
    `role` VARCHAR(16) NULL , 
    `subscription_plan_id` INT, 
    PRIMARY KEY (`id`), 
    UNIQUE (`username`)
    );

CREATE TABLE `cloud_service_cpsc449`.`subscription_plan` (
    `id` INT NOT NULL AUTO_INCREMENT , 
    `name` VARCHAR(100) NOT NULL , 
    `description` TEXT NULL , 
    `permissions` JSON NULL , 
    `usage_limits` JSON NULL , 
    PRIMARY KEY (`id`), 
    UNIQUE (`name`)
    );

CREATE TABLE `cloud_service_cpsc449`.`permission` (
    `id` INT NOT NULL AUTO_INCREMENT , 
    `name` VARCHAR(100) NOT NULL , 
    `endpoint` VARCHAR(100) NULL , 
    `description` TEXT NULL , 
    PRIMARY KEY (`id`), 
    UNIQUE (`name`)
    );
