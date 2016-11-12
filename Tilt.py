#! /usr/bin/env python

# calculating Tilt based on amplitude

# First we define Arise, Afall, Drise, And Dfall

Arise = int(input("enter Amplitude rise? ")) #Number

Afall = int(input("enter amplitude fall? ")) #Number

Drise = int(input("enter duration rise? ")) #Number

Dfall = int(input("enter duration fall? ")) #Number

tilt = (( abs(Arise) - abs(Afall) ) / 2 * ( abs(Arise) + abs(Afall) )) + (( Drise - Dfall ) / 2 * (Drise + Dfall))

print ("the tilt is", tilt )
