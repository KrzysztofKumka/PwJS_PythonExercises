import json


def createFile(str_name):
    data = []
    end_str = ""
    while(end_str != "exit"):

        mov_name = input("Enter the name of the movie you'd like to review or type exit: ")
        if(mov_name != "exit"):
            review = input("Write a short review of the movie called " + mov_name + ": ")

            data.append({
                'name': mov_name,
                'review': review
            })

        if(mov_name == "exit"):
            end_str = "exit"

    with open(str_name+'.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',', ': '))

def appendFile(str_name):
    with open(str_name + '.json') as json_file:
        data = json.load(json_file)
        end_str = ""
        while (end_str != "exit"):
            mov_name = input("Enter the name of the movie you'd like to review or type exit: ")
            if (mov_name != "exit"):
                review = input("Write a short review of the movie called " + mov_name + ": ")

                data.append({
                    'name': mov_name,
                    'review': review
                })

            if (mov_name == "exit"):
                end_str = "exit"

        with open(str_name + '.json', 'w') as f:
            json.dump(data, f, indent=4, separators=(',', ': '))

def deleteFile(str_name):
    deletemovie_name = input("Enter the name of the movie you'd like to delete from library: ")

    json_file = json.load(open(str_name + '.json'))

    for i in range(len(json_file)):
        if json_file[i]["name"] == deletemovie_name:
            json_file.pop(i)
            break

    open(str_name + '.json', 'w').write(json.dumps(json_file, sort_keys=True, indent=4, separators=(',', ': ')))

def returnFile(str_name):
    with open(str_name + '.json', 'r') as json_file:
        parsed_file = json.load(json_file)
        print(json.dumps(parsed_file, indent=4, sort_keys=True))



def main():
    print("Operating JSON data, MOVIE LIBRARY")
    print("\n")
    print("Press 1 to create new movie library (new JSON file). \n"
          "Press 2 to append data to existing movie library (edit JSON file).\n"
          "Press 3 to delete data from existing movie library (edit JSON file).\n"
          "Press 4 to print existing movie library (print JSON file).\n")

    choice = input(": ")

    if (choice == "1"):
        print("Enter the name of JSON file\n")
        name = input(": ")
        createFile(name)

    elif (choice == "2"):
        print("Enter the name of JSON file\n")
        name = input(": ")
        appendFile(name)


    elif (choice == "3"):
        print("Enter the name of JSON file\n")
        name = input(": ")
        deleteFile(name)

    elif (choice == "4"):
        print("Enter the name of JSON file\n")
        name = input(": ")
        returnFile(name)


    else:
        exit()


if __name__ == "__main__":
   main()