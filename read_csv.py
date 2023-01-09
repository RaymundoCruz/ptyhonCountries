import csv

def read_csvF1(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #return a reader object
        header = next(reader)
        data=[]
        for row in reader:
            iterable=zip(header,row) #genera tuplas
            country_dict={key:value for key,value in iterable}
            data.append(country_dict)
        return data


def filtro(item):
    dict_country={
    '1970':int(item['1970 Population']),
    '1980':int(item['1980 Population']),
    '1990':int(item['1990 Population']),
    '2000':int(item['2000 Population']),
    '2010':int(item['2010 Population']),
    '2015':int(item['2015 Population']),
    '2020':int(item['2020 Population']),
    '2022':int(item['2022 Population']),
    }
    labels=dict_country.keys()
    values=dict_country.values()
    return labels,values


def filtro_dc(data):
    dict_wpp={item['Country/Territory']:item['World Population Percentage'] for item in data if item['Continent']=='Oceania'}
    labels=dict_wpp.keys()
    values=dict_wpp.values()
    return labels,values


def filtro_lambda(data):
    labels=list(map(lambda x:x['Country/Territory'],data))
    values=list(map(lambda x:x['World Population Percentage'],data))
    return labels,values

def population_by_country(data,country):
    result=list(filter(lambda item:item['Country/Territory']==country,data))
    return result


#data=read_csvF1('population.csv')
#filtro_lambda(data)
#print(keys)
#print(values)