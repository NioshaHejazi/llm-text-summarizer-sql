# LLM-Powered Text Summarization with SQL


A command-line tool for summarizing text using a local BART model (facebook/bart-large-cnn). Summaries are stored in a PostgreSQL database, with support for keyword search and CSV export.

---

## 🚀 Features

- ✅ Summarize input text via CLI or text file
- ✅ Uses a **local BART-large model** (no internet required after setup)
- ✅ Store summaries in a PostgreSQL database
- ✅ Add tags and timestamps to each summary
- ✅ Search summaries using keywords
- ✅ Export summaries to CSV
- ✅ Simple CLI interface using `typer`

---

## 🗂️ Project Structure

```
llm-text-summarizer-sql/
├── app/                     # Core modules: DB config, summarizer
│   ├── config.py
│   ├── database.py
│   └── summarizer.py
├── local_model/             # Downloaded HuggingFace model for offline use
│   └── bart-large-cnn/
├── main.py                  # CLI entry point
├── requirements.txt         # Python dependencies
├── test_db.py               # DB test script
├── test_summarizer.py       # Summarizer test script
├── my_text.txt              # Sample input file
├── climate_summaries.csv    # Sample export
├── .env                     # Environment variables (e.g. DB credentials)
├── .gitignore               # Ignored files/folders
└── README.md
```

---

## 🧰 Setup Instructions

### 1. Clone the repo and create a virtual environment

```bash
git clone https://github.com/yourusername/llm-text-summarizer-sql.git
cd llm-text-summarizer-sql
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up PostgreSQL database

Create a PostgreSQL database (e.g., `summarizer`) and set credentials in `.env`:

```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=summarizer
DB_USER=summarizer_user
DB_PASSWORD=your_password
```

Then initialize the database:

```bash
python main.py init
```

### 4. Download and place the model

Manually download [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn/tree/main) and put it under:

```
local_model/bart-large-cnn/
```

Make sure it includes:
- `config.json`
- `pytorch_model.bin`
- `tokenizer.json`
- `vocab.json`
- `merges.txt`
- `generation_config.json` (optional)

---

## 💻 Usage

### Summarize direct text

```bash
python main.py summarize-text --text "Your paragraph here." --tags "news,policy"
```

### Summarize from file

```bash
python main.py summarize-text --file my_text.txt --tags "science,climate"
```

### List recent summaries

```bash
python main.py list --limit 3
```

### Search summaries

```bash
python main.py search "NASA"
```

### Export summaries to CSV

```bash
python main.py export --output-path summaries.csv
```

---

## 📦 Dependencies

- `transformers`
- `torch`
- `typer`
- `psycopg2-binary`
- `python-dotenv`
- `sqlalchemy`

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Testing
Basic scripts:

- `test_db.py`: checks DB connection
- `test_summarizer.py`: runs a summary and prints result

---

Basic scripts:

- `test_db.py`: checks DB connection
- `test_summarizer.py`: runs a summary and prints result

---
