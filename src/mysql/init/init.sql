CREATE TABLE IF NOT EXISTS mysql_database.node(
    id INT(8) AUTO_INCREMENT,
    dir_name VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id));

INSERT INTO mysql_database.node(dir_name, name) VALUES
    ('root', 'ルート'),
	('MobileSuit', 'モビルスーツ'),
	('Sanrio', 'サンリオ'),
	('Gundam', 'ガンダム'),
	('Dom', 'ドム'),
	('Zaku', 'ザク'),
	('RX78-2', 'RX78-2 ガンダム'),
	('Z', 'Zガンダム'),
	('NT-1', 'ガンダムNT-1'),
	('GP01', 'ガンダム試作1号機'),
	('GP02', 'ガンダム試作2号機'),
	('Unicorn', 'ユニコーンガンダム'),
	('Wing', 'ウイングガンダム'),
	('Freedom', 'フリーダムガンダム'),
	('Exia', 'ガンダムエクシア'),
	('BadBadtzMaru', 'バッドばつ丸'),
	('Cinnamoroll', 'シナモロール'),
	('HelloKitty', 'ハローキティ'),
	('KeroKeroKeroppi', 'けろけろけろっぴ'),
	('MyMelody', 'マイメロディ'),
	('Pompompurin', 'ポムポムプリン')
;

CREATE TABLE IF NOT EXISTS mysql_database.relation(
 id INT(8) NOT NULL,
 child_id INT(8) NOT NULL,
 distance INT(8) NOT NULL);

INSERT INTO mysql_database.relation(id, child_id, distance) VALUES
	(1, 1, 0), (1, 2, 1), (1, 3, 1), (1, 4, 2), (1, 5, 2), (1, 6, 2), (1, 7, 3),
	(1, 8, 3), (1, 9, 3), (1, 10, 3), (1, 11, 3), (1, 12, 3), (1, 13, 3), (1, 14, 3),
	(1, 15, 3), (1, 16, 2), (1, 17, 2), (1, 18, 2), (1, 19, 2), (1, 20, 2), (1, 21, 2),
	(2, 2, 0), (2, 4, 1), (2, 5, 1), (2, 6, 1), (2, 7, 2), (2, 8, 2), (2, 9, 2),
	(2, 10, 2), (2, 11, 2), (2, 12, 2), (2, 13, 2), (2, 14, 2), (2, 15, 2),
	(3, 3, 0), (3, 16, 1), (3, 17, 1), (3, 18, 1), (3, 19, 1), (3, 20, 1), (3, 21, 1),
	(4, 4, 0), (4, 7, 1), (4, 8, 1), (4, 9, 1), (4, 10, 1), (4, 11, 1), (4, 12, 1),
	(4, 13, 1), (4, 14, 1), (4, 15, 1),
	(5, 5, 0), (6, 6, 0), (7, 7, 0), (8, 8, 0), (9, 9, 0), (10, 10, 0), (11, 11, 0),
	(12, 12, 0), (13, 13, 0), (14, 14, 0), (15, 15, 0), (16, 16, 0), (17, 17, 0), (18, 18, 0),
	(19, 19, 0), (20, 20, 0), (21, 21, 0)
;