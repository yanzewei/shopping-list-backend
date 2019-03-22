# DATABASE DESIGN

## MySQL

### Category table
```
+----------------+----------+------+-----+---------+----------------+
| Field          | Type     | Null | Key | Default | Extra          |
+----------------+----------+------+-----+---------+----------------+
| id             | int(11)  | NO   | PRI | NULL    | auto_increment |
| name           | char(20) | NO   | UNI | NULL    |                |
| sub_table_name | char(50) | NO   | UNI | NULL    |                |
+----------------+----------+------+-----+---------+----------------+
name is the category name, like game machine, phone;
sub_table_name is the table name of the subcategory, like category_game_machine, category_mobilephone.
```

### category_game_machine
```
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| id            | int(11)       | NO   | PRI | NULL    | auto_increment |
| brand_id      | int(11)       | NO   |     | NULL    |                |
| disk          | int(11)       | YES  |     | NULL    |                |
| memory        | int(11)       | YES  |     | NULL    |                |
| color         | char(10)      | YES  |     | NULL    |                |
| joy_stick_num | int(11)       | YES  |     | NULL    |                |
| price         | decimal(10,2) | YES  |     | NULL    |                |
| add_time      | int(11)       | YES  |     | NULL    |                |
| remain_count  | int(11)       | NO   |     | NULL    |                |
+---------------+---------------+------+-----+---------+----------------+
brand_id is related with brand table's id;
remain_count is the product's stock.
```

### category_mobilephone
```
+--------------+---------------+------+-----+---------+----------------+
| Field        | Type          | Null | Key | Default | Extra          |
+--------------+---------------+------+-----+---------+----------------+
| id           | int(11)       | NO   | PRI | NULL    | auto_increment |
| brand_id     | int(11)       | NO   |     | NULL    |                |
| memory       | int(11)       | YES  |     | NULL    |                |
| color        | char(10)      | YES  |     | NULL    |                |
| price        | decimal(10,2) | YES  |     | NULL    |                |
| add_time     | int(11)       | YES  |     | NULL    |                |
| remain_count | int(11)       | NO   |     | NULL    |                |
+--------------+---------------+------+-----+---------+----------------+
brand_id is related with brand table's id;
remain_count is the product's stock.
```

### Brand table
```
+----------+---------------+------+-----+---------+----------------+
| Field    | Type          | Null | Key | Default | Extra          |
+----------+---------------+------+-----+---------+----------------+
| id       | int(11)       | NO   | PRI | NULL    | auto_increment |
| category | int(11)       | NO   | MUL | NULL    |                |
| name     | varchar(50)   | NO   | MUL | NULL    |                |
| logo     | varchar(1024) | NO   |     | NULL    |                |
+----------+---------------+------+-----+---------+----------------+
name is the brand name, like Apple, Google;
category is related to the table category's id.
```

### User table
```
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| email    | varchar(64)  | YES  | UNI | NULL    |                |
| username | varchar(64)  | YES  | UNI | NULL    |                |
| password | varchar(128) | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
Only one user now: '1', 'admin@gmail.com', 'admin', '*90DEE064FB0C1803C7A3264512EFA911FA2F9638';
All the shopping list is binded with user id = 1.
```

## Redis

### Used for storing the quantity of shopping cart.
```
Data type: hash;
Data structure: { shopping_nums_u1 : { "1-1" : 4, "2-3" : 5, "1-6" : 2 ...} };
In the key "shopping_nums_u1", "1" means user id;
In the pair ("1-1" : 4), "1-1" means category_id-sub_category_id, "4" means the according quantity.
```
