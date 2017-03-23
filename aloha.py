from tkinter import *
import tkinter.simpledialog as inp
import tkinter.messagebox as out
import random
s=[]
r=[]
st=[]
ft=[]
root=Tk()
root.geometry("3000x1000")
root["bg"]="black"

w=Label(root,text="PURE ALOHA",fg="Purple",font=("Times New Roman",30))
w.pack()
out.showinfo("","WELCOME TO ALOHA PROTOCOL IMPLEMENTATION ")
n=inp.askinteger("n","Enter number of nodes")
k=[0]*n
out.showinfo("","ENTER SENDER AND CORRESPONDING RECEIVER ")
for i in range(n):
    a=inp.askstring("a","Enter sender")
    s.append(a)
    b=inp.askstring("b","Enter receiver")
    r.append(b)
#print(s)
#print(r)
for i in range(n):
    start=inp.askinteger("start","Enter start time when frame is sent from node "+s[i])
    st.append(start)
#print(st)
t=3
for i in range(n):
    finish=st[i]+t
    ft.append(finish)
st.sort()
ft.sort()
i=0
j=i+1
while(len(st)>1):
    out.showinfo("","Sending frame from node "+s[i]+" to "+r[i])
    if ft[i]>st[j]:
        out.showinfo(""," Collision Occured ")
        nk=k[0]+1
        k[0]=nk
        if k[i]>15:
            out.showinfo("","Frame "+str(i)+"is aborted as tries has exceeded 15")
        ra=random.randint(0,2**k[i]-1)
        del(st[i])
        del(ft[i])
        del(k[i])
        st.append(ra)
        st.sort()
        ke=st.index(ra)
        ft.insert(ke,ra+t)
        k.insert(ke,nk)
        m=s[i]
        n=r[i]
        del(s[i])
        del(r[i])
        s.insert(ke,m)
        r.insert(ke,n)
    else:
        out.showinfo("","No Collision has occured")
        out.showinfo("","Frame delivered from "+s[i]+" to "+r[i]+" at trial "+str(k[i]+1))
        del(st[i])
        del(ft[i])
        del(s[i])
        del(r[i])
        del(k[i])
if len(st)==1:
    out.showinfo("","Sending frame from node "+str(s[0])+" to "+str(r[0]))
    out.showinfo("","No collision occured")
    out.showinfo("","Frame delivered from "+s[0]+" to "+r[0]+" at trial "+str(k[0]+1))
root.mainloop()

