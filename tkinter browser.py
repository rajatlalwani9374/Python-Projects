from tkinter import *
from six.moves import urllib
def go():
	text.delete(1.0, END)
	response = urllib.request.urlopen(entry.get())
	received_html = response.read()
	text.insert(1.0, received_html)

browser_window = Tk()
browser_window.title('Rajat Lalwani')
label = Label(browser_window, text= 'Enter URL:')
entry = Entry(browser_window)
entry.insert(END, "http://google.com")
button = Button(browser_window, text='Go', command = go)
text = Text(browser_window)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
browser_window.mainloop()
