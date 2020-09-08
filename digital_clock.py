from tkinter import *
import time
import datetime

todaydate=datetime.datetime.now().date()

class Digital:
    def __init__(self,root):
        self.root=root
        self.root.title("DIGITAL CLOCK")
        self.root.iconbitmap("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Students\\icon\\lista.ico")
        self.root.geometry("300x100")
        self.root.resizable(0,0)
        self.root.iconbitmap("iconn.ico")


        Main_Frame=Frame(self.root,width=300,height=100,relief=RIDGE,bd=3,bg="black")
        Main_Frame.place(x=0,y=0) 

        Lab_Date_now=Label(Main_Frame,text=todaydate,font=('times new roman',21,"bold"),bg="black",fg="cyan3")
        Lab_Date_now.place(x=80,y=0)

        def times():
            Lab_Time_now=Label(Main_Frame,font=('times new roman',31,"bold"),bg="black",fg="cyan3")
            time_strf=time.strftime("%H:%M:%S %p")
            Lab_Time_now.config(text=time_strf)
            Lab_Time_now.after(1000,times)
            Lab_Time_now.place(x=30,y=40)
        times()




if __name__=="__main__":
    root=Tk()
    app=Digital(root)
    root.mainloop()


##def stop():
##    import time
##    a=0
##    hours=0
##    while a<1:
##        for hours in range(0,25):
##            for minutes in range(0,60):
##                for seconds in range(0,60):
##                    time.sleep(1)
##                    print(hours,":",minutes,":",seconds)
##    hours+=1

#stop()
