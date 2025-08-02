# 🧠 Medical Chatbot with Custom Book Data  
**Tech Stack:** Python · Flask · Gemini 1.5 · LangChain · Pinecone

## 📌 Project Overview
This project is a **custom-trained medical chatbot** designed to provide accurate and context-aware responses using **The GALE Encyclopedia of Medicine**. It integrates **Google’s Gemini 1.5 model** via **LangChain** and performs **Retrieval-Augmented Generation (RAG)** using **Pinecone** vector database.

## 🚀 Features
- 🔍 **Custom Medical Knowledge**: Embedded data from *The GALE Encyclopedia of Medicine* for domain-specific accuracy.
- 🤖 **Conversational AI**: Uses Gemini 1.5 for generating human-like, reliable medical responses.
- 📚 **RAG Pipeline**: Implements Retrieval-Augmented Generation to fetch relevant context before answering queries.
- 🧩 **LangChain Integration**: Manages the RAG chain and model orchestration.
- 💾 **Pinecone Vector DB**: Efficient and scalable semantic search using dense vector embeddings.
- 🌐 **Web Interface**: Flask-based frontend for user-friendly interaction.

## 🧰 Tech Stack
- **Backend**: Python, Flask  
- **LLM**: Gemini 1.5 via LangChain  
- **Vector Store**: Pinecone  
- **Document Embedding**: LangChain Embedding pipelines  
- **Frontend**: HTML, CSS (basic) via Flask templates  

## 📂 Project Structure
```
📁 Medical_Chatbot
├── 📁 src
│   ├── helper.py              # PDF loader and embedding functions
│   ├── chatbot.py             # LangChain RAG chain setup with Gemini
│   └── config.py              # API keys and constants
├── 📁 templates
│   └── index.html             # Frontend UI
├── 📁 static
│   └── style.css              # Optional styling
├── app.py                     # Flask app runner
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
   ```

2. **Create virtual environment & activate**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set API Keys**  
   Create a `.env` file or update `config.py` with:
   - `GOOGLE_API_KEY` (for Gemini)
   - `PINECONE_API_KEY` and `PINECONE_ENVIRONMENT`
   - Optional: `PINECONE_INDEX_NAME`

5. **Prepare Embeddings**  
   Place the encyclopedia PDF in a `data/` folder and run:
   ```bash
   python src/helper.py
   ```

6. **Run the Application**  
   ```bash
   python app.py
   ```
   Access the chatbot at `http://127.0.0.1:5000/`

## 💬 Sample Conversations

> **User:** What are the symptoms of diabetes?  
> **Bot:** Symptoms of diabetes include increased thirst and frequent urination, excessive hunger, and unexplained weight loss. Other symptoms can be blurred vision, slow-healing sores, and frequent infections. If you experience these symptoms, consult a doctor for proper diagnosis and management.

> **User:** How can I improve my sleep quality?  
> **Bot:** To improve sleep quality, establish a regular sleep schedule, create a relaxing bedtime routine (e.g., warm bath, reading), and optimize your sleep environment for darkness, quiet, and coolness. Consider avoiding caffeine and alcohol before bed. If problems persist, consult a healthcare professional.

> **User:** I have a sore throat and fever. What could it be?  
> **Bot:** A sore throat accompanied by a fever could indicate a viral infection like the common cold or influenza, or a bacterial infection like strep throat. Further evaluation by a doctor is needed for proper diagnosis and treatment. They can perform a physical exam and potentially a rapid strep test to determine the cause.

> **User:** Can I take paracetamol and ibuprofen together?  
> **Bot:** While you can take paracetamol and ibuprofen together, it's generally not recommended without consulting a doctor or pharmacist. Combining them may increase the risk of side effects, particularly stomach upset. Always follow dosage instructions carefully.

> **User:** How to treat a minor burn at home?  
> **Bot:** For minor burns, immediately cool the burn under cool (not cold) running water for 10–20 minutes. Then, gently cover the burn with a sterile bandage. Over-the-counter pain relievers like ibuprofen or acetaminophen can help manage pain and inflammation.

## 📝 Notes
- This project is for **educational/demo purposes** and **not a substitute for professional medical advice**.

