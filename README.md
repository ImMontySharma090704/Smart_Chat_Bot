You're getting this error because the Google Generative AI SDK (used to access models like Gemini) doesn't have the necessary credentials to authenticate your requests.

Here’s how to fix it depending on how you want to authenticate:

---

### ✅ Quick Fix: Use API Key

The easiest way (especially for development) is to **use your API key**. You can do this in your Python script:

#### 1. Get an API key:
- Go to the [Google AI Studio](https://makersuite.google.com/app/apikey) (log in with your Google account)
- Click **Get API Key** (or copy an existing one)

#### 2. Add this to your Python script:
```python
import google.generativeai as genai

genai.configure(api_key="your-api-key-here")

models = genai.list_models()
for m in models:
    print(m)
```

✅ That should fix the error you're seeing.

---

### 🔐 Alternative: Set an environment variable

Instead of hardcoding the API key, you can set it as an environment variable:

#### Windows (in Command Prompt or PowerShell):
```powershell
$env:GOOGLE_API_KEY="your-api-key-here"
python test.py
```

#### Or in your script:
```python
import os
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

---

### 🧑‍💼 Advanced Option: Use OAuth (Application Default Credentials)

This is better for production apps or services running on Google Cloud.

You'll need to:

1. Set up a GCP project
2. Enable the **Generative Language API**
3. Use `gcloud auth application-default login`
4. Set the proper scopes

Follow this guide for setup: https://ai.google.dev/gemini-api/docs/oauth

---

Let me know if you want help setting up OAuth, or just want to get the API key method working first.
