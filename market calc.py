
taxes  = 0.35

def calc(p,q,dis="no"):
	if q>1:
		p *=q 
	if dis == "yes" or dis == "y":
		return (p-(p*0.35))*1.3
	else:
		return p-(p*0.35)
		
def menu():
	while True:
		price = int(input("\n\n Enter the Price: ") or "1")
		qty = int(input("\n Enter the Quantity: ") or "1")
		pack = input("\n Do You have Value Pack (y/n)?: ").lower()
		print("\n Silver gained after taxes =", calc(price,qty,pack))

menu()
