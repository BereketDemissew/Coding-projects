import re
import random
class Chatter:
    def __init__(self, name):
        self.name = name
        self.__name = ""
        self.end = True
        self.__expressions = {
            "sad" : "Oh no, I'm sorry you feel so down.",
            "happy": "Great nice to hear you're in great spirits!",
            "joyful": "Sounds like you're full of joy today!",
            "bye": None,
            "angry": "Sounds like someone is angry",
            "ok": "Not everyday can be the best day but it could be a whole lot worse",
            "good": "Nice to know your day is going well",
            "bad": "Sorry to hear that from you it can always get better",
            "mom": "Well tell you mother I said hi",
            "dad": "Hey do me a favor and tell you're dad I say hello",
            "sister": "Thats a new one not many with a sister would say their sister",
            "brother": "Intresing tell your brother that I sell candy in a white van to give him a good scare!",
            "friend": "Thinking about a friend first I respect that"
        }

        
        self.__emotion_patterns = {
        'sadness': re.compile(r'\b(sad|sadden|saddened|down|melancholy)\b', re.IGNORECASE),
        'happiness': re.compile(r'\b(happy|happiness)\b', re.IGNORECASE),
        'joy': re.compile(r'\b(joy|joyful|joyfulness|cheerful|glee|delight)\b', re.IGNORECASE),
        }
#---------------------------------------------------------------------------------------------------------------------------------------------
    def class_items(self):
        end = self.end
        nameer = self.name
        pattern = self.__emotion_patterns
        name = self.__name
        expess = self.__expressions
        
#---------------------------------------------------------------------------------------------------------------------------------------------



    def recognize_emotion(self, name):
        for emotion, pattern in self.__emotion_patterns.items():
            if pattern.search(name):
                return emotion
        return None
#---------------------------------------------------------------------------------------------------------------------------------------------

    def respond_to_emotion(self, input):
        input = self.__name
        emotion = self.recognize_emotion(input)
        
        if emotion == 'sadness':
            return f"I'm sorry you're feeling sad, {self.__name}. I'm here for you."
        elif emotion == 'happiness':
            return f"That's wonderful, {self.__name}! Happiness looks good on you!"
        elif emotion == 'joy':
            return f"Your name radiates joy, {self.__name}! Keep spreading the joy!"
        else:
            return f"Hello {self.__name}, it's great to meet you!"
#---------------------------------------------------------------------------------------------------------------------------------------------

    def get_name_and_greet(self, user_input):   
        if user_input == "bye":
             print("Thanks for playing")
             self.end = False
             return False
        match_iam = re.match(r'I am (\w+)', user_input)
        match_name = re.match(r'(\w+) is my name', user_input)
        check = True
        fail = 0
        while check:
            if fail > 0:
                user_input = input("please try again I did not get that")
                match_iam = re.match(r'I am (\w+)', user_input)
                match_name = re.match(r'(\w+) is my name', user_input)
            if match_iam:
                name = match_iam.group(1)
                self.__name = name
                check = False
            elif match_name:
                name = match_name.group(1)
                self.__name = name
                check = False
            else:
                print("Sorry, I couldn't understand your name.")
                print("please introduce yourself self when you give your name")
                fail += 1
        input = ""
        print(self.respond_to_emotion(input))
#---------------------------------------------------------------------------------------------------------------------------------------
    def looking(self):
        print(f"What did you do today {self.__name}?")
        phone = input()
        verb_pattern = r"\b(?:[a-z]+(?:s|ed|ing))?\b"
        finder =  re.findall(verb_pattern, phone.lower())
        check = False
        bringer = ''
        i = 0
        ender = True
        fail = 0
        while ender:
            if fail > 1:
                print("try again")
                phone = input()
                finder =  re.findall(verb_pattern, phone.lower())
                bringer = ''
                i = 0
                check = False
            while i < len(finder):
                if finder[i] != '':
                    bringer = finder[i]
                    check = True
                i += 1
            if check:
                infin = ""
                if bringer.endswith("ed"):
                    infin = bringer[:-2]
                    print(f"Well {self.__name}, the activity of {infin} sounds fun!")
                    break
                elif bringer.endswith("s"):
                    infin = bringer[:-1]
                    print(f"Well {self.__name}, the activity of {infin} sounds fun!")
                    break
            if phone == "funney" and check == False:
                print(chr(sum(range(ord(min(str(not())))))))
                break
            fail += 1
