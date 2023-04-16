import matplotlib.pyplot as plt
import pandas as pd
dataframe = pd.read_csv(r'C:\Users\dhanu\Downloads\autos.csv', encoding = "ISO-8859-1")
print(dataframe)
print("temp", dataframe["seller"].unique())
print("Private, Business")
print("temp1", dataframe["offerType"].unique())
print("Offer ,Petition")
print("temp2", dataframe["nrOfPictures"].unique())
print("**********************************************************************************************")
ans1 = dataframe["price"].mean()
print("3.a. ",ans1)
print("**********************************************************************************************")

ans2 = dataframe["vehicleType"].unique()
print("3.b ",ans2)
print("**********************************************************************************************")


dataframe.drop(dataframe[dataframe['yearOfRegistration'] >= 2023].index, inplace = True) #As there are junk values like 9999 for year, I have removed all values which are greater than 2023.
dataframe.drop(dataframe[dataframe['yearOfRegistration'] <= 1886].index, inplace = True) #As there are junk values like 1000, I have given this constraint because the first car was manufactured on 1886.

ans31 = dataframe["yearOfRegistration"].max()
ans32 = dataframe["yearOfRegistration"].min()
print("3.c1 Max Year of registration ", ans31)
print("3.c2 Min Year of registration ", ans32)
print("**********************************************************************************************")


ans4 = dataframe["kilometer"].std()
print("3.d Standard Deviation ", ans4)
print("**********************************************************************************************")


ansidk = dataframe['brand'].value_counts().to_dict()
print(ansidk)
brandvalues = list(ansidk.values())
brandkeys = list(ansidk.keys())
plt.pie(brandvalues, labels=brandkeys)
plt.pie(brandvalues, labels=brandkeys, autopct=lambda p:f'{p*sum(brandvalues)/100 :.0f} ')
#plt.show()



ans5 = dataframe['vehicleType'].value_counts().to_dict()
print(ans5)
values = list(ans5.values())
keys = list(ans5.keys())
ans51 = keys[values.index(max(values))]
ans52 = keys[values.index(min(values))]
print("3.f1 ", ans51)
print("3.f2 ", ans52)
print("**********************************************************************************************")

ans6 = dataframe['gearbox'].value_counts().to_dict()
#print(ans6)
gearboxvalues = list(ans6.values())
gearboxkeys = list(ans6.keys())
plt.pie(gearboxvalues, labels=gearboxkeys, autopct=lambda p:f'{p*sum(gearboxvalues)/100 :.0f} ')
#plt.show()






