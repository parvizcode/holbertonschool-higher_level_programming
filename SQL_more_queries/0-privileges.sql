-- Kullanıcı kontrolü yapalım
SELECT IFNULL(
  (SELECT CONCAT('User user_0d_1@localhost exists. Privileges: ') FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'),
  'User user_0d_1@localhost does not exist'
) AS Status;

-- Sadece kullanıcı varsa yetkileri göster
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Aynısını user_0d_2 için yapalım
SELECT IFNULL(
  (SELECT CONCAT('User user_0d_2@localhost exists. Privileges: ') FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'),
  'User user_0d_2@localhost does not exist'
) AS Status;

SHOW GRANTS FOR 'user_0d_2'@'localhost';
