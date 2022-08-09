from os import system

def ValleyCounter(Garys_Steps, Garys_Trail):
    Current_Level, Level_List, Counter = 0, [0], 0
    for Step in range(Garys_Steps):
        if Garys_Trail[Step] == 'U':
            Current_Level += 1
            Level_List.append(Current_Level)
        elif Garys_Trail[Step] == 'D':
            Current_Level -= 1
            Level_List.append(Current_Level)
            if Current_Level == -1:
                Counter += 1
    return Counter, Level_List

if __name__ == "__main__":
    system('cls')
    while True:
        Steps: int = 0
        Garys_Trail: str = ""
        User_input = input("Step number in Gary's hike: ")
        try:
            Steps = int(User_input)
            Allowed_input, Invalid_Str = "UD", True
            while Invalid_Str:
                User_input: str = input("Traveled trail: ").upper()
                if all(character in Allowed_input for character in User_input) and Steps == len(User_input):
                    Garys_Trail, Invalid_Str = User_input, False
                else:
                    system('cls')
                    print(f"Trail '{User_input}' must contain only {Steps} 'U' & 'D' characters, try again.")
                    Invalid_Str = True
        except ValueError:
            system('cls')
            print(f"Invalid integer '{User_input}', try again.")
        else:
            break
    
    Counter, Levels = ValleyCounter(Steps, Garys_Trail)
    print(f"Gary traveled {Counter} valleys through the trail: {Levels}")