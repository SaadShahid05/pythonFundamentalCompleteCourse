farenheitInp = int(input("enter how many farenheit there are: "))
celciusConverter = 5/9*(farenheitInp-32)
                       
print("this amounts to " + str(celciusConverter) + " celcius")


celciusInp = int(input("enter how many celcius there are: "))
farenheitConverter = (celciusInp*9/5)+32

print("this amounts to " + str(farenheitConverter) + " farenheit")
