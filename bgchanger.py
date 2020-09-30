
# ----------------------------- #
#								#
#								#
#	 	CREATED BY Beaver		#
#								#
#		`````````````````````	#
#		`BACKGROUND CHENGER	`	#
#		`					`	#
#		`````````````````````	#
#       Version 1.0 alfa        #
#								#
# ----------------------------- #


# Welcome window


print(" ")
print(" ")
print(" ")



print('       **************CHANGE LOGOUT BACKGROUND***************')

print(" ")

print("--Version 1.0 Alfa")

print(" ")
print(" ")

#Window man.md
man = open('man.md', mode='r', encoding='UTF-8')
print(man.read())

print(" ")
print(" ")


#programm
print('What image do you want to put on the background?')

print ('Place the image in the program folder. Path: "./bgchanger/')

print('Be sure to enter its format!')

print(" ")
print(" ")

print('Image name: ')


img = str(input())

#print("В новом окне терминала введите команду: cp imagename.jpg /usr/share/backgrounds/" + img )MB

print(" ")
print(" ")
print(" ")

print('Enter the commands: ')

print(" ")
print(" ")


print('sudo su')
print('sudo cp',img , '/usr/share/backgrounds/')
print('exit')
print('cd')
print('sudo ./ubuntu-20.04-change-gdm-background /usr/share/backgrounds/'+img)
	