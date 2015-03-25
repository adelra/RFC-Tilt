#! /usr/bin/env python

# calculating Tilt based on amplitude

# First we define Arise, Afall, Drise, And Dfall

Arise = 11 #Number

Afall = 32 #Number

Drise = 12 #Number

Dfall = 22 #Number

tilt = (( abs(Arise) - abs(Afall) ) / 2 * ( abs(Arise) + abs(Afall) )) + (( Drise - Dfall ) / 2 * (Drise + Dfall))

print ("the tilt is", tilt )
