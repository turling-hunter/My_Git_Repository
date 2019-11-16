# test connection mysql by python
# admin：Turling
# import pymysql module
import pymysql

# connect database
conn = pymysql.connect(host='localhost', user='root', password='root', database='machine_data', charset='utf8')

# print connection message
print(str(conn) + "connect successfully!")

# get a cursor object that can execute SQL sentences
cursor = conn.cursor()

# create table

sql = "CREATE TABLE data_2019_8_27_16_42_21_20ms ("\
      "id INT(10) PRIMARY KEY ," \
      "c_prop CHAR(10) NOT NULL," \
      "power_avg CHAR(10) NOT NULL," \
      "p_pump1 CHAR(10) NOT NULL," \
      "p_pump2 CHAR(10) NOT NULL," \
      "flow1 CHAR(10) NOT NULL," \
      "flow2 CHAR(10) NOT NULL," \
      "pwm_prop CHAR(5) NOT NULL," \
      "power1 CHAR(10) NOT NULL," \
      "power2 CHAR(10) NOT NULL," \
      "res_prop CHAR(10) NOT NULL," \
      "torque1	CHAR(10) NOT NULL," \
      "torque2	CHAR(10) NOT NULL, " \
      "fuel_all CHAR(10) NOT NULL," \
      "load1939 CHAR(10) NOT NULL," \
      "demand_t CHAR(10) NOT NULL," \
      "rpm_set CHAR(10) NOT NULL," \
      "rpm_real CHAR(10) NOT NULL," \
      "fuelrate CHAR(10) NOT NULL," \
      "loserate CHAR(20) NOT NULL" \
      ")ENGINE=innodb DEFAULT CHARSET=utf8;"

# print create successfully
print("create table successfully!")

# execute this SQL sentence
cursor.execute(sql)

# close cursor
cursor.close()

# close database connection
conn.close()
