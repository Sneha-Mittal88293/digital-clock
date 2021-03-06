from tkinter import *;
import datetime

def date_time():
    time = datetime.datetime.now()                #first datetime is for module name second datetime is a function
    hr = time.strftime('%I')                      # I is use for hour
    min =time.strftime('%M')
    sec =time.strftime('%S')
    am =time.strftime('%p')

    date = time.strftime('%d')                     
    month =time.strftime("%m")
    year =time.strftime('%y')
    day =time.strftime('%a')


    lab_hr.config(text = hr)
    lab_min.config(text = min)
    lab_sec.config(text = sec)
    lab_am.config(text = am)

    lab_date.config(text = date)
    lab_mon.config(text = month)
    lab_year.config(text = year)
    lab_day.config(text = day)

    lab_hr.after(200 , date_time)                                 #first parameter is change time in milisecond second is function name


clock = Tk()
clock.title('      **** DIGITAL CLOCK ****')     #title is  use for title name
clock.geometry('1000x500')                       #geometry is use for size of display
clock.config(bg='black')                       #config function give use configuration to change the colour ang bg is use for back ground colour

#   ******TIME

lab_hr = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')       # in  label function we can pass first parameter is class name 
lab_hr.place(x = 120 , y = 50 , height = 110 , width = 100 )
lab_hr_txt = Label(clock , text = "HOUR" , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')       # in  label function we can pass first parameter is class name 
lab_hr_txt.place(x = 120 , y = 190 , height = 40 , width = 100 ) 


lab_min = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_min.place(x = 340 , y = 50 , height = 110 , width = 100 )
lab_min_txt = Label(clock , text = "MIN." , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')      
lab_min_txt.place(x = 340 , y = 190 , height = 40 , width = 100 )


lab_sec = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_sec.place(x = 560 , y = 50 , height = 110 , width = 100 )
lab_sec_txt = Label(clock , text = "SEC." , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')      
lab_sec_txt.place(x = 560 , y = 190 , height = 40 , width = 100 )


lab_am = Label(clock , text = "00" , font =('Time New Roman' , 52 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_am.place(x = 780 , y = 50 , height = 110 , width = 100 )
lab_am_txt = Label(clock , text = "AM/PM" , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')      
lab_am_txt.place(x = 780 , y = 190 , height = 40 , width = 100 )

#    ********DATE

lab_date = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')       
lab_date.place(x = 120 , y = 270 , height = 110 , width = 100 )
lab_date_txt = Label(clock , text = "DATE" , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')     
lab_date_txt.place(x = 120 , y = 410 , height = 40 , width = 100 ) 


lab_mon = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_mon.place(x = 340 , y = 270 , height = 110 , width = 100 )
lab_mon_txt = Label(clock , text = "MONTH" , font =('Time New Roman' , 20 , "bold"), bg = 'red' , fg = 'white')      
lab_mon_txt.place(x = 340 , y = 410 , height = 40 , width = 100 )


lab_year = Label(clock , text = "00" , font =('Time New Roman' , 60 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_year.place(x = 560 , y = 270 , height = 110 , width = 100 )
lab_year_txt = Label(clock , text = "YEAR" , font =('Time New Roman' , 23 , "bold"), bg = 'red' , fg = 'white')      
lab_year_txt.place(x = 560 , y = 410 , height = 40 , width = 100 )


lab_day = Label(clock , text = "00" , font =('Time New Roman' , 38 , "bold"), bg = '#95B9C7' , fg = 'white')      
lab_day.place(x = 780 , y = 270 , height = 110 , width = 100 )
lab_day_txt = Label(clock , text = "DAY" , font =('Time New Roman' , 26 , "bold"), bg = 'red' , fg = 'white')      
lab_day_txt.place(x = 780 , y = 410 , height = 40 , width = 100 )


date_time()

clock.mainloop()
