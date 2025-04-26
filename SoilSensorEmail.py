#!/usr/bin/env python3
# Program Title: Soil Sensor Email
# Description: Check soil moisture 4 times a day (3 h interval) and email the result
# Author / Student: Siyuan Qin  
# ID: 202283890023
# Date: 26/4/2025

import smtplib
import time
from datetime import datetime
from email.message import EmailMessage
from gpiozero import Button

# －－－－－－User Configurable Area－－－－－－
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT   = 587                    
FROM_EMAIL  = "3072836362@qq.com"
FROM_PASS   = "hytbvsttqribdchg"
TO_EMAIL    = "2074474233@qq.com"

GPIO_CHANNEL   = 4                  
TOTAL_READINGS = 4                   
INTERVAL_SEC   = 2 * 60 * 60         
# －－－－－－－－－－－－－－－－－－－－－－－

sensor = Button(GPIO_CHANNEL)


def read_soil_status() -> tuple[str, str]:
    
    if sensor.is_pressed:
        return ("Water NOT needed", "Soil is moist. No need to water the plant.")
    else:
        return ("Please water your plant", "Soil is dry. Please water your plant.")


def send_email(reading_no: int, status: str, body: str) -> None:
    msg = EmailMessage()
    msg.set_content(f"#{reading_no}: {body}")
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = f"Plant Status #{reading_no} – {status}"

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            server.starttls()
            server.login(FROM_EMAIL, FROM_PASS)
            server.send_message(msg)
        print(f"[{datetime.now():%H:%M:%S}] Email #{reading_no} sent: {status}")
    except Exception as e:
        print(f"[{datetime.now():%H:%M:%S}] Failed to send email #{reading_no}: {e}")


if __name__ == "__main__":
    print("SoilSensorEmail started …")
    for i in range(1, TOTAL_READINGS + 1):
        print(f"\n--- Reading #{i} ---")
        status, body = read_soil_status()
        print(f"Status: {status}")
        send_email(i, status, body)

        if i < TOTAL_READINGS:
            print(f"Waiting {INTERVAL_SEC//3600} hours before next reading…")
            time.sleep(INTERVAL_SEC)

    print("\nAll readings completed. Script finished.")
