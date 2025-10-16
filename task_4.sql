-- task_4.sql
-- Print the full description of the table 'books' from the database 'alx_book_store'


SELECT TABLE_NAME,
COLUMN_NAME,
DATA_TYPE,
IS_NULLABLE,
COLUMN_DEFAULT,
COLUMN_KEY,
EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;