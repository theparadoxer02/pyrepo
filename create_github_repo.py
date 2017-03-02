import mechanize
import cookielib

repo_name = input("Enter the repository name ")

try:
	br=mechanize.Browser()
	cj=cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
except:
	print(" Error Generating Browser ")

br.set_handle_robots(False)

r=br.open('http://github.com/login')

br.select_form(nr=0)
br.form['login']='#username'
br.form['password']='#password'
br.submit()

r=br.open("http://github.com/new")
br.select_form(nr=3)
br.form['repository[name]']=repo_name
br.form['repository[description]']='made by mechaize'

br.submit()
