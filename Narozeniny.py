def narozeniny():

	from datetime import date
	global year
	global month
	global day

	today = date.today()

	#--YEAR-------------------------------------------------------------
	year = (input("Ktery rok jsi se narodil/a? "))

	def year_test():
		global year
		while (year.isdigit() == False):
			year = input("Rok musí být kladné číslo. Zkus to znovu: ")
		year = int(year)
	year_test()

	def year_test_2():
		global year
		while (year > today.year):
			year = (input("Tak to se teprve narodis! Zkus to znovu: "))
			year_test()
			year = int(year)
	year_test_2()

	while (year < (today.year - 120)):
		year = (input("Tak to ti je víc jak 120 let! Zkus to znovu: "))
		year_test()
		year_test_2()
		year = int(year)
	#--------------------------------------------------------------------

	#--MONTH-------------------------------------------------------------
	month = (input("Kolikátý mesic? "))

	def month_test():
		global month
		while (month.isdigit() == False):
			month = input("Měsíc musíš zadat jako číslo. Zkus to znovu: ")
		month = int(month)

	month_test()

	while (month > 12) or (month < 1):
		month = (input("Takovy mesic neexistuje! Zkus to znovu: "))
		month_test()
		month = int(month)
	#--------------------------------------------------------------------

	#--DAY---------------------------------------------------------------
	day = (input("Kolikateho? "))

	def day_test():
		global day
		while (day.isdigit() == False):
			day = input("Musíš zadat číslo. Zkus to znovu: ")
		day = int(day)

	day_test()

	if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
		while (day > 31) or (day < 1):
			day = (input("Takový den v daném měsíci není. Zkus to znovu: "))
			day_test()
			day = int(day)
	if (month == 4) or (month == 6) or (month == 9) or (month == 11):
		while (day > 30) or (day < 1):
			day = (input("Takový den v dan19ém měsíci není. Zkus to znovu: "))
			day_test()
			day = int(day)
	if (month == 2):
		if ((year % 4) == 0) and ((year % 100) == 0) and ((year % 400) == 0):
			while (day > 29) or (day < 1):
				day = (input("Takový den v daném měsíci není. Zkus to znovu: "))
				day_test()
				day = int(day)
		elif ((year % 4) == 0) and ((year % 100) != 0):
			while (day > 29) or (day < 1):
				day = (input("Takový den v daném měsíci není. Zkus to znovu: "))
				day_test()
				day = int(day)
		else:
			while (day > 28) or (day < 1):
				day = (input("Takový den v daném měsíci není. Zkus to znovu: "))
				day_test()
				day = int(day)
	#--------------------------------------------------------------------

	#--ZJISTENI DNE V TYDNU------------------------------------------------------
	birth = date(year, month, day)
	weekdays = ["v pondeli.","v utery.","ve stredu.","ve ctvrtek.","v patek.","v sobotu.","v nedeli.",]
	birth_weekday = weekdays[birth.weekday()]
	#-------------------------------------------------------------------------

	#--ZJISTENI, KDO MEL SVATEK-----------------------------------------------
	month_days = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
	name_in_file = (month_days[month-1] + day)-1

	f = open("Svatky.txt","r")
	if f.mode =='r':
		global name
		lines = f.readlines()
		name = lines[name_in_file]
	#--------------------------------------------------------------------------

	#--ZNAMENI ZVEROKRUHU------------------------------------------------------
	birth_in_year = date(1 ,month, day)
	if (date(1,3,21) <= birth_in_year <= date(1,4,20)):
		znameni = "Beran"
	if (date(1,7,23) <= birth_in_year <= date(1,8,22)):
		znameni = "Lev"
	if (date(1,11,23) <= birth_in_year <= date(1,12,21)):
		znameni = "Střelec"
	if (date(1,4,21) <= birth_in_year <= date(1,5,21)):
		znameni = "Býk"
	if (date(1,8,23) <= birth_in_year <= date(1,9,22)):
		znameni = "Panna"
	if (date(1,12,22) <= birth_in_year <= date(1,12,31)) or (date(1,1,1) <= birth_in_year <= date(1,1,20)):
		znameni = "Kozoroh"
	if (date(1,5,22) <= birth_in_year <= date(1,6,21)):
		znameni = "Blíženec"
	if (date(1,9,23) <= birth_in_year <= date(1,10,23)):
		znameni = "Váhy"
	if (date(1,1,21) <= birth_in_year <= date(1,2,20)):
		znameni = "Vodnář"
	if (date(1,6,22) <= birth_in_year <= date(1,7,22)):
		znameni = "Rak"
	if (date(1,10,24) <= birth_in_year <= date(1,11,22)):
		znameni = "Štír"
	if (date(1,2,21) <= birth_in_year <= date(1,3,20)):
		znameni = "Ryba"
	#-------------------------------------------------------------------------

	#--VYPOCET VEKU----------------------------------------------------------

	if (birth < today):

		age = today.year - birth.year
		age_less = age - 1

		if (birth.month < today.month):
			print("")
			print("Je ti",age,"let.")
			print("Narodil/a jsi se",birth_weekday)
			print("Svátek ten den měl/a:",name)
			print("Znamením jsi",znameni)
		elif (birth.month > today.month):
			print("")
			print("Je ti",age_less,"let.")
			print("Narodil/a jsi se",birth_weekday)
			print("Svátek ten den měl/a:",name)
			print("Znamením jsi",znameni)
		else:
			if (birth.day < today.day):
				print("")
				print("Je ti",age,"let.")
				print("Narodil/a jsi se",birth_weekday)
				print("Svátek ten den měl/a:",name)
				print("Znamením jsi",znameni)
			elif (birth.day > today.day):
				print("")
				print("Je ti",age_less,"let.")
				print("Narozeniny máš za",birth.day - today.day,"dní.")
				print("Narodil/a jsi se",birth_weekday)
				print("Svátek ten den měl/a:",name)
				print("Znamením jsi",znameni)
			else:
				print("")
				print("Dnes máš narozeniny! Je ti",age,"let.")
				print("Narodil/a jsi se",birth_weekday)
				print("Svátek ten den měl/a:",name)
				print("Znamením jsi",znameni)

	else:
		print("No tak to jsi se jeste nenarodil/a!")

if __name__ == "__main__":
	narozeniny()