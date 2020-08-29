---- drop ----
DROP TABLE IF EXISTS `evaluation_items`;

---- create ----
create table IF not exists `evaluation_items`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `item`             VARCHAR(50) NOT NULL,
 `description`      VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;

INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("推薦妥当性", "あなたはこの本に興味がありますか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("インタフェース妥当性", "インタフェースは分かりやすいですか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("説明性", "このシステムは自身に本の推薦理由を説明してくれましたか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("情報充足性", "このシステムは自身が本の良し悪しを判断するのに十分な情報を提供してくれましたか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("制御性", "システム上で自身が行った操作に応じて推薦内容を変えてくれていると感じましたか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("知覚有用性", "システムを利用して、興味のある本に容易にたどり着けましたか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("総合満足度", "あなたは全体としてこのシステムに満足していますか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("システム信頼度", "このシステムはあなたにとって信頼できるものですか?");
INSERT INTO `evaluation_items`(`item`, `description`) VALUES ("システム利用意図", "あなたはこのシステムをまた利用したいと思えますか?");

---- drop ----
DROP TABLE IF EXISTS `evaluation_data`;

---- create ----
create table IF not exists `evaluation_data`
(
 `id`               INT(20) NOT NULL AUTO_INCREMENT,
 `user_id`          INT(20) NOT NULL REFERENCES users(id),
 `evaluation_id`    INT(20) NOT NULL REFERENCES evaluation_items(id),
 `evaluation`       INT(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE(`user_id`, `evaluation_id`)
) DEFAULT CHARSET=utf8;
