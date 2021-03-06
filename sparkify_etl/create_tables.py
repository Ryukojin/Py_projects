import pymysql
#from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    Establishes database connection and return's the connection and cursor references.
    :return: return's (cur, conn) a cursor and connection reference
    """
    # connect to default database
    conn = pymysql.connect(host='127.0.0.1', 
                            user='root', 
                            password='red8Horse', 
                            database='sys', 
                            port=3306)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci")
    
    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = pymysql.connect(host='127.0.0.1', 
                            user='root', 
                            password='red8Horse', 
                            database='sparkifydb', 
                            port=3306, 
                            autocommit = True, 
                            local_infile = True)
    cur = conn.cursor()

    return cur,con

def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in drop_table_queries:
        cur.execute(query)


def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in create_table_queries:
        cur.execute(query)


def main():
    """
    Driver main function.
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    print("Table dropped successfully!!")

    create_tables(cur, conn)
    print("Table created successfully!!")

    conn.close()


if __name__ == "__main__":
    main()