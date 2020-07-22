# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:30:56 2020

@author: ckruse003
"""

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Pesquisa de Educação Financeira')

st.write("Olá, somos a FinanceYou, uma start-up de Educação Financeira que busca ajudar as pessoas a cuidar do seu dinheiro e tomar decisões responsáveis, permitindo o desenvolvimento pessoal e da sociedade. Para entendermos os seus problemas e personalizar as nossas orientações, pedimos que preencha esse questionário para nos conhecermos melhor.")

"""
Selecione as opções abaixo que mais condizem com sua condição ou realidade

"""

QF1 = st.selectbox(
    'Quem é responsável pelas decisões diárias sobre dinheiro na sua residência?',
    ["a) Você.",
     "b) Você e seu cônjuge/parceiro(a).",
     "c) Você e outro(s) membro(s) da sua família.",
     "d) Seu cônjuge/parceiro(a).",
     "e) Outro(s) membro(s) da sua família.",
     "f) Outra pessoa.",
     "g) Ninguém.",
     "h) Não sei/Prefiro não responder."])

QF2 = st.selectbox(
    'A próxima pergunta é sobre orçamento familiar. Essa é uma ferramenta para para decidir que parte da renda familiar é usada para compras, poupança e pagamento das contas. Há um orçamento familiar na sua residência?',
    ["a) Sim.",
     "b) Não.",
     "c) Não sei/Prefiro não responder."])

QF11 = st.selectbox(
    'As vezes, as pessoas tem dificuldades de cobrir seus custos de vida com sua renda. Nos últimos meses, você recebeu gastou mais para manter seu custo de vida que obteve de rendimentos?',
    ["a) Sim.",
     "b) Não.",
     "c) Não sei/Prefiro não responder.",
     "d) Não aplicável(Não possuo renda própria)."])

"""
Faremos agora algumas perguntas à respeito de atitudes e comportamentos em relação ao uso do dinheiro e outras questões financeiras.
"""
"""
Para responder às questões abaixo, utilize a seguinte escala de 1 a 5, sendo: 1 - Concordo completamente, 2 - Concordo, 3 - Neutro, 4 - Discordo  e 5 - Discordo completamente
"""

def QS1():
    QS1A = st.slider('Eu tenho mais satisfação quando gasto dinheiro do que quando poupo para o longo prazo.',1,5,3)
    QS1B = st.slider('Eu estou preparado para arriscar um pouco do meu dinheiro quando poupo ou faço algum tipo de investimento.',1,5,3)
    QS1C = st.slider('Dinheiro é para ser gasto',1,5,3)
    QS1D = st.slider('Eu estou satisfeito com minha condição financeira atual.',1,5,3)
    QS1E = st.slider('Mantenho as minhas finanças sobre controle.',1,5,3)
    QS1F = st.slider('Uso meu celular para fazer ou receber pagamentos.',1,5,3)
    QS1G = st.slider('Minha condição financeira limita a minha habilidade de fazer coisas que são importantes pra mim.',1,5,3)
    QS1H = st.slider('Traço objetivos financeiros de longo prazo e me esforço para atingi-los.',1,5,3)
    QS1I = st.slider('Acredito que guardar dinheiro no banco é seguro mesmo que o banco venha a falir.',1,5,3)
    QS1J = st.slider('Estou muito endividado agora.',1,5,3)
    QS1K = st.slider('Se eu pego dinheiro emprestado, tenho a responsabilidade de pagá-lo de volta.',1,5,3)
    QS1L = st.slider('Acredito que os bancos devem avaliar a ética de uma companhia antes de lhe prover com serviços financeiros.',1,5,3)
    
    respostas_QS1 = {'QS1A':QS1A,
                     'QS1B':QS1B,
                     'QS1C':QS1C,
                     'QS1D':QS1D,
                     'QS1E':QS1E,
                     'QS1F':QS1F,
                     'QS1G':QS1G,
                     'QS1H':QS1H,
                     'QS1I':QS1I,
                     'QS1J':QS1J,
                     'QS1K':QS1K,
                     'QS1L':QS1L,}
    return respostas_QS1

respostas_QS1 = QS1()

valores = respostas_QS1.values()

total = sum(valores)

total_str =str(total)

st.title("Seu score de Educação Financeira é: "+ total_str)

        
        
        
        
        