from comm_ai_mod import CommAIModelCostumizebel as CAIMC
from speak import Say
import json,hist_chat_name_builder

def mn1():

    chat_history = []

    is_chat__ = False

    # Initiation
    chat_hist_name=input("Enter chat ID:\n")
    if chat_hist_name:
        with open(f"files.fxg/{chat_hist_name}.json",'r') as file:
            chat_history=json.load(file)
        is_chat__=True

    while True:
        try:
            luxlulu=input("User:\n")
            lux=CAIMC(luxlulu,chat_history,"openrouter/owl-alpha").talk()

            chat_history.append({"role":"user","content":luxlulu})
            chat_history.append({"role":"assistant","content":lux})
            print("Model:")
            for i in lux:
                print(i,end='')
            print()
        
            if input("speak up?:\t").upper() == "Y":
                lakalux=lux.strip("#")
                lakalux=lakalux.strip("##")
                lakalux=lakalux.strip("###")
                lakalux=lakalux.strip("*")
                lakalux=lakalux.strip("**")
                Say(lakalux.strip(),1).sayLoud()
            else:
                print()

        except KeyboardInterrupt:
            if is_chat__==True:
                with open(f"files.fxg/{chat_hist_name}.json","w") as file:
                    json.dump(chat_history,file,indent=4)
            if is_chat__==False:
                new_name=hist_chat_name_builder.make_name()
                with open(f"files.fxg/{new_name}.json",'w') as file:
                    json.dump(chat_history,file,indent=4)
                    print("chat history name\n",new_name)
            print("\n\n\tGood Bye!\t\n\n")
            break

def mn2():

    chat_history = []

    is_chat__ = False

    # Initiation
    model_list=["inclusionai/ring-2.6-1t:free","baidu/cobuddy:free","nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free","poolside/laguna-xs.2:free","poolside/laguna-m.1:free","google/gemma-4-26b-a4b-it:free","google/gemma-4-31b-it:free"]
    for i,mod in enumerate(model_list):
        print(f"{i+1}:\t{mod}")
    ij=int(input("\n"))
    if ij <= len(model_list):
        model = model_list[ij - 1]
    else:
        raise IndexError("Model index out of range")

    chat_hist_name=input("Enter chat ID:\n")
    if chat_hist_name:
        with open(f"files.fxg/{chat_hist_name}.json",'r') as file:
            chat_history=json.load(file)
        is_chat__=True

    while True:
        try:
            luxlulu=input("User:\n")
            lux=CAIMC(luxlulu,chat_history,model).talk()

            chat_history.append({"role":"user","content":luxlulu})
            chat_history.append({"role":"assistant","content":lux})
            print("Model:")
            for i in lux:
                print(i,end='')
            print()
        
            if input("speak up?:\t").upper() == "Y":
                lakalux=lux.strip("#")
                lakalux=lakalux.strip("##")
                lakalux=lakalux.strip("###")
                lakalux=lakalux.strip("*")
                lakalux=lakalux.strip("**")
                Say(lakalux.strip(),1).sayLoud()
            else:
                print()

        except KeyboardInterrupt:
            if is_chat__==True:
                with open(f"files.fxg/{chat_hist_name}.json","w") as file:
                    json.dump(chat_history,file,indent=4)
            if is_chat__==False:
                new_name=hist_chat_name_builder.make_name()
                with open(f"files.fxg/{new_name}.json",'w') as file:
                    json.dump(chat_history,file,indent=4)
                    print("chat history name\n",new_name)
            print("\n\n\tGood Bye!\t\n\n")
            break

def main():
    xboy = input("1> pre set\n2> select optimum\n")
    if int(xboy)==1:
        mn1()
    elif int(xboy)==2:
        mn2()
    else:
        print("invaleid input\n")
        main()

if __name__ == "__main__":
    main()