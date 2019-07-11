-- ALTER TABLE `users` DROP COLUMN `nam。e`;

ALTER TABLE `users` MODIFY `id` INT(20) NOT NULL;

ALTER TABLE `search_words` DROP COLUMN `user_id`;
