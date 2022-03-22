import tweepy, pyautogui, time, os, hashlib
from tweepy import api
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By

#test vscode commit

#DO NOT CHANGE FAILSAFE TO FALSE, YOU WOULD RISK DESTROYING YOUR COMPUTER, DO NOT ALTER THESE FAILSAFES
pyautogui.FAILSAFE = True
#0.1 is too fast, this is the lowest pause I'm comfortable with
pyautogui.PAUSE = 0.2

#TO CHECK YOUR TWEEPY VERSION, RUN "pip show tweepy" IN YOUR COMMAND LINE
#DO NOT USE CHANGE ALL OCCURANCES FOR BACKSLASHES/FORWARD SLASHES, A BACKSLASH IS PRESENT IN THE getKeys METHOD AND WILL BREAK IF THE split(\n) IS ALTERED

key_file = "C:\\Users\\jrkni\\AppData\\Local\\Programs\\Python\\Python310\\VSCodeScriptsIMade\\HaloIntroTwitterBot\\TwitterAPIKeys.txt"
destination_folder = "C:\\Users\\jrkni\\AppData\\Local\\Programs\\Python\\Python310\\VSCodeScriptsIMade\\HaloVideoRandomizer\\Halo Videos"

#Gets API keys and Access Tokens from a .txt file 
def getKeys(credential):
    cred_dict = {}
    with open(key_file) as f:
        for line in f.read().split("\n"):
            splitLines = line.split(": ")
            cred_dict[splitLines[0]] = splitLines[1]
        return cred_dict[credential]

api_key = getKeys("API Key")
api_secret_key = getKeys("API Key Secret")
access_token = getKeys("Access Token")
access_token_secret = getKeys("Access Token Secret")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
bot_id = api.verify_credentials()

web_URL = Request("https://thisvid.space/sahphoenix_", headers = {'User-Agent': 'Chrome/98.0.4758.102'})
webPage = urlopen(web_URL)
driver = webdriver.Chrome("/Users/jrkni/AppData/Local/Programs/Python/Python310/Lib/site-packages/selenium/webdriver/chromium/chromedriver.exe")
driver.get("https://thisvid.space/sahphoenix_")
vidLinks = driver.find_elements(By.LINK_TEXT, "Video link")

def checkMentionMediaType_Respond():
    mention_id = 1
    while True:
        mentions = api.mentions_timeline(since_id = mention_id)
        for mention in mentions:
            mention_id = mention.id
            message = "@"+ mention.author.screen_name + " @this_vid" + "ty for clip"
            #sets mention_id to the id of the current mention being accessed (keeping track of which mention is being accessed)
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            #if the mention is in reply to an original tweet (not a reply to a reply) and if the mention is not my bot's tweet
                for media in mention.entities:
                #checks if there is any media-entity
                    if "media" in mention.entities:
                        media_details = mention.entities["media"]
                        media_details_kind = media_details[0]
                        if media_details_kind["type"] != "video": #and media_details_kind["type"] != "gif":
                    #need to limit the downloads to only video, but it seems to work at the moment if I only tweet videos at it
                    #checks if media type is a video. If not, then it'll stop executing here.
                            try:
                                print("Attempting to @this_vid...")
                                api.update_status(message, in_reply_to_status_id = mention.id_str)
                                print("Successfully mentioned @this_vid bot")
                            except Exception as exc:
                                print(exc)
        time.sleep(15)
        return True

#def checkMentions():
    #Needs to check if a particular tweet has already been replied to
    #if tweet has reply and the reply mention.author.id == bot_id:
        #skip to the next mention

def changeDirToDestination():
    pyautogui.keyDown("alt")
    pyautogui.press("d")
    pyautogui.keyUp("alt")
    pyautogui.typewrite(destination_folder)

def hotkeySave():
    pyautogui.keyDown("ctrlleft")
    pyautogui.press("s")
    pyautogui.keyUp("ctrlleft")

def numfilesinDestination():
    
    #Counts files in destination_folder
    numFiles = 0
    for f in os.listdir(destination_folder):
        numFiles+=1

    return numFiles

def getVidLinks():
    
    i = 0
    
    for element in vidLinks:
        j = 0
        currentDir = os.getcwd()
        
        newFileName = "newIntro" + str(numfilesinDestination() + 1)
        
        print(element)
        
        element = i
        vidLinks[element].click()

        hotkeySave()

        pyautogui.typewrite(newFileName)
        isDirPath = destination_folder + "\\" + newFileName
        
        if (currentDir != destination_folder):
            
            print("Incorrect directory, changing to destination_folder address")
            changeDirToDestination()
            
            if (os.path.isdir(isDirPath)):
                print("file already exists")
                exit
            
            else:
                while (j < 4):
                    pyautogui.press("enter")
                    j+=1

        elif (currentDir == destination_folder):
            
            print("Correct directory")
            
            if (os.path.isdir(isDirPath)):
                print("file already exists")
                exit
                
            else:
                while (j < 4):
                    pyautogui.press("enter")
                    j+=1
        
        print("Clicked link")
        i+=1
        print("Next element")

#def blake2b_for_file(path, block_size=256*128, hr=False):
   # '''
    #Block size directly depends on the block size of your filesystem
    #to avoid performances issues
    #Here I have blocks of 4096 octets (Default NTFS)
    #'''
    #blake2b = hashlib.blake2b()
    #with open(path,'rb') as f: 
        #for chunk in iter(lambda: f.read(block_size), b''): 
             #blake2b.update(chunk)
    #if hr:
        #return blake2b.hexdigest()
    #return blake2b.digest()

#blake2bsumFiles = {}
#with open(destination_folder) as folder:
    #for file in folder:
        #file = 
        #blake2bsumFiles[blake2bsumFiles[0]] = blake2b_for_file(file)

def main():
    checkMentionMediaType_Respond()
    getVidLinks()


if __name__ == "__main__":
    main()
