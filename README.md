# Smart Menu Base - All-in-One Menu Dashboard

A comprehensive Streamlit-based dashboard that provides multiple automation and management tools in one place.

## 🚀 Features

### 📱 Python Automation Tasks
- **WhatsApp Messaging**: Schedule and send WhatsApp messages
- **Email Automation**: Send emails with custom content
- **Instagram Posting**: Upload photos with captions
- **Voice Calls**: Make calls using Twilio
- **AI Integration**: Ask questions to Gemini AI
- **Web Scraping**: Extract content from websites

### 🌐 HTML/JS Integration
- Camera access and photo capture
- SMS sending capabilities
- GPS location services
- Gmail integration
- Social media posting (Facebook/Twitter)
- WhatsApp Web integration
- Weather information

### 🐧 Linux System Management
- Remote SSH terminal access
- Command execution on Linux servers
- AI-powered command explanations
- Comprehensive Linux command library

### 🐳 Docker Container Management
- Remote Docker operations via SSH
- Container lifecycle management
- Image management
- Network and volume operations
- AI-powered Docker command explanations

### 🤖 Machine Learning
- CSV data upload and analysis
- Linear Regression models
- Random Forest models
- Real-time predictions
- Data visualization
- Feature importance analysis

### 🪟 Windows Automation
- System application launchers
- File and folder operations
- System control (shutdown, restart, lock)

### 📁 Smart File Explorer
- Intelligent file management
- AI-powered file search
- File operations (rename, delete, create)
- Folder summarization

## 🛠️ Installation

1. **Clone the repository**
   ```bash
       git clone https://github.com/yourusername/smart-menu-base.git
    cd smart-menu-base
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Keys** (Optional)
   - Gemini AI API Key (for AI features)
   - Twilio credentials (for voice calls)
   - Instagram credentials (for posting)

4. **Run the application**
   ```bash
   streamlit run "all in 1/fullmenu.py"
   ```

## 📋 Requirements

- Python 3.7+
- Streamlit
- Paramiko (for SSH connections)
- PyWhatKit (for WhatsApp automation)
- Instagrapi (for Instagram automation)
- Twilio (for voice calls)
- Google Generative AI (for Gemini integration)
- Scikit-learn (for machine learning)
- Pandas, Matplotlib, Seaborn (for data analysis)

## 🔧 Configuration

### API Keys Setup
The application will prompt for API keys when needed:
- **Gemini AI**: Enter your API key in the respective sections
- **Twilio**: Provide SID and Auth Token for voice calls
- **Instagram**: Username and password for posting

### File Paths
- HTML files should be placed in a folder and the path specified in the HTML/JS Tasks section
- Customize music folder paths in Windows Tasks as needed

## 🚨 Security Notes

- **Never commit API keys or credentials to version control**
- **Use environment variables for sensitive information**
- **The application prompts for credentials when needed**
- **All personal data has been removed from the repository**

## 📝 Usage Examples

### WhatsApp Automation
1. Navigate to "Python Tasks"
2. Select "Send WhatsApp Message"
3. Enter phone number, message, and timing
4. Click "Send WhatsApp"

### Linux Remote Management
1. Go to "Linux Menu"
2. Enter SSH credentials
3. Execute commands remotely
4. Use AI to understand commands

### Machine Learning
1. Upload CSV file in "Machine Learning" section
2. Select features and target variables
3. Choose model type
4. Train and get predictions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

- This tool is for educational and personal use
- Respect privacy and terms of service of third-party platforms
- Use responsibly and in compliance with applicable laws
- The developers are not responsible for misuse of this software

## 🆘 Support

For issues and questions:
- Create an issue on GitHub
- Check the documentation
- Review the code comments

---

**Built with ❤️ by Arushi Soni**
