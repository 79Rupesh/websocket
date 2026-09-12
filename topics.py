# web socket

# web socket kya karta ?

# web socket 2 way communication banana hai

# client <--> Server


#         continue
#         connection

# Brower : "Hello"
# server : "Hii"

# requrment H.W

# Backend : fastapi
# frondend : HTML + javascript

# ye feature add karna hai

# websocket connectio
# username
# send message
# receive message
# broadcast
# online users count
# join notification
# leave notification


# websocket.accept()
# websocket.close()
# websocket.receive_text()
# websocket.send_text()







# HTTPException

# # Exception kya hotah hai ?
# program ko run karte waqt kuchh problem aati hai wahi hai exception
# 1.

# a=10
# b=2

# print(a/b)


#  basic python try/except

# try:
#     resky Code
# except:
#     error handle


# a=10
# b=0
# try:
#     print(a/b)
# except:
#     print("Zero se divide nhi kar sakhte hai ")



# from fastapi import FastAPI , HTTPException

# app = FastAPI()

# @app.get("/divide")
# def divide():

#     if 0==0:
#         raise HTTPException(
#             status_code=400,
#             detail="can not by zero"
#         )

#     result = 10/0

#     return {
#         "result":result
#     }




# try:
#     risky Code
# except:
#     ager error aaya Tab
# else:
#     ager error na aaye tab jo chalana hai
# finally:
#     hamesha chalega




# try:
#     a=10
#     b=2
#     result = a/b

# except:
#     print("Somrthong went wrong")
# else:
#     print("Division succefully")
#     print(result)
# finally:
#     print("mai humesha chaluga")