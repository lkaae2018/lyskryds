#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep 

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVgul=LED(20)
EVgreen=LED(16)

EVred.off()
EVgreen.off()
EVgul.off()
NSred.off()
NSgreen.off()
NSgul.off()

def redred(x):# Udgangs punkt for lyskrydset
    if x=="NS": #Hvis lyskrydset kommer fra NS skal den gå til EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        EVred.on()
        sleep(2)
        return EV(x)
    elif x=="EV": #Hvis lyskrydset kommer fra EV skal den gå til NS
        x="NS"
        print("NS red   EV red")
        NSred.on()
        EVred.on()
        sleep(2)
        return NS(x)

def NS(x): #NS gul lyser sammen med rød
    NSgul.on()
    sleep(2)
    NSred.off() #NS rød og NS gul slukker
    NSgul.off()
    return NSgreenst()
    
def NSgreenst():# Grænt lys tænder og slukker efte 5 sek.
    NSgreen.on() 
    sleep(5)
    NSgreen.off()
    return NSgulst()

def NSgulst(): # Gul tænder og slukker efter 2 sek.
    NSgul.on()
    sleep(2)
    NSgul.off()
    x="NS"
    return redred(x)

def EV(x):
    EVgul.on()
    sleep(2)
    EVred.off()
    EVgul.off()
    return EVgreenst()

def EVgreenst():
    EVgreen.on()
    sleep(5)
    EVgreen.off()
    return EVgulst()
    
def EVgulst():
    EVgul.on()
    sleep(2)
    EVgul.off()
    x="EV"
    return redred(x)


state=redred(x="EV")
while state: state=redred(x="EV")

