import matplotlib.pyplot as plt

def generate_bar_chart(country,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'imgs/{country}.png')
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax =plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()