CREATE TABLE IF NOT EXISTS users (
  id       INT(11)      NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  url      VARCHAR(255) NOT NULL,
  mode     VARCHAR(10)  NOT NULL,

  PRIMARY KEY (id),
  UNIQUE KEY username (username)
);

CREATE TABLE IF NOT EXISTS fields (
  id      INT(11)     NOT NULL AUTO_INCREMENT,
  user_id INT(11)     NOT NULL,
  name    VARCHAR(80) NOT NULL,
  type    VARCHAR(80) NOT NULL,
  value   VARCHAR(80) NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);