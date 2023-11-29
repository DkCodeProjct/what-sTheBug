def main():
    
    attemptsToLogging = 3
    while attemptsToLogging > 0:
        
        getUserName = input("enter name to loggin: ")
        if isvalid(getUserName):
            print("loggin succsess//")
            break
        else:
            print("invalid loggin name !!!")
            attemptsToLogging -= 1
    
    if attemptsToLogging == 0:
        print("try agin after 30.sec")

def isvalid(s):
    
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if len(s) >= 2 and len(s) <=  6:
        return True
    
    i = 0
    while i < len(s):
        if s[0].isalpha() == False:
            if s[3] == '0':
                return False
            else:
                break
        i += 1

        for char in s:
            if not char in [" ", ",", ".", "/", "?"]:
                return False
        return True

if __name__ == "__main__":
    main() 
