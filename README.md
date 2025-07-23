# AI Multi-tool
An AI multi-tool that simplifies daily AI usage.
You can check example of the deployed app on [ai-multi-tool.streamlit.app](https://ai-multi-tool.streamlit.app/).

## Authentication
This application uses Google OAuth authentication following the [Streamlit Google authentication guide](https://docs.streamlit.io/develop/tutorials/authentication/google). Users must log in with their Google account to access the application.

## Local Development

### Prerequisites
Before running locally, create a `.streamlit/secrets.toml` file (not included in the repository) with your Google OAuth credentials:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

### Running the Application

#### Option 1: Using Docker
```bash
docker build -t ai-multi-tool .
docker run -p 8501:8501 ai-multi-tool
```

#### Option 2: Direct Streamlit
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`.

# Deployment
The fastest and easiest way to deploy your streamlit application is using [Streamlit Cloud](https://streamlit.io/cloud).
For deployment you need:
1. Login to [Streamlit Cloud](https://share.streamlit.io/) with your GitHub account.
2. Pick a repo with application, branch, and file.
3. **Configure secrets**: Add your authentication data to the Streamlit Cloud portal following the [secrets management guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management). Use the same format as the local `.streamlit/secrets.toml` file.
4. Click **Deploy**. Then any time you do a `git push` your app will update immediately.

## Code Review
For reviewing the code, an integrated GitHub workflow for Claude is available following [this guide](https://docs.anthropic.com/en/docs/claude-code/github-actions).
