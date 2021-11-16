from PIL.Image import EXTENSION
from python import conversions
import tkinter as tk
from tkinter import filedialog
import os
dir=os.getcwd()
def help():
    pass
def load():
    print("Choose an image File from the popup menu")
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames()
    try:
        width,height=conversions.imgtohex(files[0])
    except:
        print("Please Select valid file")
    print("Image Loaded Successfully\n")
    processMenu(width,height)
def processMenu(width,height):
    while 1:
        print("Select a filter")
        print("1. Grayscale")
        print("2. Sepia")
        print("3. Blur")
        print("4. Increase/Decrease Brightness ")
        print("5. Crop ")
        print("6. Main Menu")
        choice = int(input("Your choice: "))
        if (choice==1):
            try:
                print("Processing Image!")
                command="iverilog ./verilog/greyscale.v"
                os.system(command)
                print("Please wait! It may take longer time depending on the quality of the image")
                command="vvp a.out"
                os.system(command)
                print("Processing complete! Please select a location to save from the popup menu")
                root = tk.Tk()
                root.withdraw()
                file = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes= [('JPG','.jpg'), ('BMP', '.bmp')])
                conversions.hextoimg(width,height,file)
            except:
                print("Please select valid location and file name")
                continue
        elif choice==2:
            try:
                print("Processing Image!")
                command="iverilog ./verilog/sepia.v"
                os.system(command)
                print("Please wait! It may take longer time depending on the quality of the image")
                command="vvp a.out"
                os.system(command)
                print("Processing complete! Please select a location to save from the popup menu")
                root = tk.Tk()
                root.withdraw()
                file = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes= [('JPG','.jpg'), ('BMP', '.bmp')])
                conversions.hextoimg(width,height,file)
            except:
                print("Please select valid location and file name")
                continue
        elif choice==3:
            try:
                print("Processing Image!")
                command="iverilog ./verilog/blur.v"
                os.system(command)
                print("Please wait! It may take longer time depending on the quality of the image")
                command="vvp a.out"
                os.system(command)
                print("Processing complete! Please select a location to save from the popup menu")
                root = tk.Tk()
                root.withdraw()
                file = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes= [('JPG','.jpg'), ('BMP', '.bmp')])
                conversions.hextoimg(width,height,file)
            except:
                print("Please select valid location and file name")
                continue
        elif choice ==4:
            try:
                print("Enter a value between -255 to 255(-ve value will decrease brightness)")
                brighness=int(input())
                f=open("./data/size.hex","w")
                sign=0
                if brighness<0:
                    brighness*=-1
                    sign=1
                f.write(hex(width)[2:]+"\n"+hex(height)[2:]+"\n"+hex(brighness)[2:]+"\n"+str(sign))
                f.close()
                print("Processing Image!")
                command="iverilog ./verilog/brightness.v"
                os.system(command)
                print("Please wait! It may take longer time depending on the quality of the image")
                command="vvp a.out"
                os.system(command)
                print("Processing complete! Please select a location to save from the popup menu")
                root = tk.Tk()
                root.withdraw()
                file = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes= [('JPG','.jpg'), ('BMP', '.bmp')])
                conversions.hextoimg(width,height,file)
            except:
                print("Please select valid location and file name")
                continue
        elif choice ==5:
            try:
                print("Enter 4 numbers seperated by space 'top bottom right left' ");
                top,bottom,right,left = list(map(int,input().split()));
                f=open("./data/size.hex","w")
                top = int(top/100*height);
                bottom = int(bottom/100*height);
                left= int(left/100*width);
                right = int(right/100*width);
                f.write(hex(width)[2:]+"\n"+hex(height)[2:]+ "\n"+ hex(top)[2:]+"\n"+hex(bottom)[2:]+"\n"+hex(left)[2:]+"\n" + hex(right)[2:]+"\n");
                f.close()
                print("Processing Image!")
                command="iverilog ./verilog/crop.v"
                os.system(command)
                print("Please wait! It may take longer time depending on the quality of the image")
                command="vvp a.out"
                os.system(command)
                print("Processing complete! Please select a location to save from the popup menu")
                root = tk.Tk()
                root.withdraw()
                file = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes= [('JPG','.jpg'), ('BMP', '.bmp')])
                conversions.hextoimg(width-(left+right),height-(top+bottom),file)
            except:
                print("Please select valid location and file name")
                continue
        else :
            break
        print("Image Saved!")
while (1):
    print("Main Menu")
    print("1. Load Image")
    print("2. Help")
    print("3. Quit")
    choice=int(input("Your choice: "))
    if choice==3:
        break
    if choice==1:
        load()
    if choice==2:
        help()