import base64,marshal,os,click
from uncompyle6 import main

class Com:
	def __init__(self,fil,jum):
		self.file=fil
		self.cout=0
		self.jml=jum
		self.mars(open(fil,'r').read())

	def mars(self,strg):
		x=compile(strg,'<script>','exec')
		xx=marshal.dumps(x)
		xxx=f"#Compile\n# bcsetris7\n\nimport marshal\nexec(marshal.loads({xx}))"
		if self.cout == self.jml:
			with open(self.file.replace('.py','_comlap.py'),'w') as com:
				com.write(xxx)
			print(f"[+] File tersimpan: {self.file.replace('.py','_marshal.py')}")
			return True
		self.bes(xxx)

	def bes(self,strg):
		en=base64.b64encode(bytes(strg,'utf-8'))
		de=f"#ok\n\nimport base64\nexec(base64.b64decode({en}).decode('utf-8','ignore'))"
		self.cout+=1
		self.mars(de)

os.system('clear')
print("""
	amankan coding anda lebih mantap ! code by bcsetris7""")
try:
	ofile=input("[?] File ORI: ")
	juml=int(input("[?] Jumlah compile: "))
	if juml > 10:
		click.pause("[WARM] Anda memasukan jumlah lebih dari 10, itu bisa membuat size file membengkak! [ENTER]")
	Com(ofile,juml)
	pil=input("[?] Compile ke bytes code (y/n) ")
	if pil.lower() == 'y':
		main.compile_file(ofile.replace('.py','_comlap.py'))
		print("[DONE]")
	else:
		print("[DONE]")
except KeyboardInterrupt:
	print("[Key Interrupt]")
except Exception as F:
	print(f"[Err] {str(F)}")
