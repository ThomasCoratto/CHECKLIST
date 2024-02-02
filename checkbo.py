import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv('C:/Users/moesios/Desktop/teste saida/dados.csv')

# Funções para verificar os itens
def verifica_creches():
    return df['creches'].any()

def verifica_qtd_moradores():
    return df['qtd_moradores'].any()

def verifica_instrucao():
    return df['instrucao'].any()

def verifica_deslocamento():
    return df['deslocamento'].any()

def verifica_deslocamento_motivo():
    return df['deslocamento_motivo'].any()

def verifica_deslocamento_deslocs():
    return df['deslocamento_deslocs'].any()

def verifica_responsavel_pessoa_com_mob_reduzida():
    return df['responsavel_pessoa_com_mob_reduzida'].any()

def verifica_aposentado():
    return df['aposentado'].any()

def verifica_solicitou_entrega_no_dia_anterior():
    return df['solicitou_entrega_no_dia_anterior'].any()

def verifica_solicitou_servico_no_dia_anterior():
    return df['solicitou_servico_no_dia_anterior'].any()

def verifica_enderecos_ensino():
    return df['endereco_ensino_1'].any() and df['endereco_ensino_2'].any()

def verifica_enderecos_trabalho():
    return df['endereco_trabalho_1'].any() and df['endereco_trabalho_2'].any()

# Criar o site
st.title('Verificação de Itens')

# Criar as caixas de seleção
st.checkbox('Criches', value=verifica_creches())
st.checkbox('Qtd de Moradores', value=verifica_qtd_moradores())
st.checkbox('Bater grau de instrução com nível matriculado', value=verifica_instrucao())
st.checkbox('Deslocamento', value=verifica_deslocamento())
st.checkbox('Motivo pelo qual não se deslocou', value=verifica_deslocamento_motivo())
st.checkbox('Deslocamentos', value=verifica_deslocamento_deslocs())
st.checkbox('Mora com a pessoa com mob. reduzida', value=verifica_responsavel_pessoa_com_mob_reduzida())
st.checkbox('Aposentado', value=verifica_aposentado())
st.checkbox('Solicitou entrega no dia anterior?', value=verifica_solicitou_entrega_no_dia_anterior())
st.checkbox('Solicitou serviço no dia anterior?', value=verifica_solicitou_servico_no_dia_anterior())
st.checkbox('Endereços de ensino 1 e 2', value=verifica_enderecos_ensino())
st.checkbox('Endereços de trabalho 1 e 2', value=verifica_enderecos_trabalho())