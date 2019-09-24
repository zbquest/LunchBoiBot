import urllib.request
import webbrowser
import json
import time
import random
import re

#random food place to pick from
def FoodPicker():
    r = ""
    f = random.randrange(14)
    print(f)
    if f == 0:
        r = "ASS"
    elif f == 1:
            r = "MVR"
    elif f == 2:
        r = "Charlie Staples"
    elif f == 3:
        r = "Kravitz"
    elif f == 4:
        r = "Knafa"
    elif f == 5:
        r = "Uptown Pizza"
    elif f == 6:
        r = "Republic Pizza"
    elif f == 7:
        r = "Pressed"
    elif f == 8:
        r = "Golden Hunan"
    elif f == 9:
        r = "Chipotle"
    elif f == 10:
        r = "Sr. Jalapeno"
    elif f == 11:
        r = "Royal Oaks"
    elif f == 12:
        r = "Avalon"
    elif f == 13:
        r = "Chik-fil-A"
    return r

#Global main variables
offset = 0
t = 0
url = "https://api.telegram.org/bot938450342:AAESkJvw-rVlYRs9xnEbHwAstRt180RRj5c/getupdates?offset="
rurl = "https://api.telegram.org/bot938450342:AAESkJvw-rVlYRs9xnEbHwAstRt180RRj5c/sendmessage"

#Processes all old messages
length = 100
while length > 10:
    #pulls data from bot webpage and repeatedly clears till data is new
    with urllib.request.urlopen(url+str(offset)) as fp:
        j = json.loads(fp.read().decode())
        offset = j["result"][len(j["result"])-1]["update_id"]
        print("o="+str(offset))
        t = j["result"][len(j["result"])-1]["message"]["date"]
        print("t="+str(t))
        length = len(j["result"])
        print("l="+str(length))

#main infinite loop
while True:
    #pulls data from bot webpage and clears old messages
    with urllib.request.urlopen(url+str(offset)) as fp:
        j = json.loads(fp.read().decode())
        print(j)
        offset = j["result"][len(j["result"])-1]["update_id"]
        print("o="+str(offset))

        #if last message has new timestamp then do a thing
        if t != j["result"][len(j["result"])-1]["message"]["date"]:
            print("t="+str(t))
            c = 1

            #processes all new messages
            while c < len(j["result"]):
                print("c="+str(c))
                r = ""

                #get important info about message
                i = j["result"][c]["message"]["chat"]["id"]
                t = j["result"][c]["message"]["date"]
                m = j["result"][c]["message"]["text"]
                print("message:="+m)

                #start bot code here and r is the response the bot says

                #rolls for random lunch options when "whats for lunch" is said
                if m.lower() == "/whatsforlunch":
                    r = FoodPicker()

                #YEEETTTT!!!
                if m.lower().find("/lunchboi") >= 0:
                    r = "YEEEETT!!"

                #
                #
                #
                #
                #
                #
                
                #end of code for bot decisions
                
                #posts response if response is needed
                if r != "":
                    #golden hunan doesnt work error:400
                    if r == "Golden Hunan":
                        webbrowser.open(rurl+"?chat_id="+str(i)+"&text="+str(r)+"")
                    else:
                        print (rurl+"?chat_id="+str(i)+"&text="+str(r)+"")
                        with urllib.request.urlopen(rurl+"?chat_id="+str(i)+"&text="+str(r)+"") as rfp:
                            print (r)

                #increment counter
                c += 1
        fp.close()

        #delay interval in sec
        print("sleep")
        time.sleep(3)
        print("awake")
