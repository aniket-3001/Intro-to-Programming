# take file name as parameter, parse the file and return a dictionary
def parse_file_into_dict(fname):
    dict = {}
    with open(fname) as f:
        for c in f:
            # extract the URL and init_importance from the line
            url_var = c[0:5:]
            innit_imp = ""
            for d in enumerate(c[7::]):
                if d[1] == ':':
                    index = d[0]+9
                    break
                innit_imp += d[1]
            innit_imp = float(innit_imp)

            # extract the unique URLs referenced in the text
            text = c[index:]
            references = []
            for i in range(len(text)):
                if text[i:i+3] == "URL":
                    references.append(text[i:i+5])
            references = set(references)

            # add the URL, init_importance, unique references and overall importance to the dictionary
            dict[url_var] = [innit_imp, references, 0]
    return dict


def set_overall_imp(dict):  # calculate overall importance for each page
    for page_url in dict:
        for ref_url in dict[page_url][1]:
            ref_val = dict[page_url][0] / len(dict[page_url][1])
            dict[ref_url][2] += ref_val
    return dict


url_dict = set_overall_imp(parse_file_into_dict("IP Assignment-2/pages.txt"))
N = int(input("Enter upto what rank do you want to see the pages: "))
print()

if N > len(url_dict):
    print("Number of pages in the input file is less than the number of pages requested")
    N = len(url_dict)

sorted_dict = dict(
    sorted(url_dict.items(), key=lambda item: item[1][2], reverse=True))

ctr = 1
for key, val in sorted_dict.items():
    if ctr > N:
        break
    print(f"Page URL: {key}, Overall Importance: {val[2]}")
    ctr += 1
