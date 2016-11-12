#! /usr/bin/env python
# simple tool for calculating Duration
# Adel Rahimi

Drise = int(input("enter rise duration? ")) #Number
Dfall = int(input("fall duration duration? ")) #Number

tilt_dur = (Drise - Dfall) / (Drise + Dfall)

print ("tilt duration is", tilt_dur)

