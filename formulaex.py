a = ""
a = input()
array = []
str_arr = ""
b = ""
#while b!=";":
#    b =  input().split()
#    array.append(b)

str_arr= a.split(' ')
#print(str_arr)
formul = []
i=0

for i in range(str_arr.__len__()):
    if (str_arr[i] == '+' or str_arr[i] == '/' or str_arr[i] == '-' or str_arr[i] == '*' or str_arr[i] == '^'):
        if str_arr[i-2]== '=':
            formul.append(str_arr[i-3])
        if str_arr[i-2]== '(' and str_arr[i-3]=='=':
            formul.append(str_arr[i-4])
 #   for j in range(str_arr[i].__len__()):
  #      if str_arr[i][j] == "=":
j=0
m=0

for j in range(formul.__len__()):
    p = j + 1
    while(p<formul.__len__()):
        if(formul[j] == formul[p]): formul[p]=""
        p = p+1
    j = j+1


for m in range(formul.__len__()):
    print(formul[m])
find_formul = ""
path_formul = ""
rev_path_formul=""
timer = formul.__len__()
flag = 1
#while(find_formul != "end" or timer == 0 or flag ==1):
find_formul = input()
#if(find_formul=="end"): flag=0
j = 0
for j in range(str_arr.__len__()):
    if(str_arr[j]== find_formul):
        k = j
        if(str_arr[j+1] != '='):
            rev_path_formul=""
            while(str_arr[k]!= ';'): k = k-1
            while(k<j-1):
                rev_path_formul = rev_path_formul + " " + str_arr[k+1]
                k= k+1
            path_formul = path_formul + rev_path_formul
        k = j
        while(str_arr[k] != ';'):
            path_formul = path_formul + " " + str_arr[k]
            k = k+1
        path_formul = path_formul + "|"
print(path_formul)
#    timer = timer - 1

