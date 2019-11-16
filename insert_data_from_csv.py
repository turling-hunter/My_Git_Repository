# import pymysql module
import pymysql

def connect_database():
    try:
        # connect database
        conn = pymysql.connect(host='localhost', user='root', password='root', database='machine_data', charset='utf8')
        # print connection message
        print(str(conn) + "connect successfully!")

        # return successful collection
        return conn
    except Exception as e:
        # print error message
        print(e)

# get database connection
conn = connect_database()

# get a cursor object that can execute SQL sentences
cursor = conn.cursor()

# insert sql sentences
sql = "INSERT INTO data_2019_8_27_16_42_21_20ms(id,c_prop,power_avg,p_pump1,p_pump2," \
      "flow1,flow2,pwm_prop,power1,power2,res_prop,torque1,torque2,fuel_all,load1939," \
      "demand_t,t,rpm_set,rpm_real,fuelrate,duty_tor,acc_loose_tor,grade_x,loserate) " \
      "Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

# save csv row data
rows = []

# open csv file
with open("./data/2019.8.27.16.42.21.20ms.csv", 'r') as csv_file:

    # get row data without csv head
    lines =csv_file.readlines()[1:]
    for line in lines:
        # row data change into list without enter
        temp = line.strip('\n').split(',')[:-1]
        rows.append(temp)
csv_file.close()

for row in rows:
    # insert data with rollback
    try:
        # execute this SQL sentence
        cursor.execute(sql, row)
        # commit transaction
        conn.commit()
        # print successful message
        print("insert successfully!")
    except Exception as e:
        # rollback if having exception
        conn.rollback()
        # print error message
        print(e)

# close cursor
cursor.close()

# close database connection
conn.close()
