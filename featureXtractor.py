import urllib.request


def main():
    print("\t\tfeatureXtractor VER:0.1")
    print("----------------------------------------------------------------------")
    print("\n\nHi!! I am ver 0.1");
    content = urllib.request.urlopen('http://www.python.org/')
    for l in content:
        print(l)
    

#if __name__=='__main()__':
#    main()
main()
