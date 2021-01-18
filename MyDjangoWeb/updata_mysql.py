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
    count = cursor.execute(sql,[username,psw])

    conn.commit()
    cursor.close()
    conn.close()
    if count == 1:
        print("用户信息inset成功！！！")
    else:
        print("insert 错误！！")

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

#填写用户个人信息
def inser_user_info(user_info):
    conn = conn_mysql()
    cursor = conn.cursor()
    name = user_info['name']
    age = user_info['age']
    sex = user_info['sex']
    hobby = user_info['hobby']
    city = user_info['city']
    addr = user_info['addr']
    sql = "INSERT INTO user_info (name,age,sex,hobby,city,addr) VALUES (%s,%s,%s,%s,%s,%s)"
    count = cursor.execute(sql,[name,age,sex,hobby,city,addr])
    conn.commit()
    cursor.close()
    conn.close()
    if count == 1:
        print("用户个人信息inser完成！！！")
        return True
    else:
        return False

#查询用户是否存在
def find_username(username):
    conn = conn_mysql()
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE (username = %s);"
    count = cursor.execute(sql,username)
    conn.commit()
    cursor.close()
    conn.close()
    if count == 1:
        return True
    else:
        return False


