from built_functions import *
import threading


start=int(input("Enter number where to start="))
end=int(input("Enter end point="))

mid=(start+end)//2

if __name__=="__main__":
    t1=threading.Thread(target=main,args=(start,mid))
    t2=threading.Thread(target=main,args=(mid+1,end+1))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("Done Sucessfully")



