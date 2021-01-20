import os

def file_count(d):
    count = 0
    for path in os.listdir(d):
        if os.path.isfile(os.path.join(d, path)):
            count += 1
    print(count-1)


def main():
    path = ""
    file_count(path)

if __name__ == '__main__':
    main()