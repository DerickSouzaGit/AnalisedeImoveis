import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Dados e Graficos do DF=-=-=-=-=-=-=-=--=--=--=-=-=-=-=-=-=-=-=-=-=-=-")

#carregando primeiro bd do distrito federal
df = pd.read_csv("dados/ImóveisDF.csv", sep=";")

#setando para não mostrar notação cientifica
pd.set_option('display.float_format', '{:,.2f}'.format) #no pandas

#Mostrando infos vbásicas
#print(df.info())
#print(df.head())    

#Convertendo para formato correto
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
df["area"] = pd.to_numeric(df["area"], errors="coerce")
df["quartos"] = pd.to_numeric(df["quartos"], errors="coerce")

#Preenchendo valores vazios
df["preco"] = df["preco"].fillna(df["preco"].median())  
df["area"] = df["area"].fillna(df["area"].median())
df["quartos"] = df["quartos"].fillna(df["quartos"].median())

#Filtrando valores vazios
df = df[df['preco'] > 0]
df = df[df['area'] > 0]

#Mostrando valores importantes
print("Dados importantes: ")
print("")
print(df.describe())

#df_numeric = df.select_dtypes(include=['number'])

#plt.figure(figsize=(10, 8))
##sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
#plt.title("Mapa de Correlação")
#plt.show()


#criando grafico do frequencia de preços
plt.figure(figsize=(15,3))
plt.hist(df["preco"].sort_values(), bins=150, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.title("Frequência e distribuição de preços No Distrito Federal")

#grafico da relação por tipo de lote / preço
plt.figure(figsize=(10,4))
df.groupby("tipo")["preco"].mean().sort_values().plot(kind="bar", color="orange")
plt.ylabel("Preço Médio")
plt.title("Relação tipo / preço no Distrito Federal")
plt.xticks(rotation=45)

#grafico da relação grafico / preço
plt.figure(figsize=(12,6))
df.groupby("bairro")["preco"].mean().sort_values().plot(kind="bar", color="orange")
plt.ylabel("Preço Médio")
plt.title("relação bairro / preço no Distrito Federal")
plt.xticks(rotation=45)

#mostrar graficos
plt.show()

print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Dados e Graficos de SP=-=-=-=-=-=-=-=--=--=--=-=-=-=-=-=-=-=-=-=-=-=-")

#carregando bd1 de sp
df2 = pd.read_csv("dados/ImóveisSP.csv")

#mostrnado infos basicas
#print(df2.info())
#print(df2.head())

#convertendo para formato correto
df2["ID"] = pd.to_numeric(df2["ID"], errors="coerce")
df2["Price"] = pd.to_numeric(df2["Price"], errors="coerce")
df2["Area"] = pd.to_numeric(df2["Area"], errors="coerce")
df2["Bedrooms"] = pd.to_numeric(df2["Bedrooms"], errors="coerce")
df2["Bathrooms"] = pd.to_numeric(df2["Bathrooms"], errors="coerce")
df2["Parking_Spaces"] = pd.to_numeric(df2["Parking_Spaces"], errors="coerce")
df2["created_date"] = pd.to_datetime(df2["created_date"], errors="coerce")
df2["extract_date"] = pd.to_datetime(df2["extract_date"], errors="coerce")

#Preenchendo valores vazios
df2["Price"] = df2["Price"].fillna(df2["Price"].median())  
df2["Area"] = df2["Area"].fillna(df2["Area"].median())  
df2["Bedrooms"] = df2["Bedrooms"].fillna(df2["Bedrooms"].median())  
df2["Bathrooms"] = df2["Bathrooms"].fillna(df2["Bathrooms"].median())  
df2["Parking_Spaces"] = df2["Parking_Spaces"].fillna(df2["Parking_Spaces"].median())  

#filtrando valores vazios
df2 = df2[df2['Price'] > 0]
df2 = df2[df2['Area'] > 0]

#informações importantes do bd de sp
print("Dados importantes: ")
print("")
print(df2.describe())

#grafico da relação por tipo de lote / preço
plt.figure(figsize=(15,3))
plt.hist(df2["Price"].sort_values(), bins=150, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.title("Frequência e distribuição de preços em São Paulo")

#grafico da relação por tipo de lote / preço
plt.figure(figsize=(10,4))
df2.groupby("Bedrooms")["Price"].mean().sort_values().plot(kind="bar", color="orange")
plt.ylabel("Preço Médio")
plt.title("Relação quarto / preço em SP")
plt.xticks(rotation=45)

#mostrando graficos
plt.show()
print("Para mostrar os gráficos, por favor, instale os requerimentos do requirements.txt e execute no cmd ou vscode")
input()

print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-FIM DA ANALISE=-=-=-=-=-=-=-=--=--=--=-=-=-=-=-=-=-=-=-=-=-=-")

