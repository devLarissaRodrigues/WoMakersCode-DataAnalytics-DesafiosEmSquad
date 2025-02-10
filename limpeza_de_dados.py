#Fazer a instalação do pandas, numpy, matplotlib e seaborn no terminal com o seguinte comando: pip install pandas numpy matplotlib seaborn    
import pandas as pd

titanic = pd.read_csv('dataset/train.csv')

'''
Variáveis:
Survival: Sobrevivência (0 = Não, 1 = Sim)
Pclass: Classe do bilhete (1 = 1º, 2 = 2º, 3 = 3º)
Sex: Gênero
Age: Idade em anos
Sibsp: Nº de irmãos/filhos a bordo do Titanic
Ticket: Número do bilhete
Fare: Tarifa do passageiro
Cabin: Número da cabine
Embarked: Porto de embarcação (C = Cherbourg, Q = Queenstown, S = Southhampton)
'''

print(titanic.head(3))

'''
print(titanic.shape)
print(titanic.info())
print(titanic.describe())
print(titanic.nunique())
'''

#Verificação dos valores vazios:
print(titanic.isnull().sum())
filtroEmbarqued = titanic[titanic.Embarked.isnull()]
print(filtroEmbarqued)
filtroEmbarquedAtualizado = titanic.loc[titanic.Embarked.isnull(), 'Embarked'] = 'S'
print(filtroEmbarquedAtualizado)

titanic.groupby('Pclass')['Age'].median()
print(titanic)


