# please note that by mistake I deleted the in.txt file given in question and then the internet got disabled, hence I am making a file of my own. The code would work for all files of the format of in.txt

with open("2022073._Aniket/in.txt") as f:
    main_lst = []
    for line in f:
        lst = [str((int(c))**2) for c in line.strip().split()]
        main_lst.append(lst)

with open("2022073._Aniket/out.txt", 'w') as f:
    for c in main_lst:
        print(c)
        s = ""
        for d in c:
            s += d + ' '
        f.write(s+'\n')
