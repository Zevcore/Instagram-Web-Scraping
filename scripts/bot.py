from selenium import webdriver
import time, random

count = 100 # ilość postów
driver = webdriver.Firefox();

def findByXpath(xpath):
    global driver
    elements = driver.find_elements_by_xpath(xpath)
    while len(elements) == 0:
        time.sleep(0.5)
        elements = driver.find_elements_by_xpath(xpath)
    return elements[0]

tags = ['love', 'instagood', 'me', 'tbt', 'cute', 'l4l', 'f4f', 'like4like', 'follow4follow', 'photooftheday', 'happy', 'tagforlikes', 'beautiful', 'self', 'girl', 'picoftheday', 'like4like', 'smile', 'friends', 'fun', 'like', 'fashion', 'instagirl', 'instaboy']
comments = ['Thats nice!', 'Awesome!', 'Lovely <3', 'Haha so pretty', 'What a gorgeous view', 'Cool style', "Nice shoot", "What a save!", "Sorry!", "My bad...", "Nice one!", 'What a play!', 'Centering!']

url = "https://www.instagram.com/"
login = "luthel2020"
password = "od!Jednegodo9"
hashtag = tags[random.randint(0, len(tags))]
hashtag_url = "https://www.instagram.com/explore/tags/" + hashtag + "/"

driver.get(url)
time.sleep(1)

#Login
findByXpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
findByXpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(login)
findByXpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
findByXpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()

time.sleep(random.randint(2,4))

#Go to tag
findByXpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
driver.get(hashtag_url)
findByXpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]').click()

#Like loop
for i in range(count):
    current = findByXpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    inside = driver.find_element_by_css_selector('span[class=""]>svg[class="_8-yf5 "][viewBox="0 0 48 48"]')
    context = inside.get_attribute('aria-label')
    if context != "Nie lubię":
        time.sleep(random.randint(5,8))
        current.click()
        time.sleep(random.randint(5,8))

        follow = findByXpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        textarea = findByXpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
        if follow.get_attribute('innerText') == "Obserwuj":
            follow_rand = random.randint(0,10)
            if follow_rand <= 8:
                follow.click()
                time.sleep(random.randint(5,8))

            comment_rand = random.randint(0,10)
            if comment_rand <= 6:
                textarea.click()
                comment = driver.find_element_by_css_selector('textarea[class="Ypffh focus-visible"]')
                comment.send_keys(comments[random.randint(0, len(comments))])
                findByXpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
                time.sleep(random.randint(0,10))


    else: 
        time.sleep(random.randint(8,11))

    print(f"Odwiedzono: {i+1} z {count}")



    #Next post
    findByXpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
    time.sleep(random.randint(3,5))

print('...', end='')