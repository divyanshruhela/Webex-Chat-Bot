#import required libararies
import cx_Oracle
from webexteamssdk import WebexTeamsAPI
import csv
import time

#WebEx Bot token
webex_token = ""

#room id of the webex space
room_id = ""

#Sql Query to fetch the data
oracle_query = ""

api = WebexTeamsAPI(webex_token)


def run_script():
    count = 0
    #Fill the host port and service name
    dsn_tns = cx_Oracle.makedsn(
        "Host", "Port", service_name="service name"
    )
    #Fill the Usernanem and password of the oracle database you want to connect
    conn = cx_Oracle.connect(user="", password="", dsn=dsn_tns)
    cur = conn.cursor()
    cur.execute(oracle_query)
    result = cur.fetchall()
    with open("CGI_ERROR_REPORT.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Column1",
                "Column2",
            ]
        )
        for row in result:
            writer.writerow(row)
          #Give the name of report
    with open("REPORT.csv", "rb") as file:
        api.messages.create(
            roomId=room_id,
            files=["REPORT.csv"],
            text=f"REPORT, NUMBER OF ROWS:{count} ",
        )


def main():
    while True:
        run_script()
        time.sleep(300)


if __name__ == "__main__":
    main()
