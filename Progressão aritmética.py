r=[]
o=int(input("Qual a ordem da progressão aritmética? "))
for k in range(1, o+1):
	z=int(input("Digite a razão de ordem n°{}: ".format(k)))
	r.append(z)
n=int(input("Quantos números mostrar? "))
c=int(input("Primeiro termo: "))
for n in range(0, n):
	print(c, end=" ")
	q=2
	i=len(r)-q
	for k in range(1, len(r)):
		i=len(r)-q
		r[i]=r[i]+r[i+1]
		q=q+1
	c=c+r[i]