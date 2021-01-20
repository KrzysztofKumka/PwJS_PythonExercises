import os

def catalogue_structure(path):
    for root, dirs, files in os.walk(path):
        l1 = root.replace(path, '').count(os.sep)
        l2 = ' ' * (l1 + 15)
        print('{}{}/'.format(l2, os.path.basename(root)))
        l3 = ' ' * (l1 + 20)

        for f in files:
            print('{}{}'.format(l3, f))

if __name__ == "__main__":
    catalogue_structure("//path//")