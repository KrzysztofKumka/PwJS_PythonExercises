from xml.dom import minidom

def parseDOM(path):
    doc = minidom.parse(path)
    name = doc.getElementsByTagName("name")[0]
    print(name.firstChild.data)

    read = doc.getElementsByTagName("movie_info")
    for read in read:
        title = read.getAttribute("Title")
        description = read.getElementsByTagName("Description")[0]
        year = read.getElementsByTagName("Year")[0]
        print("Title: %s, Description: %s, Year: %s" % (title, description.firstChild.data, year.firstChild.data))


def appendDOM(path):
    filepath = path
    xmldoc = minidom.parse(filepath)

    xmldoc.getElementsByTagName("Description")[0].childNodes[0].nodeValue = "Great movie"

    with open("modifiedxmlfile.xml", "w") as fs:
        fs.write(xmldoc.toxml())
        fs.close()


def main():
    parseDOM("movie_library.xml")

    appendDOM("movie_library.xml")

if __name__ == "__main__":
    main()