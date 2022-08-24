import numpy as np
def convert_strings_to_num_array(strings: str):      
            strings = strings.lower()
            strings = strings.encode('utf_8')
            # strings=strings.decode("utf_8")
            lst = strings.split()
            index = len(lst)
            words_lst = []
            for str1 in lst:
                arr = np.frombuffer(str1, dtype=np.uint8)
                # print("array" ,arr)
                data_arr = np.array(arr)
                # print(data_arr)
                word_lst = [np.sum(data_arr), data_arr.size, str1]
                words_lst.append(word_lst)

            return words_lst
            # print(index)
ww=convert_strings_to_num_array("sahill goyal is best")
print(ww)
for i in range(0,len(ww)):
# #     print(ww[i][2])
    ww[i][0]=int(ww[i][0])
#     ww[i][2]=ww[i][2].decode("utf_8")
#     # print(i)
print(ww)
print(type(ww[0][0]))