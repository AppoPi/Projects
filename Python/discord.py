import requests
import time



channelID = '163392059141652480'



class DiscordAPI:
    LOGIN = 'https://discordapp.com/api/auth/login'
    LOGOUT = 'https://discordapp.com/api/auth/logout'
    GET_MESSAGES = 'https://discordapp.com/api/channels/' + channelID + '/messages'
    token = ''
    USER = 'appopi@yahoo.com'
    PASS = 'e75ySnx6rA9w'

    def login(self,):
        r = requests.post(self.LOGIN, data = {"email":self.USER, "password":self.PASS})
        self.token = r.json()[u'token']
        return r

    def logout(self):
        return requests.post(self.LOGOUT)

    def getMessages(self):
        json = {
            'before': 1000000000,
            'after': 0,
            'limit': 50}
        return requests.get(self.GET_MESSAGES, headers = json) #{"token":self.token})

    
a = DiscordAPI()
print a.login()

print a.getMessages()
print a.logout()
