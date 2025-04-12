import requests
def loop1():
 def t600thingactivate():
     data = {"Specialty":str(mysteriousdevice)}
     url = str(httpthingy)+str(SpecialDomain)+str("/checkthe600thing")
     the600thing = requests.post(url,json=data)
     the600thing = the600thing.json()
     the600thing = the600thing["Success"]
     return str(the600thing)
 def countdownthingactivate():
     data = {"Specialty":str(mysteriousdevice)}
     url = str(httpthingy)+str(SpecialDomain)+str("/checkthecountdowthing")
     countdownthing = requests.post(url,json=data)
     print("COUNTDOWNTHING: "+str(countdownthing))
     try:
      countdownthing = countdownthing.json()
     except:
      print("HOW?")
     try:
      countdownthing = countdownthing["Success"]
     except:
         print("NO!")
     return str(countdownthing)
 print("DOES THIS EVEN DO ANYTHINGg")
 the600thing = 0
 timeatstarttime = 0
 with open("changethe600thing.txt","w") as file:
     file.write(str(600))
 totaltime = 3
 with open("changethe600thing.txt","r") as file:
    fileread = str(file.read())
    print("IT WORKS NOW!")
    if float(fileread)>0:
     themega600thing = float(fileread)-totaltime
     
     if themega600thing<0 and themega600thing>=-3:
         countdownthing = ConvertTheNumber(themega600thing)-3
         if countdownthing<0:
             the600thing = 600+countdownthing
             with open("changethe600thing.txt","w") as file:
                 file.write(str(the600thing))
         with open("countdownthing.txt","w") as file:
             file.write(str(countdownthing))
     elif themega600thing<0:

         the600thing = ConvertTheNumber(themega600thing)-3
         with open("changethe600thing.txt","w") as file:
             file.write(str(the600thing))
     else:
         if the600thing%3 == 0 and not the600thing%2 == 0:
             countdownthing = ConvertTheNumber(themega600thing)
             with open("countdownthing.txt","w") as file:
                 file.write(str(countdownthing))
         else:
          the600thing = ConvertTheNumber(themega600thing)


          with open("changethe600thing.txt","w") as file:
             file.write(str(the600thing))

    else:
        with open("countdownthing.txt","r") as file:
            themegacountdownthing = float(file.read())-totaltime
            themegacountdownthing = ConvertTheNumber(themegacountdownthing)-2
            #if it is 2 off switch 2 to four

            the600thing = themegacountdownthing
            with open("changethe600thing.txt","w") as file:
                file.write(str(the600thing))
 averagetimelist = 0
 averagetimecount = 0
 SpecialDevice = 2

 while True:
     countdownthingactivate()
     while the600thing>0:
         starttime = time.time()
         time.sleep(0.25)
         try:
          response23 = ""
          if SpecialDevice == 2:
           response23 = t600thingactivate()
         
           floatable = True
           try:
             float(response23)
           except:
             floatable = False
           if floatable == False:
               the600thing = 0
               break
           the600thing = float(response23)
           
           countdownthing = 3
          else:
           response23 =t600thingactivate()
         
           floatable = True
           try:
             float(response23)
           except:
             floatable = False
           if floatable == False:
               the600thing = 0
               break
           try:
            response23 = response23.json()
           except Exception as e:
               print("THAT'S NONSENSE: "+str(e))
           try:
            print("RESPONSE23"+str(response23["Error"]))
           except Exception as e:
            print("WELL IT ERRORED"+str(e))
           the600thing = float(response23)
           countdownthing = 3

         except Exception as e:
             lol=True
         endtime = time.time()
         truetime = endtime-starttime
         averagetimelist+=truetime
         averagetimecount+=1
         trueaveragetime = averagetimelist/averagetimecount

     numthing=3
     while numthing>0:
      time.sleep(0.25)
      if numthing == 0:
          the600thing = 600
          break
      try:
       response222 = ""
       response222 = countdownthingactivate()

       responsedata = response222
       numthing = float(responsedata)
       if numthing<0.3:
          numthing = 0
          the600thing = 600
          break
       else:
         print("Response222:"+str(response222))

      except Exception as e:

         loadloop = True
         numthing = 0
         the600thing = 600
         break
         lol=True
         
thread2 = threading.Thread(target=loop1)
thread2.start()
