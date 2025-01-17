import re
import random 
import chatbot_functions as ch
#import antigravity do not uncomment unless you want to fly 
import sys







# Is able to maintain a dialogue no matter what the user name is, except for “bye”, which should terminate the dialogue. 20pts
chatbot = ch.Chatter("chatbot")
base_stuff = sys.getsizeof(chatbot.class_items)
functions = sys.getsizeof(chatbot.recognize_emotion) + sys.getsizeof(chatbot.respond_to_emotion) + sys.getsizeof(chatbot.get_name_and_greet) + sys.getsizeof(chatbot.looking) + sys.getsizeof(chatbot.exp) + sys.getsizeof(chatbot.calling) + sys.getsizeof(chatbot.exp2) + sys.getsizeof(chatbot.family) + sys.getsizeof(chatbot.finisher) + sys.getsizeof(chatbot) + sys.getsizeof(chatbot.fun1)
total_mem_used = functions + base_stuff

print(f"dictionary used {total_mem_used} bytes")















