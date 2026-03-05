from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time


class instagram:

    def __init__(self,username,password):
        self.browser= webdriver.Chrome()
        self.password= password
        self.username= username
        self.followerlist= []
        self.followlist= []
        self.nonfollowers= []

    def login(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(self.username)
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//input[@name="pass"]').send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div').click()  
        time.sleep(5)

    def check_auth(self):
        print(self.browser.current_url)
        if self.browser.current_url == "https://www.instagram.com/accounts/login/two_factor":
            input("Authenticator detected, please solve it.\n(Press any key to continue)\n")

    def get_followers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/followers/")
        time.sleep(3)
        self.browser.find_element(By.XPATH, f"//a[@href='/{self.username}/followers/']").click()
        time.sleep(2)
        self.scroll()
        page_source_html=self.browser.page_source
        soup= BeautifulSoup(page_source_html, "html.parser")
        followers= soup.find("div", {"style":"display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;"})
        for follower in followers:
            follower_name=follower.find("span", {"dir":"auto"}).text
            self.followerlist.append(follower_name)
        
        followers_text = f"👥 Followers Found: {len(self.followerlist)}"
        print("\n\033[1;32m" + "╔" + "═"*38 + "╗\033[0m")
        print("\033[1;32m║\033[0m" + f"\033[1;37m {followers_text.center(36)} \033[0m" + "\033[1;32m║\033[0m")
        print("\033[1;32m" + "╚" + "═"*38 + "╝\033[0m\n")

    def get_follows(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/following/")
        time.sleep(3)
        self.browser.find_element(By.XPATH, f"//a[@href='/{self.username}/following/']").click()
        time.sleep(2)
        self.scroll()
        page_source_html=self.browser.page_source
        soup= BeautifulSoup(page_source_html, "html.parser")
        follows= soup.find("div", {"style":"display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;"})
        for follow in follows:
            follow_name=follow.find("span", {"dir":"auto"}).text
            self.followlist.append(follow_name)
        
        follows_text = f"👣 Following Found: {len(self.followlist)}"
        print("\n\033[1;35m" + "╔" + "═"*38 + "╗\033[0m")
        print("\033[1;35m║\033[0m" + f"\033[1;37m {follows_text.center(36)} \033[0m" + "\033[1;35m║\033[0m")
        print("\033[1;35m" + "╚" + "═"*38 + "╝\033[0m\n")

    def scroll(self):
        self.browser.execute_script("document.body.style.overflow = 'hidden';")
        try:
            time.sleep(2)
            dialog = self.browser.find_element(By.XPATH, "//div[@role='dialog']")
            scroll_script = """
                let dialog = arguments[0];
                let scrollableDiv = Array.from(dialog.querySelectorAll('div')).find(el => el.scrollHeight > el.clientHeight);
                if (scrollableDiv) {
                    scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
                    return scrollableDiv.scrollHeight;
                }
                return 0;
            """
            last_height = 0
            
            while True:
                new_height = self.browser.execute_script(scroll_script, dialog)
                time.sleep(1.5) 
                if new_height == last_height:
                    break
                    
                last_height = new_height
                
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            
        finally:
            self.browser.execute_script("document.body.style.overflow = '';")

    def check_non_followers(self):
        self.nonfollowers = list(set(self.followlist) - set(self.followerlist))

        print("\n\033[1;36m" + "╔" + "═"*38 + "╗\033[0m")
        print("\033[1;36m║\033[0m" + " \033[1;31m    Your Non Followers  \033[0m" + "\033[1;36m║\033[0m")
        print("\033[1;36m╠" + "═"*38 + "╣\033[0m")
        
        for user in self.nonfollowers:
            print(f"\033[1;33m  ➤ \033[0m {user}")
        print("\033[1;36m" + "╚" + "═"*38 + "╝\033[0m\n")

    def save(self):
        with open("instagramlist.txt","w", encoding="utf-8") as file:
            file.write(f"Your Followers: {self.followerlist}\nYour Follows: {self.followlist}\nYour NonFollowers:{self.nonfollowers}")

def askinfo():
    print("\n\033[1;36m" + "╔" + "═"*38 + "╗\033[0m")
    print("\033[1;36m║\033[0m" + "\033[1;37m        🚀 INSTAGRAM LOGIN 🚀       \033[0m" + "\033[1;36m║\033[0m")
    print("\033[1;36m╠" + "═"*38 + "╣\033[0m")
    username = input("\033[1;36m║\033[0m \033[1;33m👤 Username :\033[0m ")
    password = input("\033[1;36m║\033[0m \033[1;31m🔑 Password :\033[0m ")
    print("\033[1;36m" + "╚" + "═"*38 + "╝\033[0m\n")
    print("\033[1;32m[+] Login information received successfully. Bot is starting...\033[0m\n")
    os.system('cls')
    return username,password

username, password = askinfo()
insta=instagram(username,password)
insta.login()
insta.check_auth()
insta.get_followers()
insta.get_follows()
insta.check_non_followers()

insta.save()
