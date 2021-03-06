def getTeamData(data):
    data_list = []
    #data = tr list 
    print(type(data))
    for tr in data:
        data_values = []
        for dIndex, dValue in enumerate(tr):
            if dValue != '\n':
                data_values.append(dValue.getText())
        
        data_list.append(data_values)
    return data_list

def cleanTeamData(dataset,search_string):
    teams = [i.lower() for i in search_string.split(', ')]
    indecesToDelete = [0, 7, 8, 9, 16, 17, 20, 22, 26, 27, 28]
    indexToAdd = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 18, 19, 21, 23, 24, 25]
    data = getTeamData(dataset)

    data_list = []
    cleaned_data_list = []
    row_data_list = []

    for row in data:
        if row[2].lower() in teams:
            row_data_list.append(row)

    for i in row_data_list:
        cleaned_data_values = []
        for columnIndex, value in enumerate(i):
            if columnIndex not in indecesToDelete:
                if columnIndex == 2:
                    cleaned_data_values.append(value.upper())
                else:
                    cleaned_data_values.append(value)
        cleaned_data_list.append(cleaned_data_values)
    return cleaned_data_list


def getPlayerData(data):
    data_list = []
    for tr in data:
        data_values = []
        for dIndex, dValue in enumerate(tr):
            if dValue != '\n':
                data_values.append(dValue.getText())
        
        data_list.append(data_values)
    return data_list

def cleanPlayerData(dataset,search_string):
    players = [i.lower() for i in search_string.split(', ')]
    indecesToDelete = [0, 7, 8, 9, 16, 17, 20, 22, 26, 27, 28]
    indexToAdd = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 18, 19, 21, 23, 24, 25]
    data = getPlayerData(dataset)
    data_list = []
    cleaned_data_list = []

    row_data_list = []
    for row in data:
        if row[1].lower() in players:
            row_data_list.append(row)

    for i in row_data_list:
        cleaned_data_values = []
        for columnIndex, value in enumerate(i):
            if columnIndex not in indecesToDelete:
                if columnIndex == 2:
                    cleaned_data_values.append(value.upper())
                else:
                    cleaned_data_values.append(value)
        cleaned_data_list.append(cleaned_data_values)
    return cleaned_data_list
