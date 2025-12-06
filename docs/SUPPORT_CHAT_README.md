# Support Chat Feature

A live support chat widget powered by LLM (OpenAI) that provides contextual help based on your application's documentation and codebase.

## Features

- **Interactive Chat Widget**: A beautiful, unobtrusive chat bubble that appears on all main pages
- **Context-Aware Responses**: The assistant reads your documentation and code to provide accurate answers
- **Documentation Generation**: Can propose and save new help articles when gaps are detected
- **Conversation History**: Maintains context throughout the conversation
- **Article Management**: List, view, and generate help articles

## Setup Instructions

### 1. Install Dependencies

```powershell
pip install -r requirements-support.txt
```

This will install:
- `openai` - For LLM integration
- `python-dotenv` - For environment variable management

### 2. Configure OpenAI API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_flask_secret_key
```

To get an OpenAI API key:
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API keys section
4. Create a new API key
5. Copy it to your `.env` file

### 3. Add Documentation

Place your documentation files in the `docs/` folder:

```
docs/
├── getting-started.md
├── features.md
├── troubleshooting.md
└── api-reference.md
```

The support assistant will use these files to answer questions.

### 4. Run the Application

```powershell
python app/app.py
```

The chat widget will automatically appear on the dashboard and bug form pages.

## How It Works

### Backend Architecture

1. **Context Builder** (`app/support/context_builder.py`)
   - Scans the `docs/` directory and `help_articles/` folder
   - Optionally includes key source code files
   - Builds a context string (max 15KB) to send to the LLM

2. **LLM Helper** (`app/support/llm_helper.py`)
   - Handles OpenAI API integration
   - Supports both single-turn and multi-turn conversations
   - Includes error handling and fallbacks

3. **Routes** (`app/support/routes.py`)
   - `POST /api/support/chat` - Main chat endpoint
   - `POST /api/support/generate-article` - Save new help articles
   - `GET /api/support/articles` - List all help articles
   - `GET /api/support/article/<filename>` - Get specific article

4. **Prompts** (`app/support/prompts.py`)
   - Defines system prompts for the assistant
   - Includes templates for article generation

### Frontend Components

1. **Chat Widget** (`static/support-chat.js`)
   - Handles UI interactions
   - Manages conversation state
   - Sends requests to backend API
   - Renders markdown-like responses

2. **Styling** (`static/support-chat.css`)
   - Beautiful gradient design
   - Smooth animations
   - Responsive layout
   - Mobile-friendly

## Usage

### Asking Questions

Simply click the chat bubble and type your question:

- "How do I create a bug report?"
- "What are the different bug statuses?"
- "How can I filter bugs?"
- "What's the difference between reporter and manager roles?"

### Saving Help Articles

When the assistant detects a documentation gap, it will propose a new article:

1. The bot response will include a "Proposed Help Article" section
2. A "Save Article" button will appear
3. Click to save the article to `help_articles/`
4. The article becomes available for future reference

### Viewing Help Articles

```javascript
// API endpoint to list all articles
GET /api/support/articles

// API endpoint to get a specific article
GET /api/support/article/creating-a-bug-report.md
```

## Customization

### Adjust Context Size

In `app/support/context_builder.py`:

```python
context = build_context(
    base_path=base_path,
    query=user_message,
    include_docs=True,
    include_code=True,
    max_context_length=15000  # Adjust this value
)
```

### Change LLM Model

In `app/support/llm_helper.py`:

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",  # Change to gpt-4, gpt-3.5-turbo, etc.
    ...
)
```

### Modify System Prompt

Edit `app/support/prompts.py` to customize the assistant's behavior:

```python
SUPPORT_ASSISTANT_PROMPT = """You are a helpful support assistant...
[Customize the instructions here]
"""
```

### Style the Chat Widget

Edit `app/static/support-chat.css` to match your brand:

```css
.support-chat-bubble {
    background: linear-gradient(135deg, #YOUR_COLOR_1, #YOUR_COLOR_2);
}
```

## API Reference

### POST /api/support/chat

Send a message to the support assistant.

**Request:**
```json
{
    "message": "How do I create a bug?",
    "conversation": [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
}
```

**Response:**
```json
{
    "reply": "To create a bug report...",
    "timestamp": "2025-12-06T10:30:00"
}
```

### POST /api/support/generate-article

Generate and save a new help article.

**Request:**
```json
{
    "topic": "Creating Bug Reports",
    "conversation": [...]
}
```

**Response:**
```json
{
    "success": true,
    "article_path": "help_articles/creating-bug-reports.md",
    "title": "Creating Bug Reports",
    "content": "# Creating Bug Reports\n\n..."
}
```

### GET /api/support/articles

List all available help articles.

**Response:**
```json
{
    "articles": [
        {
            "title": "Creating Bug Reports",
            "path": "help_articles/creating-bug-reports.md",
            "created": "2025-12-06T10:30:00"
        }
    ]
}
```

## Troubleshooting

### "OpenAI API error: Authentication failed"

Make sure your `.env` file contains a valid `OPENAI_API_KEY`.

### Chat widget not appearing

1. Check browser console for JavaScript errors
2. Ensure `support-chat.js` and `support-chat.css` are loaded
3. Verify the files are in the `static/` directory

### "No documentation or context files found"

Add markdown files to the `docs/` directory or root-level `.md` files.

### LLM responses are slow

Consider:
1. Using a faster model (e.g., `gpt-3.5-turbo`)
2. Reducing `max_context_length`
3. Adding caching for frequently asked questions

## Cost Considerations

The OpenAI API charges per token. Approximate costs:

- **gpt-4o-mini**: ~$0.00015 per 1K input tokens, ~$0.0006 per 1K output tokens
- **gpt-3.5-turbo**: ~$0.0005 per 1K input tokens, ~$0.0015 per 1K output tokens
- **gpt-4**: Higher cost, better quality

Each conversation includes:
- System prompt + context (~2-5K tokens)
- User message (~50-200 tokens)
- Response (~200-800 tokens)

For a small team, costs should be minimal (< $10/month).

## Future Enhancements

Potential improvements:

1. **Semantic Search**: Use embeddings for better context retrieval
2. **Caching**: Cache common questions/answers
3. **Feedback System**: Let users rate responses
4. **Multiple Languages**: Support i18n
5. **Voice Input**: Add speech-to-text
6. **Analytics**: Track common questions to improve docs
7. **Fine-tuning**: Train a custom model on your docs

## Security Notes

- Never commit `.env` files to version control
- Add `.env` to `.gitignore`
- Use environment variables in production
- Consider rate limiting for the API endpoints
- Validate and sanitize all user inputs

## License

Part of the Bug Tracker application.
