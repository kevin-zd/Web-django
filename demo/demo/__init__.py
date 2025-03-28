# 让mysql以mysqlDB的方式来对接ORM
from pymysql import install_as_MySQLdb
install_as_MySQLdb()