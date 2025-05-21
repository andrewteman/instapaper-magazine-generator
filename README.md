
# 📰 Instapaper to Magazine Generator

Turn your saved [Instapaper] (https://www.instapaper.com) articles into a beautifully formatted, printable PDF magazine — complete with inline images, cleaned typography, and 16pt reading-friendly type. Perfect for zine-style printing, weekend reading, or offline archiving.

---

## ✨ Features

- 📥 Extracts full article content and **inline images**
- 🔤 Cleans up common web encoding artifacts (like em dashes, smart quotes, etc.)
- 🖨 Outputs a **print-ready PDF** with large type and elegant formatting
- 📘 Designed for **saddle-stitch (stapled booklet)** printing layout

---

## 📦 Requirements

### Python dependencies

Install via pip:

```bash
pip3 install -r requirements.txt
```

### System dependencies

You must install [`wkhtmltopdf`](https://github.com/wkhtmltopdf/wkhtmltopdf/releases) manually:

1. Download the macOS `.pkg` or Windows installer
2. Install it
3. Ensure the `wkhtmltopdf` command is available in your terminal  
   (You can test it by running `which wkhtmltopdf`)

---

## 🚀 How to Use

### 1. Export your Instapaper library

- Log into Instapaper
- Visit [instapaper.com/export](https://www.instapaper.com/user)
- Email yourself a `.csv` export

### 2. Rename the export

Save the file as:

```
Instapaper-Export.csv
```

Place it in the same folder as the script.

### 3. Run the script

```bash
python3 instapaper_magazine.py
```

This will generate:

```
Instapaper_Magazine.pdf
```

---

## 🖨 Make it Print-Ready (Booklet Format)

Use [**Create Booklet**](https://createbooklet.com) (for macOS) or another imposition tool to reformat your PDF into printer spreads.

### Recommended Print Settings:

- 📄 Paper size: US Letter or A4
- 🔁 Duplex: Yes (flip on **short edge**)
- 📚 Binding: Left (saddle stitch)
- ➕ Add blank pages to bring total page count to a multiple of 4

---

## 🧪 Customization Ideas

- Add a cover or back page
- Change font or layout via embedded CSS in the script
- Modify the number of articles (`top_n`) to suit your page budget
- Adapt the script to export EPUB or Kindle-friendly files

---

## 🙏 Credit

Idea by [Andrew Teman](https://github.com/andrewteman)  
Script formatting and automation support by [OpenAI ChatGPT](https://openai.com/chatgpt)

---

## 📄 License

MIT License. Use freely, modify widely, and share generously.
