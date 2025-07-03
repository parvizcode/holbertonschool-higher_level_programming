-- Kullanıcı varsa silmeden oluşturmak için IF NOT EXISTS kullanacağız
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Tüm yetkileri verme
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Yetkilerin geçerli olması için
FLUSH PRIVILEGES;
