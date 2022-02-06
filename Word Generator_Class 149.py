from tkinter import * 
import random
root=Tk()
root.title("Lucky Friend")
root.geometry("500x500")
root.configure(background = "snow")

word_holder = Label(root)
word_holder.place(relx=0.5, rely=0.6, anchor=CENTER)
alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def random_number() :
    random_number = random.randint(0,25)
    random_number2 = random.randint(0,25)
    random_number3 = random.randint(0,25)
    random_number4 = random.randint(0,25)
    random_number5 = random.randint(0,25)
    
    random_alpha1 = alpha_list[random_number]
    random_alpha2 = alpha_list[random_number2]
    random_alpha3 = alpha_list[random_number3]
    random_alpha4 = alpha_list[random_number4]
    random_alpha5 = alpha_list[random_number5]
    word_holder["text"] = "Word Generated : " + random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    

btn=Button(root,text="Generate a word", command = random_number, bg="light blue",fg="black")
btn.place(relx=0.5,rely=0.5, anchor=CENTER)


root.mainloop()

    