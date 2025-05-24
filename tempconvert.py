import sys
def faren_cels(faren):
    cels=(faren-32)/1.8
    return cels;

def cels_faren(cels):
    faren=cels*1.8+32
    return faren;

print("Menu")
print("1.Farenheit to Celsius")
print("2.Celsius to Farenheit")
print("3.Exit")
ch=int(input("Enter your choice:\n"))

if(ch==1):
    faren=int(input("Enter the value of farenheit"))
    cels=faren_cels(faren)
    print(cels);

elif (ch==2):
    cels=int(input("Enter the value of celsius"))
    faren=cels_faren(cels)
    print(faren);

else:
    sys.exit()