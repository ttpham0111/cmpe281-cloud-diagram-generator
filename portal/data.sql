CREATE TABLE users (
  id       INT(11)      NOT NULL AUTO_INCREMENT,
  user_id  VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,

  PRIMARY KEY (id),
  UNIQUE KEY user_id (user_id)
);

INSERT INTO users (user_id, password) VALUES
  ('tenant_1', '$2b$12$/VRaDHc1M/Fviw7hEH08oOlH/JX0e1rAP2FkoKpOK.P/iuj7kw9xa'),
  ('tenant_2', '$2b$12$RkqyKpOhxuRslqvf53tSHu4iPeTc4pns2G78uvT9le2brZVe6R6GG'),
  ('tenant_3', '$2b$12$JN6bCXqMVYJrqEkT1E2Hqew3XeMk41CizL4Iej9FdedLFsUL21vyO'),
  ('tenant_4', '$2b$12$cTacWmzTYtFY91pWGOTFuu.uHRAFjtsGli7oDO6wt3j0O9aVIzgw6');