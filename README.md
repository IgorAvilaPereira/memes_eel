# 📸 memes_eel


Uma aplicação desktop divertida feita em **Python + HTML/CSS/JS** via [Eel](https://github.com/python-eel/Eel), que apresenta alguns dos memes mais icônicos da internet brasileira.

---

## ✨ Funcionalidades

- 🎨 Interface moderna com HTML, CSS e JavaScript  
- 🖼️ Navegação por memes brasileiros clássicos  
- 🖥️ Empacotável como aplicativo de desktop multiplataforma  
- 💡 Exemplo educativo de uso do framework Eel  

---

## 📸 Demonstração

![Demo do app](demo.gif)

---

## 📦 Requisitos

Certifique-se de ter o Python instalado (3.10+). Depois, instale as dependências:

```bash
pip install eel
pip install pyinstaller
````

---

## ⚙️ Ambiente de Desenvolvimento

Aplicação criada no seguinte ambiente:

![Setup](setup.png)

---

## 🛠️ Gerar Executável

Use o **PyInstaller** com Eel para empacotar o projeto:

```bash
python -m eel main.py web --onefile --noconsole
```

O executável será gerado na pasta `dist/`.

---

## ▶️ Executar o App

```bash
cd dist
./main      # Linux/macOS
main.exe    # Windows
```

---

## 📁 Estrutura do Projeto

```
memes_eel/
├── main.py
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── demo.gif
├── setup.png
├── README.md
└── LICENSE
```
---

## 🪪 Licença

Distribuído sob a licença MIT.  
