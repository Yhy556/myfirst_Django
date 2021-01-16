# _*_ config = utf8 _*_
import pymysql

def conn_mysql():
    host = ""
    user = ""
    psw = ""
    db = ""

    conn = pymysql.connect(
        host = "172.24.2.91",
        user = "root",
        password = "Luo*zhen1234",
        database  = "test01",
        charset = "utf8"
    )
    return conn
#插入数据库
def inser_user_data(username,psw):
    conn = conn_mysql()
    #获取游标
    cursor = conn.cursor()
    sql = "INSERT INTO user (username,password) VALUES (%s, %s);"
    cursor.execute(sql,[username,psw])
    print("用户信息inset成功！！！")
    conn.commit()
    cursor.close()
    conn.close()

#数据库查询
def sel_user_data(username,psd):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE (username = %s) AND (password = %s);"
    num = cursor.execute(sql,[username,psd])
    conn.commit()
    cursor.close()
    conn.close()
    if num == 1:
        return True
    else:
        return False


