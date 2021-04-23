import pandas

def find_all(parameter, iterable): #retorna uma lista com os índices de todas as instâncias de parameter dentro de um iterável
    indexes = []
    i = 0
    for element in iterable:
        if callable(parameter) and parameter(element):
            indexes.append(i)
        elif element == parameter:
            indexes.append(i)
        i += 1
    return indexes

def build_from_dataframe(df, indexes, columns): #constrói um novo dataframe baseado nas linhas(informadas por indexes) e nas colunas do df anterior
    rows = []
    for index in indexes:
        row = []
        for column in columns:
            row.append(df[column][index])
        rows.append(row)
    filtered = pandas.DataFrame(rows, columns = columns)
    return filtered


def filter_by_date(df, date_column_name, date): #entrega o dataframe filtrado por data. Informe a data como string em formato dd/mm/aaaa
    date_column_content = df[date_column_name]
    columns = df.columns
    indexes = find_all(lambda x: x[:10] == date, date_column_content)
    filtered = build_from_dataframe(df, indexes, columns)
    return filtered
    



def filter_by_name(df, name_column_name, parameter): #entrega o dataframe filtrado por nome. Identifique o nome da coluna em name_column_name
    name_column_content = df[name_column_name]
    columns = df.columns
    indexes = []
    if type(parameter) == str:
        parameter = [parameter]
    for name in parameter:
        indexes += find_all(name, name_column_content)

    filtered = build_from_dataframe(df, indexes, columns)
    return filtered

def count(parameter, iterable): #conta as ocorrências de um dado elemento dentro de um iterável
    i = 0
    for element in iterable:
        if element == parameter:
            i += 1
    return i

def filter_by_condition(df, column_name, condition): #filtra de acordo com uma condição, a ser informada por meio de uma função. Informar
    column_name_content = df[column_name]           #o nome da coluna a ser verificada
    columns = df.columns
    indexes = find_all(condition, column_name_content)
    filtered = build_from_dataframe(df, indexes, columns)
    return filtered

def filter_by_row_and_column(df, rows = None, columns = None): #filtra por linhas e colunas. Use tuplas de dois elementos se se referir
    if rows == None:                                           #a todos os elementos do primeiro índice informado ao segundo. Use listas
        rows = range(0, len(df))                               #caso se refira a índices específicos
    
    if columns == None:
        columns = df.columns

    if type(columns) == str:
        columns = [columns]
    
    elif type(columns) == tuple:
        u = df.columns.index(columns[0])
        v = df.columns.index(columns[-1])
        columns = df.columns[u : v + 1]
    
    elif type(columns) == list:
        columns = columns
    
    if type(rows) == int:
        for column in columns :
            rows.append(df[column][rows])

    elif type(rows) == tuple:
        start = rows[0]
        stop = rows[-1]
        rows = range(start, stop + 1)
    
    filtered = build_from_dataframe(df, rows, columns)
    return filtered

def get_unique_values(iterable):  #retorna uma lista com os valores únicos de um iterável
    result = []
    for element in iterable:
        if result.count(element) == 0:
            result.append(element)
    return result

        
def to_hours(df, time_column_name):  #converte a coluna de horas(formato hh:mm) em unidades de hora(arredondado para 3 casa decimais)
    new_column = []
    for i in range(len(df)):
        hours = int(df.loc[i, time_column_name][-5: -3]) #hora em inteiro(horas e minutos são extraídos por string slicing)
        minutes = int(df.loc[i, time_column_name][-2:]) #análogo
        minutes_in_hours = round(minutes/60, 3) #convertendo os minutos em horas e arredondando para 3 casas decimais
        new_column.append(hours + minutes_in_hours)
    
    columns = df.columns
    rows = []
    for index in range(len(df)):
        row = []
        for column in columns:
            if column == time_column_name:
                row.append(new_column[index])
            else:
                row.append(df[column][index])
        rows.append(row)
    filtered = pandas.DataFrame(rows, columns = columns)
    return filtered


            

def layout(fig, x, y, sizex): #layout seta um dado jogo no gráfico junto com sua boxart de acordo com os parâmetros informados
    formatted = y.replace(" ", "%20")   #sizex representa o tamanho horizontal(largura) da imagem
    if y == "Source SDK Base 2013 Multiplayer":
        source = "https://res-3.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco/b17gr3xreillrivarc3d"
    else:
        source = "https://static-cdn.jtvnw.net/ttv-boxart/{}-100x100.jpg".format(formatted)
    fig.add_layout_image(
        dict(
            source = source,
            xref="x",
            yref="y",
            x = x,
            y = y,
            yanchor = "middle",
            xanchor = "left",
            sizex = sizex,
            sizey = 0.85
        )
)