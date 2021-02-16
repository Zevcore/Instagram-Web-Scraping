from selenium import webdriver
from scripts import bot

driver = webdriver.Firefox()

bot = bot.Bot(driver ,100, 'luthel2020', 'od!Jednegodo9')
bot.loginBot()
