from flask_mysqldb import MySQLdb

def save_comment(mysql, form):

    sql = '''
        INSERT INTO comment (
            com_article,
            com_author_name,
            com_author_email,
            com_comment
        ) VALUES (
            %s,
            %s,
            %s,
            %s
        )
    '''
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, (
        form['name'],
        form['email'],
        form['subject'],
        form['message'],
    ))
    mysql.connection.commit()
    cur.close()

    return True