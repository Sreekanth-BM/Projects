try:
   try:
     #string = "hhelO"+9
     string = "hhelO"
   except:
     print("String+Number")
   else:
     try:
       string= "hell"+9
     except:
       print("Number+String")
except:
    print("Last exception")
