class Konto:

	antal_konton = 0

	def __init__(self, kontonr, efternamn, namn, fodelsedata, kredit, saldo):
		self.__kontonr = kontonr
		self.__efternamn = efternamn
		self.__namn = namn
		self.__fodelsedata = fodelsedata
		Konto.antal_konton += 1
		
		if kredit % 1000 != 0:
			raise Exception("Krediten måste vara jämt delbart med 1000, försök igen")
		else:
			self.__kredit = kredit

		if saldo < 0 and abs(saldo) > self.__kredit:
			raise Exception("Otillräcklig kredit")
		else:
			self.__saldo = saldo

	def lagg_till_pengar(self, pengar):

		if pengar < 0:
			print("Det går inte att sätta in negativa värden")
		else:
			self.__saldo += pengar

	def ta_ut_pengar(self, uttag):
		nytt_saldo = self.__saldo - uttag

		if nytt_saldo < 0 and abs(self.__saldo) > self.__kredit:
			print("Otillräcklig kredit")
		else:
			self.__saldo = nytt_saldo
			print("Nytt saldo: ", nytt_saldo)

	def kolla_saldo(self):
		return self.__saldo

	def satt_kredit(self, ny_kredit):

		if self.__saldo < 0 and abs(self.__saldo) > ny_kredit:
			print("Saldot är för lågt, försök igen.")
		elif ny_kredit % 1000 != 0:
			print("Krediten måste vara jämt delbart med 1000")
		else:
			self.__kredit = ny_kredit

	def stanga_konto(self):
		if self.__saldo == 0:
			return True
		else:
			print("Saldot måste vara noll")

	def kontonr(self):
		return self.__kontonr

