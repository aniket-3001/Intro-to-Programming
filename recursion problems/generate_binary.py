def gen_bin_str(n, bin_str, bin_lst):
    if n == 0:
        bin_lst.append(bin_str)
        return
    gen_bin_str(n-1, bin_str + "0", bin_lst)
    gen_bin_str(n-1, bin_str + "1", bin_lst)


n = int(input())
bin_lst = []
gen_bin_str(n, "", bin_lst)
bin_lst.sort()
print(bin_lst)
