

CREATE TABLE posts (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(30) NOT NULL,
content TEXT NOT NULL
);

INSERT INTO posts (title, content)
VALUES ("Заголовок 1", "content 1 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nulla, eius.");

INSERT INTO posts (title, content)
VALUES ("Заголовок 2", "content 2 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nulla, eius.");

INSERT INTO posts (title, content)
VALUES ("Заголовок 3", "content 3 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nulla, eius.");