#---------------------------------------------------------------------------------------------------------------------------------------------
    def exp(self, phone):
        ender = True
        while ender:
            found_expression = None
            for key in self.__expressions:
                if phone in key:
                    found_expression = self.__expressions[key]
                    break
            phone = phone.lower()
            if re.search(r'\b(sad|sadden|saddened|down|melancholy)\b', phone):
                print(self.__expressions["sad"])
                break
            elif re.search(r'\b(happy|happiness)\b', phone):
                print(self.__expressions["happy"])
                break
            elif re.search(r'\b(joy|joyful|joyfulness|cheerful|glee|delight)\b', phone):
                print(self.__expressions["joyful"])
                break
            elif re.search(r'\b(angry|mad|frustrated|rage)\b', phone):
                print(self.__expressions["angry"])
                break
            elif re.search(r'\b(ok|alright|50/50)\b', phone):
                print(self.__expressions["ok"])
                break
            elif re.search(r'\b(good|great|wonderful)\b', phone):
                print(self.__expressions["good"])
                break
            elif re.search(r'\b(bad|awful|not good)\b', phone):
                print(self.__expressions["bad"])
                break

            if (found_expression and phone != "bye") and self.__name in phone:
                stuff = "I am " + self.__name
                self.get_name_and_greet(stuff)
            if found_expression and phone != "bye" :
                print(found_expression)
                ender = False
            elif phone == "bye":
                return False
            
            else:
                phone = input("I'm sorry, I did not get that. Can you type that again?")
#---------------------------------------------------------------------------------------------------------------------------------------------
    def calling(self):
        if self.end :
            print(f"{self.__name} how are you feeling right now?")
            phone = input()
            if phone == "bye":
                self.end = False
                print("Thanks for playing")
                return False
            self.exp(phone)
            self.looking()
 # -------------------------------------------------------------------------------------------------------------------------------------               
    def exp2(self, phone):
        ender = True
        while ender:
            found_expression = None
            for key in self.__expressions:
                if phone in key:
                    found_expression = self.__expressions[key]
                    break
            phone = phone.lower()
            if re.search(r'\b(mom|mommy|mother)\b', phone):
                print(self.__expressions["mom"])
                break
            elif re.search(r'\b(dad|daddy|father)\b', phone):
                print(self.__expressions["dad"])
                break
            elif re.search(r'\b(brother|bro)\b', phone):
                print(self.__expressions["brother"])
                break
            elif re.search(r'\b(sister|sis|sista)\b', phone):
                print(self.__expressions["sister"])
                break
            elif re.search(r'\b(friend|buddy|pal)\b', phone):
                print(self.__expressions["friend"])
            
            
            if re.search(r'\b(bye)\b', phone):
                print("Thanks for playing")
                return False
            
            else:
                phone = input("I'm sorry, I did not get that. Can you type that again?")
 # -------------------------------------------------------------------------------------------------------------------------------------               
    def family(self):
        print(f"Ready for a question {self.__name}? Y/N")
        awn = input()
        check = True
        while check:
            if awn == "Y":
                check = False
                break
            else:
                print("WRONG AWNSER! TRY AGAIN")
                awn = input()
        print("What family member are you thinking about right now?")
        fam = input()
        self.exp2(fam)
 # -------------------------------------------------------------------------------------------------------------------------------------               
    def finisher(self):
        user_input = input("Hello this discount ELIZA chatbox made by your local sleep deprived college student at your service! May I ask for thy users name (please say your name along 'I am __' or '___ is my name): ")
        self.get_name_and_greet(user_input)
        self.calling()
        self.family()
        while self.end:
            self.fun1()
 # -------------------------------------------------------------------------------------------------------------------------------------               
    def fun1(self): 
        lists = ["Sloths can hold their breath longer than dolphins", "pythons .sort() function is made in C and not python.", "The first computer viruses were created for demonstration purposes, not to cause damage.", "python is older than Java", "The fear of long words is called hippopotomonstrosesquippedaliophobia, or sesquipedalophobia", "Scotland chose the unicorn as its national animal.", "rodents can't puke", "a toaster makes an awful bath bomb", "netflix only cancels good shows", "butterflies are opportunistic blood feeders", "No word in the English language rhymes with the word month", "pinocchio translates to pine eye", "the eiffel tower is taller in the summer", "toothpaste was once made of grounded-up ox hooves' ashes, burnt eggshells, and pumice", "There is only one letter that does not appear in the name of any us state", "lemon float but limes sink", "there is a species of insect with a giant penis relative to its body size, making up approximately 25 percent of its body mass. Its giant penis acts to defend against predation by violently emitting a stream of chemicals that cause a violent exothermic reaction. Its giant penis that makes up a quarter of its body mass kills its predators by boiling them alive with the hot fluid violently shot from its penis", "The chainsaw was originally made for aiding in childbirth", "brown bears can run up to 30 miles an hour", "toenails keep growing after you die", "the largest intestinal tapeworm was over 100 feet long", "chatGPT can't count the number of r's in strawberry", "people with blue eyes share a common ancestor", "The human organ most variable in size is the stomach which can vary up to six times in size depending on the individual", "print(chr(sum(range(ord(min(str(not()))))))) prints something that looks like among us","All of the items in this list came from asking random ELON students from multiple majors and departments."]
        if self.end:
            print("Thank you for geting this far my dear human! do you want to hear a fun fact? ('yes' or 'Y' / or type 'bye' to end)")
            awn = input()
            if awn == "bye":
                print("Thanks for playing!")
                self.end = False
                return False
            elif awn == "Y" or awn == "yes" or awn == "y":
                print("you picked correct")
                pick = random.randrange(0, len(lists) - 1)
                guess = lists[pick]
                print(guess)
            else:
                print("To bad here you go!")
                pick = random.randrange(0, len(lists) - 1)
                guess = lists[pick]
                print(guess)