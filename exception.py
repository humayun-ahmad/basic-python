while True:
    try:
        number  = int(input("What is your fav number hoss ? \n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure enter your number\n")
    except ZeroDivisionError:
        print("Don't enter zero")
    except:
        break
    finally:
        print("Loop complete\n")