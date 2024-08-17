import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo local (usando raw string)
file_path = r'C:\Users\01002452\OneDrive - Faculdade São Leopoldo Mandic\Área de Trabalho\PYTHON\healthcare_dataset.csv'

# Carregar os dados
df = pd.read_csv(file_path)

# Verifique os nomes das colunas para garantir que a coluna 'Hospital' existe
print(df.columns)

# Título do dashboard
st.title('Healthcare Dataset Dashboard')

# Seção de filtros
st.sidebar.header('Filtros')

# Suponha que a coluna correta seja 'Hospital Name' em vez de 'Hospital'
hospitais = st.sidebar.multiselect(
    'Selecione o Hospital',
    options=df['Hospital'].unique(),  # Use o nome correto aqui
    default=df['Hospital'].unique()   # Use o nome correto aqui
)

# Filtro por condição médica
condicoes_medicas = st.sidebar.multiselect(
    'Selecione a Condição Médica',
    options=df['Medical Condition'].unique(),
    default=df['Medical Condition'].unique()
)

# Aplicar filtros
df_filtrado = df[(df['Hospital'].isin(hospitais)) & (df['Medical Condition'].isin(condicoes_medicas))]

# Gráfico de Distribuição por Idade
st.subheader('Distribuição Etária dos Pacientes')
fig, ax = plt.subplots()
df_filtrado['Age'].hist(bins=20, ax=ax)
ax.set_xlabel('Idade')
ax.set_ylabel('Número de Pacientes')
st.pyplot(fig)

# Gráfico de Barras de Custo Médio por Condição Médica
st.subheader('Custo Médio por Condição Médica')
custo_medio = df_filtrado.groupby('Medical Condition')['Billing Amount'].mean().sort_values()
st.bar_chart(custo_medio)

# Gráfico de Barras de Tempo Médio de Permanência por Hospital
st.subheader('Tempo Médio de Permanência por Hospital')
df_filtrado['Discharge Date'] = pd.to_datetime(df_filtrado['Discharge Date'])
df_filtrado['Date of Admission'] = pd.to_datetime(df_filtrado['Date of Admission'])
df_filtrado['Stay Duration'] = (df_filtrado['Discharge Date'] - df_filtrado['Date of Admission']).dt.days
tempo_medio_hospital = df_filtrado.groupby('Hospital')['Stay Duration'].mean().sort_values()
st.bar_chart(tempo_medio_hospital)

# Mostrar a tabela de dados filtrados
st.subheader('Dados Filtrados')
st.write(df_filtrado)
