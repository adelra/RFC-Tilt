#! /usr/bin/env python
# simple tool for converting RFC prameters to Tilt prameter
# Adel Rahimi

# we have to define A Rise
arise = int(input("enter Amplitude rise? ")) #Number

# We have to define A Fall
afall = int(input("enter Amplitude fall? ")) #Number

tilt_amp = (abs(arise) - abs(afall))/ (abs(arise) + abs(afall))

print ("tilt amp is", tilt_amp)
