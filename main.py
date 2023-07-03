from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from PIL import Image, ImageTk
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')



def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0
    
    the_word=random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo ("Cool Stuff", "You guessed right")
                    newGame()

        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses==11:
                    messagebox.showwarning ("Opps!", "Game Over")
                    newGame()





if __name__ == '__main__':
    root = ctk.CTk()
    root.title('Names of African Countries')
    root.resizable(False, False)
    root.geometry('500x400')

    word_list = ["NIGERIA", "TOGO", "MALI", "ZAMBIA", "GAMBIA",
             "CAMEROUN", "ALGERIA", "EGYPT", "MOROCCO", "GHANA", "SOMALIA",
             "GABON", "SENEGAL", "TANZANIA", "BENIN", "ETHIOPIA", "GUINEA",
             " SUDAN", "CONGO", "ANGOLA", "BOTSWANA", "NIGER", 
             "RWANDA", "BURUNDI", "COMOROS", "KENYA"]

    photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png"),PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"),PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]
    
    frame1 = ctk.CTkFrame(root)
    frame1.grid(row = 0, column = 0)
    imgLabel=Label(frame1, bg="goldenrod4")
    imgLabel.grid(row=0, column=0, columnspan=3, padx=35, pady=40)

    
    lblWord = StringVar()
    Label(frame1, bg="goldenrod4", fg="floral white", textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)




    frame2 = ctk.CTkFrame(root)
    frame2.grid(row = 1 , column = 0)

    n=0

    for c in ascii_uppercase:
        
        letter_butt=ctk.CTkButton(master=frame2,  text=c ,command=lambda c=c: guess(c), font=('Helvetica', 18), fg_color="black", border_spacing=20, border_width=2, border_color="goldenrod4", bg_color="black", width=40, height=40).grid(row=1+n//9,column=n%9)
        n+=1

    restart_butt=ctk.CTkButton(master=frame2, text="Restart", command=lambda:newGame(), fg_color="goldenrod4", border_spacing=5, border_width= 2, border_color="black", bg_color="goldenrod4",  width=40, height=40,font=("Helvetica" ,10, "bold")).grid(row=3, column=8)






    #welcome_page()
    newGame()
    root.mainloop()    
