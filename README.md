# AI Multi-Tool

An AI-powered toolkit that provides multiple AI utilities in one streamlined application. Built with Streamlit and powered by Nebius AI Studio API.

You can check the example of the deployed app on [ai-multi-tool.streamlit.app](https://ai-multi-tool.streamlit.app/).

## 🚀 Features

### 💬 Chatbot
- Interactive AI conversations
- Persistent chat history
- Multiple AI model options
- Customizable response parameters

### 📝 Text Checker
- Grammar and spelling correction
- Style and readability improvements
- Customizable editing instructions
- Professional text enhancement

### 👨‍🍳 Recipe Creator
- Generate recipes from available ingredients
- Multiple cooking method options (steamed, fried, baked, etc.)
- Customizable servings and dietary restrictions
- Consistent recipe formatting with prep times and nutritional info

### ⚙️ Advanced Settings
- **Model Selection**: Choose from 5 different AI models (Llama, DeepSeek, Qwen, Gemma, Mistral)
- **Temperature Control**: Adjust creativity vs. focus (0.0-1.0)
- **Token Limits**: Configure response length (128-8192 tokens)
- **Real-time Configuration**: All settings apply immediately

## 🔧 Setup & API Key

### Getting Your Nebius AI Studio API Key
1. Visit [Nebius AI Studio API Keys](https://studio.nebius.com/settings/api-keys)
2. Sign up or log in to your account
3. Generate a new API key
4. Copy and paste it into the sidebar when running the app

📖 [Full API documentation](https://docs.nebius.com/studio/api/authentication)

## 🏃‍♂️ Running the Application

### Option 1: Using Docker
```bash
# Build the container
docker build -t ai-multi-tool .

# Run the container
docker run -p 8501:8501 ai-multi-tool
```

### Option 2: Direct Streamlit
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will be available at `http://localhost:8501`.

## 📦 Dependencies

```
streamlit>=1.42.0
Authlib>=1.3.2  
requests>=2.31.0
```

## 🚀 Deployment

### Streamlit Cloud (Recommended)
1. Login to [Streamlit Cloud](https://share.streamlit.io/) with your GitHub account
2. Select this repository, branch, and `app.py` file
3. Click **Deploy**
4. Users will need to provide their own Nebius AI Studio API keys

### Docker Deployment
```bash
# Build and run with custom port
docker run -p 80:8501 ai-multi-tool
```

## 🔄 Development

### Project Structure
```
ai-multi-tool/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── README.md          # This file
└── .streamlit/        # Streamlit configuration
```

### Key Functions
- `call_nebius_api()` - Reusable API integration
- `chatbot_interface()` - Chat functionality
- `text_checker_interface()` - Text correction
- `recipe_creator_interface()` - Recipe generation

## 🤖 AI Models Available

1. **🚀 Meta Llama 3.1 8B** - Fast, lightweight for quick responses
2. **🧠 DeepSeek R1** - Advanced reasoning capabilities
3. **⚡ Qwen 2.5 72B** - Large multilingual model
4. **🔬 Google Gemma 2 9B** - Efficient Google model
5. **🇫🇷 Mistral Nemo** - European balanced performance

## 🔒 Privacy & Security

- **No data storage**: Conversations and inputs are not stored
- **API key security**: Keys are entered locally and not transmitted to our servers
- **Direct API calls**: Communication goes directly to Nebius AI Studio
- **Open source**: Full code transparency

## 🛠️ Code Review

For code review automation, an integrated GitHub workflow for Claude is available following [this guide](https://docs.anthropic.com/en/docs/claude-code/github-actions).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.