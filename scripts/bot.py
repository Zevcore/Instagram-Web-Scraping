import time, random

class Bot():

    def __init__(self, driver, count, login, password):
        self.driver = driver
        self.count = count
        self.login = login
        self.password = password

    def findPath(self, xpath):
        elements = self.driver.find_elements_by_xpath(xpath)
        while len(elements) == 0:
            time.sleep(0.5)
            elements = self.driver.find_elements_by_xpath(xpath)
        return elements[0]

    def loginBot(self):
        self.driver.get("https://instagram.com")
        time.sleep(2)

        self.findPath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        self.findPath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(self.login)
        self.findPath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(self.password)
        self.findPath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()

        self.findTag()

    def findTag(self):
        self.findPath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        self.driver.get('https://www.instagram.com/explore/tags/fire/') # TODO: randomize tags
        self.findPath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]').click() # TODO: randomize choice

        self.loopBot()

    def loopBot(self):
        for i in range(self.count):
            current = self.findPath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            inside = self.driver.find_element_by_css_selector('span[class=""]>svg[class="_8-yf5 "][viewBox="0 0 48 48"]')
            context = inside.get_attribute('aria-label')
            if context != "Nie lubię":
                time.sleep(random.randint(5,8))
                current.click()
                time.sleep(random.randint(5,8))

                follow = self.findPath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                textarea = self.findPath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                if follow.get_attribute('innerText') == "Obserwuj":
                    follow_rand = random.randint(0,10)
                    if follow_rand <= 8:
                        follow.click()
                        time.sleep(random.randint(5,8))

                    comment_rand = random.randint(0,10)
                    #if comment_rand <= 6: # TODO: comms
                        #textarea.click()
                        #comment = driver.find_element_by_css_selector('textarea[class="Ypffh focus-visible"]')
                        #comment.send_keys(comments[random.randint(0, len(comments))])
                        #self.findPath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
                       # time.sleep(random.randint(0,10))


                else: 
                    time.sleep(random.randint(8,11))

                print(f"Odwiedzono: {i+1} z {self.count}")



        #Next post
        self.findPath('/html/body/div[4]/div[1]/div/div/a[2]').click()
        time.sleep(random.randint(3,5))