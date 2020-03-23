import random
from tkinter import *


def press():

    greetings=['hola','hello','namaste','salaam']
    random_greetings=random.choice(greetings)

    questions=['how u doing','whats up','kaise ho','aur kya haal']
    responses=['good','okay','chill','mast','bole to jhakaaaaas']
    random_response=random.choice(responses)

    question1=['where am i','whats my location','what is this place','is this hell']
    answer=['u are in mumbai','u are in navi mumabi','u r in the city of dreams','u r in kharghar']
    random_answer=random.choice(answer)

    while True: 
        userInput = input("enter input ")
        if userInput in greetings:
            print(random_greetings)
        elif userInput in questions:
            print(random_response)
        elif userInput in question1:
            print(random_answer)
        else:
            print("i did not understand what u said")

if __name__ == "__main__":
    gui= Tk()
    gui.configure(background="#645cdb")
    gui.title("Sita- The ChatBot")
    gui.geometry("500x500")
    photo = PhotoImage(file="chatbot.png")
    label1 =label1(gui, image=photo)
    label1.pack()
    button1=Button(gui,text='Lets chat',highlightbackground='#645cdb',width= 12,height=2,command=lambda: press)
    button1.grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
    gui.mainloop()