def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))

    k = 3.9

    for i in range(10):
        x = k * x * (1 - x)
        print(x)

main()