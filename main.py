print("""
        .oooooo..o   .oooooo.      ooooo     ooo       .o.       ooooooooo.   oooooooooooo            .o.       ooooooooo.   ooooooooo.   
       d8P'    `Y8  d8P'  `Y8b     `888'     `8'      .888.      `888   `Y88. `888'     `8           .888.      `888   `Y88. `888   `Y88. 
       Y88bo.      888      888     888       8      .8"888.      888   .d88'  888                  .8"888.      888   .d88'  888   .d88' 
        `"Y8888o.  888      888     888       8     .8' `888.     888ooo88P'   888oooo8            .8' `888.     888ooo88P'   888ooo88P'  
            `"Y88b 888      888     888       8    .88ooo8888.    888`88b.     888    "           .88ooo8888.    888          888         
      oo     .d8P `88b    d88b     `88.    .8'   .8'     `888.   888  `88b.   888       o       .8'     `888.   888          888         
      8""88888P'   `Y8bood8P'Ybd'    `YbodP'    o88o     o8888o o888o  o888o o888ooooood8      o88o     o8888o o888o        o888o       
                                                                                                                                    ©Madesh.Inc""")
print("    ")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("The addition of two numbers",num1+num2)

        elif choice == '2':
            print("The Subtract of two numbers",num1-num2)

        elif choice == '3':
            print("The Multiply of two numbers",num1*num2)

        elif choice == '4':
            print("The Divide of two numbers",num1/num2)

        elif choice == '5':
            print("The square of two numbers",num1**num2)
        break
    else:
        print("Invalid Input")