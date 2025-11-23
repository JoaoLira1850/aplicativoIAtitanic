# 🛳️ Projeto IA Titanic – Predição de Sobrevivência  
Sistema completo envolvendo **Machine Learning + API Backend + App Mobile em React Native**.

---

# 📘 Visão Geral

Este projeto demonstra o fluxo completo de criação e deploy de um modelo de Inteligência Artificial, desde a análise dos dados até o consumo da IA em um aplicativo mobile.

O sistema contém **3 camadas integradas**:

1. **Notebook de Inteligência Artificial (Machine Learning)**  
2. **Backend com FastAPI (Deploy do modelo .pkl)**  
3. **Aplicativo Mobile em React Native (Front-End)**  

Cada parte conversa entre si de maneira totalmente funcional.

---

# 🧠 1. Notebook – Machine Learning (Titanic)

Arquivo: `titanicNotebook.ipynb`

### ✔ Tecnologias utilizadas
- Jupyter / Colab  
- Python 3  
- Pandas e NumPy  
- Scikit-Learn  
- Matplotlib e Seaborn  

### ✔ O que foi feito
- Limpeza e preparação dos dados  
- Criação das features  
- Balanceamento  
- Treinamento de modelos: DecisionTree, RandomForest, Logistic Regression etc.  
- Avaliação: acurácia, precisão, recall, F1-score  
- Geração da **matriz de confusão**  
- Exportação do modelo final `.pkl` para uso no Backend

---

# 🌐 2. Backend – API em Python (FastAPI)

Pasta: `ProjetoTitanicAPI/`

### ✔ Tecnologias utilizadas
- Python  
- FastAPI  
- Uvicorn  
- Scikit-Learn  
- Pydantic  
- CORS Middleware (para permitir acesso do app mobile)

### ✔ Funções do Backend
- Carrega o modelo `.pkl`  
- Recebe os dados de um passageiro via **POST /predict**  
- Valida os dados com Pydantic  
- Retorna:
  - previsão da IA (0 ou 1)  
  - probabilidade  

## 📱 3. Front-End Mobile – React Native

O front-end deste projeto foi desenvolvido em **React Native**, funcionando como a interface onde o usuário insere os dados do passageiro e visualiza a previsão retornada pela API FastAPI.

### ✔ Tecnologias utilizadas no Front-End
- **React Native**
- **JavaScript (ES6)**
- **Expo / Metro Bundler**
- **Hooks do React**
  - `useState` para controle dos campos e estados internos
  - `useEffect` para ações baseadas no estado
- **StatusBar** do React Native
- **fetch / axios** para integração HTTP com o backend
- **StyleSheet** para estilização (equivalente a CSS)
- **Flexbox** para responsividade e organização da interface
- Componentes nativos utilizados:
  - `View`
  - `Text`
  - `TextInput`
  - `ScrollView`
  - `TouchableOpacity` / `Pressable`

---

### 🛠 Funcionalidades Implementadas
- Formulário completo com os dados necessários para a IA prever a sobrevivência:
  - Sexo  
  - Idade  
  - Classe  
  - Tarifa  
  - SibSp  
  - Parch  
  - Embarque  
- Controle total dos inputs utilizando **useState**
- Envio dos dados ao backend via POST
- Recebimento da previsão (sobreviveu / não sobreviveu)
- Exibição clara e estilizada da resposta ao usuário
- Tratamento visual:
  - Loading
  - Mensagens de erro (ex.: API offline)
  - Mensagem colorida dependendo do resultado
- Layout organizado com Flexbox e estilizado com StyleSheet

---

### 🔗 Integração com o Backend FastAPI

```javascript
const response = await fetch(`${API_URL}/predict`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    Sex,
    Age,
    SibSp,
    Parch,
    Fare,
    Pclass_2,
    Pclass_3,
    Embarked_Q,
    Embarked_S,
  }),
});


### ✔ Como rodar
```bash
pip install -r requirements.txt
uvicorn main:app --reload
npm install
npx expo start

