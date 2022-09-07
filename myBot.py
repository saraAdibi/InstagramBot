from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from info import username, password


class Bot():
    def __init__(self):
        self.login(username, password)

    def login(self, username, password):
        # opening web browser
        self.driver = webdriver.Firefox()
        self.driver.get('https://instagram.com')
        sleep(2)

        # set the username
        username_input = self.driver.find_element(
            "xpath", '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input'
        )
        username_input.send_keys(username)
        sleep(1)

        # set the password
        password_input = self.driver.find_element(
            'xpath', '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input'
        )
        password_input.send_keys(password)
        sleep(1)

        # LOGIN
        self.driver.find_element(
            'xpath', '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div'
        ).click()
        sleep(3)

        # Current follow requests page
        self.driver.get(
           'https://www.instagram.com/accounts/access_tool/current_follow_requests'
        )
        sleep(5)

        list_of_usernames = []
        for username in self.driver.find_elements(by=By.CLASS_NAME, value='-utLf'):
            list_of_usernames.append(username.text)
            print(list_of_usernames)
        for i in list_of_usernames:
            self.driver.get(f'https://instagram.com/{i}')
            sleep(2)
            self.driver.find_element(
                'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button/div'
            ).click()
            sleep(2)
            self.driver.find_element(
                'xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]'
            ).click()
            sleep(5)


def main():
    myBot = Bot()


if __name__ == '__main__':
    main()
