-- ---- drop ----
-- DROP TABLE IF EXISTS `test_table`;
-- --
-- -- ---- create ----
-- -- create table IF not exists `test_table`
-- -- (
-- --  `id`               INT(20) AUTO_INCREMENT,
-- --  `name`             VARCHAR(20) NOT NULL,
-- --  `created_at`       Datetime DEFAULT NULL,
-- --  `updated_at`       Datetime DEFAULT NULL,
-- --     PRIMARY KEY (`id`)
-- ) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

---- drop ----
DROP TABLE IF EXISTS `genres`;

---- create ----
-- create table IF not exists `genres`
-- (
--  `id`               INT(20) AUTO_INCREMENT,
--  `name`             VARCHAR(100) NOT NULL,
--   PRIMARY KEY (`id`)
-- ) DEFAULT CHARSET=utf8;



---- drop ----
DROP TABLE IF EXISTS `books`;

---- create ----
create table IF not exists `books`
(
 `id`               INT(15) NOT NULL,
 `isbn`             INT(13) NOT NULL,
 `name`             VARCHAR(100) NOT NULL,
 `business_flg`     BOOLEAN NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;



---- drop ----
DROP TABLE IF EXISTS `book_genres`;
---- drop ----
DROP TABLE IF EXISTS `topic_terms`;

---- create ----
-- create table IF not exists `book_genres`
-- (
--  `id`               INT(20) AUTO_INCREMENT,
--  `book_id`          INT(15) NOT NULL REFERENCES books(book_id),
--  `genre_id`         INT(20) NOT NULL REFERENCES genres(id),
--   PRIMARY KEY (`id`)
-- ) DEFAULT CHARSET=utf8;



---- drop ----
DROP TABLE IF EXISTS `topics`;

---- create ----
create table IF not exists `topics`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `book_id`          INT(15) NOT NULL REFERENCES books(book_id),
 `adjective_flg`    BOOLEAN NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;



---- drop ----
DROP TABLE IF EXISTS `words`;

---- create ----
create table IF not exists `words`
(
 `id`               INT(20) NOT NULL,
 `word`             VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


---- drop ----
DROP TABLE IF EXISTS `topic_words`;

---- create ----
create table IF not exists `topic_words`
(
 `id`               INT(20) NOT NULL,
 `topic_id`         INT(20) NOT NULL REFERENCES topics(id),
 `word_id`          INT(20) NOT NULL REFERENCES words(id),
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
