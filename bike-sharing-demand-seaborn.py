import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

BaseDados = pd.read_csv('D:\\Python\\Kaggle\\Bike Sharing Demand\\train.csv')
#print(BaseDados.describe()) #Traz informações como desvio padrão, média, valor mínimo e máximo de colunas, etc.
#print(BaseDados.sample(5).T) #Traz uma amostra da base de dados.
#print(BaseDados)

#print (BaseDados.atemp.describe()) #Faz um describe na coluna atemp 
#print (BaseDados.atemp.value_counts()) #Aplica um value_counts (agrupa informações e faz a soma por linhas do dataset.)
#print (BaseDados.atemp.mode()) #Aplica Moda na coluna atemp
#print(BaseDados[['temp','atemp']].describe()) #Faz um descibre nas colunas temp e atemp
#print (BaseDados.loc[20:30,'workingday':'humidity']) #imprime as linhas 20-30 e as colunas específicas com .loc
#print(BaseDados.iloc[20:31,3:8]) #Faz o mesmo que a linha acima mas usando o método iloc.
#print(BaseDados.at[20,'humidity']) #Traz o valor da célula da linha 20 e da coluna humidity
#print(BaseDados.iat[20,7]) #Faz o msm q a anterior mas com o método iat, que funciona por index
BaseDados['datetime'] = pd.to_datetime(BaseDados['datetime']) #Transforma a coluna datetime no tipo datetime64[ns]
BaseDados['year'] = BaseDados['datetime'].dt.year #cria uma nova coluna chama year por meio do método dt.
BaseDados['day'] = BaseDados['datetime'].dt.day #cria uma nova coluna chama day por meio do método dt.
BaseDados['dayofweek'] = BaseDados['datetime'].dt.dayofweek #cria uma nova coluna chama dayofweek por meio do método dt.
BaseDados['hour'] = BaseDados['datetime'].dt.hour #cria uma nova coluna chama hour por meio do método dt.
BaseDados['month'] = BaseDados['datetime'].dt.month #cria uma nova coluna chama month por meio do método dt.
#print(BaseDados.temp.median()) #Calcula a mediana da coluna temp.
#print(BaseDados[BaseDados['temp'] > BaseDados['temp'].median()]) #mostra o dados que possuem temp maior que a mediana de temp.
#print(BaseDados.season.value_counts()) #mostra quantas entradas existem para cada seaso. Ex: 2734 season 4.
#BaseDados['temp'].hist() #histograma da coluna temp
#sns.distplot(BaseDados['temp'], bins=10) #histograma utilizando Seaborn
#sns.boxplot(y = 'temp', x = 'season', data  = BaseDados) #boxplot utilizando Seaborn
#sns.violinplot(y = 'temp', data = BaseDados) #boxplot do tipo violino. Mostra um boxplot e a distribuição de valores.
#sns.violinplot(y = 'temp', x = 'season', data = BaseDados) #boxplot violino com y recebendo temp e x recebendo season
#sns.violinplot(y = 'temp', x = 'season', data = BaseDados, hue = 'weather') #violinplot utilizando o parâmetro hue = ângulo tomado no espaço L*C*hº(hue)
#sns.boxplot(y = 'humidity', x = 'weather', data = BaseDados) #boxplot com a variáveis humidity e weather
#sns.violinplot(y = 'humidity', x = 'weather', data = BaseDados)
#plt.show()
#print(BaseDados.groupby('workingday')['count'].mean()) #groupby similar ao SQL
#BaseDados.groupby('workingday')['count'].mean().plot.bar() #Agrupa as visitas por workingday, calcula a média da coluna count e gera um gráfico de barras
#print(BaseDados.groupby('month')['count'].median()) #Agrupa as vistitas por mês e calcula a mediana da coluna count
#sns.barplot(y = 'count', x = 'workingday', data = BaseDados) #o barplot do seaborn é similar ao groupby
#sns.barplot(y = 'count', x = 'season', data = BaseDados)
#sns.barplot(y = 'count', x = 'season', hue = "workingday", data = BaseDados) #o mesmo gráfico com três variáveis.
#sns.barplot(y = 'casual', x = 'weather', data = BaseDados)
#print(BaseDados.groupby('month')['count'].describe()) #agrupa por mês e gera uma análise descritiva (decribe)
#BaseDados.groupby('month')['count'].describe()['mean'].sort_index(ascending=False).plot() #gráfico de linha com as médias por mês
#BaseDados.groupby('month')['count'].describe()['max'].sort_index(ascending=False).plot() #gráfico de linha com os valores máximos por mês
#BaseDados.groupby('month')['count'].describe()['min'].sort_index(ascending=False).plot() #gráfico de linha com os valores mínimos por mês
#sns.pairplot(x_vars='temp', y_vars='count', data = BaseDados, size = 7) #gráfico de variáveis contínuas
#sns.pairplot(x_vars='temp', y_vars='count', data = BaseDados, hue = 'season', size = 7) #gráfico com um código de cores de acordo com a coluna season
#sns.pairplot(x_vars='humidity', y_vars='count', data = BaseDados, hue = 'season', size = 7, kind ='reg') #gráfico que traça regressões lineares com o parâmetro kind=reg
#sns.pairplot(x_vars='temp', y_vars='casual', data = BaseDados, size = 7, hue = 'holiday', kind = 'reg') #gráfico de vriáveis contínuas entre temp e casual, utilizando hue como 'holiday' e kind como 'reg'
#print(BaseDados[['humidity','count']].corr()) #calcula a correlação entra humidity e count
#print(BaseDados.groupby('season')[['humidity','count']].corr()) #calcula a correlação entra humidity e count após fazer um groupby por season
#print(BaseDados[['temp', 'casual']].corr())
#print(BaseDados.groupby('holiday')[['temp','casual']].corr())
#print(BaseDados.sort_index()) #ordena o índice
#print(BaseDados.sort_values(by='count', ascending = False)) #ordena pela coluna count de forma decrescente
#print(BaseDados.sort_values(['count', 'registered'])) #ordena pelas colunas count e registered de forma crescente
#print(BaseDados.sort_values(['humidity', 'weather'])) #ordena pelas colunas humidity e weather de forma crescente
#print(BaseDados['count'].shift(1)) #O .shift() serve para deslocar uma coluna para cima ou para baixo em relação a uma referência horizontal
'''for i in range (1,6):
    BaseDados['last_count_'+str(i)] = BaseDados['count'].shift(i) #Cria colunas last_count_ de 1 a 5 a partir da coluna count
print(BaseDados)'''
'''for i in range (1,6):
    BaseDados['last_registered_'+str(i)] = BaseDados['registered'].shift(i) #Cria colunas last_count_ de 1 a 5 a partir da coluna count
print(BaseDados)'''
#BaseDados.groupby('month')['count'].mean().plot.barh() #gráfico de barras horizontal, agrupado por meses, aplicando média em count.
#BaseDados['month'] = BaseDados['month'].astype('category') #transforma month no tipo category
#BaseDados['month'].cat.categories #categories é o mapa de códigos.
#BaseDados['month'].cat.categories = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] #Da os nomes aos códigos correspondentes no mapa de códigos.
#BaseDados.groupby('month')['count'].mean().plot.barh() #Gráfico agrupado por mês com a média das visitas
#BaseDados['month'].cat.as_ordered(True) #Diz que a categoria é ordenada na ordem em que se encontra.
#BaseDados['season'] = BaseDados['season'].astype('category')
#BaseDados['season'].cat.categories = ['Primavera', 'Verão', 'Outono', 'Inverno']
#BaseDados.groupby('season')['count'].mean().plot.barh() #Gráfico agrupado por season com a média das visitas
#BaseDados.groupby('season')['temp'].mean().plot.barh() #Gráfio agrupado por season com a temperatura média de cada estação
plt.show()

