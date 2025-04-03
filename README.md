# SnapandLearn - AI Image Analysis Tool

<a id="readme-top"></a>

![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Vision_API-green)

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Security](#security)
- [Development](#development)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- Image upload (JPG/PNG/JPEG) or camera capture
- GPT-4 Vision analysis
- Real-time results
- Secure API key management
- Customizable prompts

## 🚀 Quick Start
```bash
# Clone repo
git clone https://github.com/yourusername/SnapandLearn.git
cd SnapandLearn

# Create venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install deps
pip install streamlit python-dotenv requests Pillow

# Configure
echo "OPENAI_API_KEY=your_key" > .env

# Run
streamlit run snapnlearn.py
```
Access: `http://localhost:8501`

## 🛠️ Configuration
### .env File
```ini
OPENAI_API_KEY=your_key_here
```

### Custom Prompts
Edit in `analyze_photo()`:
```python
{"type": "text", "text": "Your custom prompt"}
```

## 🔒 Security
1. Never commit .env
```bash
echo ".env" >> .gitignore
```
2. Use environment variables
3. Rotate keys regularly

## 💻 Development
### Structure
```
SnapandLearn/
├── snapnlearn.py
├── requirements.txt
├── .env.example
└── README.md
```

### Dependencies
```python
streamlit==1.22.0
python-dotenv==1.0.0
requests==2.31.0
Pillow==10.0.0
```

## 🗺️ Roadmap
- [ ] OAuth 2.0
- [ ] Custom prompt UI
- [ ] Multi-model support
- [ ] Response formatting

## 🤝 Contributing
1. Fork repo
2. Create branch
3. Commit changes
4. Push
5. Open PR

## 📜 License
Proprietary

---
<p align="right">(<a href="#readme-top">back to top</a>)</p>