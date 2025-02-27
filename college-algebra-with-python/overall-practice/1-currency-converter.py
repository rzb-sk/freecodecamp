# This is a simple currency converter using ratios and proportions lesson

# USD to INR

# current rate for USD to INR
usd = 1
inr = 87.31

# how much to convert
usd_to_convert = float(input("Please enter the amount to convert in USD: "))

inr_after_convert = usd_to_convert * inr

print("INR after conversion is :", inr_after_convert)
