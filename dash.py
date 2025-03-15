import streamlit as st 

#cabeçalho

st.header('Enquete da Programação') #Cabeçalho
st.checkbox('Aluno') # Caixa de Seleção
st.checkbox('Professor')
# st.button('Clique Aqui') # Botão de Clique
st.radio('SABE PROGRAMAR?', ['Sim', 'Não',]) #Multipla Seleção
st.selectbox('GOSTARIA DE APRENDER MAIS SOBRE LINGUAGENS DE PROGRAMAÇÃO?',
             ['Sim', 'Não', 'Talvez']) # Escolher Opção
st.multiselect('QUAIS AS LINGUAGENS DE PROGRAMAÇÃO VOCÊ CONHECE?',
               ['Python', 'HTML', 'JavaScript', 'C#', 'C++', 'Outras']) # multipla seleção
st.select_slider('QUAL SEU NÍVEL EM PROGRAMAÇÃO?', ['Iniciante', 'Intermediário', 'Profissional', 'Lendário'])
st.slider('SELECIONE UMA NOTA A VOCÊ NA ÁREA DA PROGRAMAÇÃO', 0, 10)
st.image("prog.png") #inserir foto

if st.button('FINALIZAR'):
    st.success("Parabéns, Você Completou nossa Enquete!")
else:
    st.info('Você precisa clicar no Botão Finalizar')

st.title("MUITO OBRIGADO POR PARTICIPAR DA NOSSA ENQUETE!")
st.header("Muito Obrigado Por Participar da Nossa Enquete!")