#consulta os comentários

SELECT com_author_name, com_comment,
DATE_FORMAT(com_date, '%%d/%%m/%%Y às %%H:%%i) AS com_datebr
FROM comment
WHERE com_article = '5'
AND com_status = 'on'
ORDER BY com_date DESC;
