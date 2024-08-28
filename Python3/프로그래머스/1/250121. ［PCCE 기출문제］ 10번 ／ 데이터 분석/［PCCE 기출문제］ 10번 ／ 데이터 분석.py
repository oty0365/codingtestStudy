def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_idx = 0
    val_idx = 0
    if(ext=="code"):
        ext_idx = 0
    elif(ext=="date"):
        ext_idx = 1
    elif(ext=="maximum"):
        ext_idx = 2
    elif(ext == "remain"):
        ext_idx=3
    if(sort_by == "code"):
        val_idx = 0
    elif(sort_by == "date"):
        val_idx = 1
    elif(sort_by == "maximum"):
        val_idx = 2
    elif(sort_by == "remain"):
        val_idx = 3
    for i in range(0,len(data)):
        if(data[i][ext_idx]<val_ext):
            answer.append(data[i])
    answer.sort(key=lambda x:x[val_idx])
    print(answer)
    return answer