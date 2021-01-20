def main():
    print('Enter your name, surname and year of birth: ')
    x, y, z = map(str, input().split())
    print('Name: ' + x + '\nSurname: ' + y + '\nYear of birth: ' + z)



if __name__ == "__main__":
   main()