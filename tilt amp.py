#! /usr/bin/env python
# simple tool for converting RFC prameters to Tilt prameter
# Adel Rahimi

# we have to define A Rise
arise = 12 #number

# We have to define A Fall
afall = 22 #number

tilt_amp = (abs(arise) - abs(afall))/ (abs(arise) + abs(afall))

print (tilt_amp)
