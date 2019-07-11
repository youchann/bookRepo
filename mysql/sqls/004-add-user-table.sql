---- drop ----
DROP TABLE IF EXISTS `users`;

---- create ----
create table IF not exists `users`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `name`             VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


---- drop ----
DROP TABLE IF EXISTS `search_words`;

---- create ----
create table IF not exists `search_words`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `user_id`          INT(20) NOT NULL REFERENCES users(id),
 `word`             VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
