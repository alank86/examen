cadena=raw_input('introduce una palabra:')
def getVocales(cadena):
	vocales=cadena
	for char in cadena:
		if char in 'aeiouAEIOU':
			vocales = vocales + char
	print vocales
