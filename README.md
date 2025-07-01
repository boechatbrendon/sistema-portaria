

```markdown
# 📦 Sistema de Portaria Residencial

**Sistema web completo para controle de encomendas em condomínios**, desenvolvido com foco em usabilidade, organização e eficiência. Ideal para porteiros registrarem o recebimento e a entrega de encomendas com rapidez e segurança.

---

## 🧩 Visão Geral

O **Sistema de Portaria** foi projetado para facilitar a rotina em portarias de condomínios residenciais. Com uma interface simples e moderna, permite o registro detalhado de moradores, unidades e encomendas, garantindo rastreabilidade e histórico de todas as movimentações.

---

## ✅ Funcionalidades

- 🔐 Autenticação com login seguro para porteiros
- 🏢 Cadastro e visualização de unidades e moradores
- 📬 Registro de encomendas com nota fiscal e porteiro responsável
- 📦 Marcação de retirada de encomendas com histórico completo
- 📅 Filtro de histórico por intervalo de datas
- 🖼️ Interface responsiva com suporte a tema escuro
- ⚡ Atualização dinâmica de moradores via AJAX ao selecionar a unidade

---

## 🛠️ Tecnologias Utilizadas

| Stack | Tecnologias |
|-------|-------------|
| Backend | Flask · Python · Flask-Login · SQLite |
| Frontend | HTML5 · Jinja2 · Tailwind CSS · JavaScript (AJAX) |
| Outros | Werkzeug · Flask-WTF · WTForms |

---

## 📁 Estrutura do Projeto


SistemaPortaria/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── routes/
│   ├── templates/
│   └── static/
│
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sistema-portaria.git
cd sistema-portaria
````

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor Flask:

```bash
python main.py
```

> Acesse: `http://127.0.0.1:5000` no navegador

---

## 🧪 Funcionalidades em Desenvolvimento

* 👨‍💼 Painel do síndico com permissões administrativas
* 📊 Relatórios automáticos de entregas
* 🏙️ Suporte a múltiplos condomínios
* 🧾 Upload de comprovantes de retirada

---

## 📸 Imagens do Sistema *(recomendado)*



---

## 👤 Autor

**Brendon Boechat**
Desenvolvedor Backend em formação
🔗 GitHub: [@boechatbrendon](https://github.com/boechatbrendon)
📧 Email: [boechatbrendon1@email.com](mailto:boechatbrendon@gmail.com)

---

## 📝 Licença

Este projeto está sob a Licença MIT.
Sinta-se à vontade para usar, modificar e distribuir.

---


