import read_csv
import charts


def run():

    data=read_csv.read_csvF1('population.csv')
    country=input("type a country : ")

    result=read_csv.population_by_country(data,country)

    if len(result)>0:
        year,population=read_csv.filtro(result[0])
        charts.generate_bar_chart(country,year,population)
#----------------------------------------------
#    label,value=read_csv.filtro_lambda(data)
#    charts.generate_pie_chart(label,value)
  
if __name__ == '__main__':
    run()
    