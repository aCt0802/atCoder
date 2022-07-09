def get_ans():
    N = int(input())
    strList = []
    for i in range(N):
        strList.append(str(input()))
    print(strList)

    # 横方向
    for record in strList:
        for i in range(N - 6):
            section = list(record[i:i + 6])
            print(section)
            if section.count('#') >= 4:
                return 'Yes'
            else:
                pass

    print("ここから縦")
    
    # 縦方向
    for i in range(N):
        for j in range(N - 6):
            section = list(strList[j][i] , strList[j + 1][i] , strList[j + 2][i] , strList[j + 3][i] , strList[j + 4][i] , strList[j + 5][i])
            print(section)
            if section.count('#') >= 4:
                return 'Yes'
            else:
                pass

    # 斜め
    # TODO 実装する!!

if __name__ == '__main__':
    print(get_ans())