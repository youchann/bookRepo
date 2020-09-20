---- drop ----
DROP TABLE IF EXISTS `users`;

---- create ----
create table IF not exists `users`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `student_number`   VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


---- drop ----
DROP TABLE IF EXISTS `search_words`;

---- create ----
create table IF not exists `search_words`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `word`             TEXT NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

---- drop ----
DROP TABLE IF EXISTS `selected_books`;

---- create ----
create table IF not exists `selected_books`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `user_id`          INT(20) NOT NULL REFERENCES users(id),
 `book_id`          INT(20) NOT NULL REFERENCES books(id),
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
