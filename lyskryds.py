#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from time import sleep 

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(21)
EVgul=LED(20)
EVgreen=LED(16)


print("Test!")
EVred.on()
sleep(1)
EVgreen.on()
sleep(1)
EVgul.on()
sleep(1)
NSred.on()
sleep(1)
NSgreen.on()
sleep(1)
NSgul.on()
sleep(1)
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
    sleep(1)
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
    sleep(1)
    NSgul.off()
    x="NS"
    return redred(x)

def EV(x):#EV gul lyser sammen med rød
    EVgul.on()
    sleep(1)
    EVred.off()
    EVgul.off()
    return EVgreenst()

def EVgreenst():# Grænt lys tænder og slukker efte 5 sek.
    EVgreen.on()
    sleep(5)
    EVgreen.off()
    return EVgulst()
    
def EVgulst():# Gul tænder og slukker efter 2 sek.
    EVgul.on()
    sleep(1)
    EVgul.off()
    x="EV"
    return redred(x)


state=redred(x="EV")
while state: state=redred(x="EV")

