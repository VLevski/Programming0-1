say = input("Say what you have to say: ")

answer = "@"
if "hello" in say:
	answer = answer + "H"
if "how are you?" in say:
	answer = answer + "h"
if "feelings"	in say:
	answer = answer + "F"
if "age" in say:
	answer = answer + "A"

H = "Hello there, good stranger! "
h = "I am fine, thanks for asking! How are you? "
F = "Because I'm a machine I have no feelings "
A = "I've no age - only current time-stamp "

# Truth table:	
#	H	h	F	A
#---------------------------------
#	0	0	0	0
#	0	0	0	1
#	0	0	1	0
#	0	0	1	1
#	0	1	0	0
#	0	1	0	1
#	0	1	1	0
#	0	1	1	1
#	1	0	0	0
#	1	0	0	1
#	1	0	1	0
#	1	0	1	1
#	1	1	0	0
#	1	1	0	1
#	1	1	1	0
#	1	1	1	1

if answer == "@HhFA":
	print(H + h + F + A)
elif answer == "@HhF":
	print(H + h + F)
elif answer == "@HhA":
	print (H + h + A)
elif answer == "@Hh":
	print(H + h)
elif answer == "@HFA":
	print(H + F + A)
elif answer == "@HF":
	print(H + F)
elif answer == "@HA":
	print(H + A)
elif answer == "@H":
	print(H)
elif answer == "@hFA":
	print(h + F + A)
elif answer == "@hF":
	print(h + F)
elif answer == "@hA":
	print(h + A)
elif answer == "@h":
	print(h)
elif answer == "@FA":
	print(F + A)
elif answer == "@F":
	print(F)
elif answer == "@A":
	print(A)
else:
	print("What you meen?")

