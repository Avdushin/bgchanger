
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

#It's jus a russian version of programm

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
print('Какое изображение хотите поставить на фон?')
print('Поместите изображение в папку программы. Путь: "./bgchanger/')

print('Обязательно введите его формат!')
print('Имя изображения:')

img = str(input())

#print("В новом окне терминала введите команду: cp imagename.jpg /usr/share/backgrounds/" + img )MB

print(" ")
print(" ")
print(" ")

print('Введите команды: ')

print(" ")
print(" ")


print('sudo su')
print('sudo cp',img , '/usr/share/backgrounds/')
print('exit')
print('cd')
print('sudo ./ubuntu-20.04-change-gdm-background /usr/share/backgrounds/'+img)
	