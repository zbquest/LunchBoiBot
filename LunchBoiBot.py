import urllib.request
import webbrowser
import json
import time
import random
import re

#Global main variables
restaurants = [
  {'name':'MVR','phone':'','menu_url':'https://'},
  {'name':'Charlie Staples','phone':'','menu_url':'https://'},
  {'name':'Krzavit','phone':'','menu_url':'https://'},
  {'name':'Knafa','phone':'','menu_url':'https://'},
  {'name':'Uptown Pizza','phone':'','menu_url':'https://'},
  {'name':'Republic Pizza','phone':'','menu_url':'https://'},
  {'name':'Pressed','phone':'','menu_url':'https://'},
  {'name':'Golden Hunan','phone':'','menu_url':'https://'},
  {'name':'Chipotle','phone':'','menu_url':'https://'},
  {'name':'Sr. Jalapeno','phone':'','menu_url':'https://'},
  {'name':'Royal Oaks','phone':'','menu_url':'https://'},
  {'name':'Avalon','phone':'','menu_url':'https://'},
  {'name':'Chik-fil-A','phone':'','menu_url':'https://'},
]
rchoice = 0
offset = 0
kill = False
timestamp = 0
url = "https://api.telegram.org/bot938450342:AAESkJvw-rVlYRs9xnEbHwAstRt180RRj5c/getupdates?offset="
rurl = "https://api.telegram.org/bot938450342:AAESkJvw-rVlYRs9xnEbHwAstRt180RRj5c/sendmessage"

#random food place to pick from
def FoodPicker():
    rchoice = 0
    random.shuffle(restaurants)
    return restaurants[rchoice]["name"]


#Processes all old messages
length = 100
while length > 10:
    #pulls data from bot webpage and repeatedly clears till data is new
    with urllib.request.urlopen(url+str(offset)) as fp:
        j = json.loads(fp.read().decode())
        offset = j["result"][len(j["result"])-1]["update_id"]
        print("o="+str(offset))
        timestamp = j["result"][len(j["result"])-1]["message"]["date"]
        print("t="+str(timestamp))
        length = len(j["result"])
        print("l="+str(length))

#main infinite loop
while True and not kill:
    #pulls data from bot webpage and clears old messages
    with urllib.request.urlopen(url+str(offset)) as fp:
        j = json.loads(fp.read().decode())
        print(j)
        offset = j["result"][len(j["result"])-1]["update_id"]
        print("o="+str(offset))

        #if last message has new timestamp then do a thing
        if timestamp != j["result"][len(j["result"])-1]["message"]["date"]:
            print("t="+str(timestamp))
            c = 1

            #processes all new messages
            while c < len(j["result"]):
                print("c="+str(c))
                r = ""

                #get important info about message
                i = j["result"][c]["message"]["chat"]["id"]
                timestamp = j["result"][c]["message"]["date"]
                m = j["result"][c]["message"]["text"]
                print("message:="+m)

                #start bot code here and r is the response the bot says

                #rolls for random lunch options when "whats for lunch" is said
                if m.lower() == "/whatsforlunch":
                    r = FoodPicker()

                #no will cycle through the list till the end
                if m.lower() == "/no":
                    if rchoice >= len(restaurants) - 1:
                        r = "just get ASS you ungrateful fuck"
                    else:
                        rchoice += 1
                        r = restaurants[rchoice]["name"]

                #YEEETTTT!!!
                if m.lower().find("lunchboi") >= 0:
                    r = "YEEEETT!!"

                #
                #
                #
                #
                #
                #

                #end of code for bot decisions

                #kills the god lunch boi
                if m.lower() == "/killboi":
                    kill = True
                    break
                
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
