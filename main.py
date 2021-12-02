import re, random,time
#---------------------
def append_jecna_postfix(string):
        string = str(string)
        string += "@spsejecna.cz"
        return string

def append_seznam_postfix(string):
        string = str(string)
        string += "@seznam.cz"
        return string

# print(append_jecna_postfix("c12"))
# print(append_seznam_postfix("c12"))
#
# appender_postfix = append_jecna_postfix
#
# print(appender_postfix("novak"))
#
# appender_postfix = append_seznam_postfix
#
# print(appender_postfix("novak"))

#-----------------------

# def create_email(appender_function, username):
#         username = str(username)
#         print(appender_function(username))
#
# appender_postfix = append_jecna_postfix
# create_email(appender_postfix, "novak")
# #ma vratit novak@spsejecna.cz
# appender_postfix = append_seznam_postfix
# create_email(appender_postfix, "novak")
# #ma vratit novak@seznam.cz

#------------------------

# def formatuj_prijmeni_prvni(jmeno, prijmeni):
#         print((prijmeni,jmeno))
#
# def formatuj_monogram(jmeno, prijmeni):
#         jmeno = jmeno[0]
#         prijmeni = prijmeni[0]
#         print(jmeno, prijmeni)
#
# formatuj_monogram("novak","kik")
#
# def vyber_formatovaci_funkci(delka):
#         if delka <4:
#                 return formatuj_monogram
#         else:
#                 return formatuj_prijmeni_prvni
#
# formatovac = vyber_formatovaci_funkci(3)
# formatovac("Jan","Novak")
# formatovac = vyber_formatovaci_funkci(155)
# formatovac("Jan", "Novak")

#------------------------
#
# def toBig(string):
#         return string.upper()
#
# def spaceToSmile(string):
#         string = re.sub(' +',':-)' ,string)
#         return string
#
# def vTow(string):
#         string = re.sub('v','w',string)
#         return string
#
# def addStars(string):
#         string = '*' + string + '*'
#         return string
#
# def expressionOfFeelings(string):
#         string = re.sub('!','!!!!!',string)
#         string = re.sub('\?','???',string)
#         return string
#
# funky_functions = [toBig,spaceToSmile,vTow,addStars,expressionOfFeelings]
# def funky_format(text):
#         return funky_functions[random.randrange(0, len(funky_functions)-1)](text)
#
# print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))

#------------------------

# def generuj_nasobici_funkci(krok):
#     def pricitej(cislo):
#         return cislo*krok
#     return pricitej
#
# nasob_nulou = generuj_nasobici_funkci(0)
# nasob_minus_jednickou = generuj_nasobici_funkci(-1)
# nasob_sedmnacti = generuj_nasobici_funkci(17)
# nasob_devetsetdevatenacti = generuj_nasobici_funkci(919)
#
# print(nasob_sedmnacti(1))
# print(nasob_nulou(2))
# print(nasob_devetsetdevatenacti(3))

#------------------------

# def formatuj_cele_jmeno(jmeno, prijmeni):
#     return jmeno + " " + prijmeni
#
# def formatuj_zkracene_jmeno(jmeno, prijmeni):
#     return jmeno[0] + ". " + prijmeni
#
# def wrapper_velka_pismena( f ):
#         def formatuj_velka_pismena(jmeno, prijmeni):
#                 vysledek = f(jmeno, prijmeni)
#                 return vysledek.upper()
#         return formatuj_velka_pismena
#
# cele_jmeno_velkymi = wrapper_velka_pismena(formatuj_cele_jmeno)
# print (cele_jmeno_velkymi("jan", "novak"))
#
# zkrace_velkymi = wrapper_velka_pismena(formatuj_zkracene_jmeno)
# print (zkrace_velkymi("jan", "novak"))
#

#------------------------

# def wrapper_velka_pismena( f ):
#         def formatuj_velka_pismena(jmeno, prijmeni):
#                 vysledek = f(jmeno, prijmeni)
#                 return vysledek.upper()
#         return formatuj_velka_pismena
#
# @wrapper_velka_pismena
# def formatuj_cele_jmeno(jmeno, prijmeni):
#     return jmeno + " " + prijmeni
#
# @wrapper_velka_pismena
# def formatuj_zkracene_jmeno(jmeno, prijmeni):
#     return jmeno[0] + ". " + prijmeni
#
# print(formatuj_cele_jmeno("jan", "novak"))
#
#
# print(formatuj_zkracene_jmeno("jan", "novak"))

#------------------------

# def wrapper_repeat(f):
#     def twice():
#         f()
#         f()
#     return twice
# @wrapper_repeat
# def hellowordl():
#     print("hello world")
#
# hellowordl()

#------------------------

# def elapsed_time(chupapi):
#         start_time = time.time()
#         chupapi()
#         end_time = time.time()
#         print("Vypocet trval " + str((end_time - start_time)) + "sec")
#
# @elapsed_time
# def tri_na_sedm_milionu():
#     return 3 ** 7000000



