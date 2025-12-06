# Support Chat - Quick Reference

## Installation (5 minutes)

```powershell
# 1. Install dependencies
pip install openai python-dotenv

# 2. Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env
echo "SECRET_KEY=your-secret-key" >> .env

# 3. Run the app
cd app
python app.py

# 4. Visit http://127.0.0.1:5000 and look for chat bubble 💬
```

## System Prompt & Article Format

The AI uses a structured format when proposing new help articles:

```
=== PROPOSED_HELP_ARTICLE ===
Title: <clear, user-facing title>
Summary: <2–3 sentence summary>
Steps:
1. First step
2. Second step
3. Third step
Common issues & fixes:
- Issue: Problem description
  Fix: Solution
=== END_PROPOSED_HELP_ARTICLE ===
```

**Detection:**
- Frontend: Looks for `=== PROPOSED_HELP_ARTICLE ===` marker
- Backend: `extract_proposed_article()` extracts content and title
- Saves directly to `help_articles/` when user clicks "Save Article"

**Customize:** Edit `app/support/prompts.py` to change AI behavior

## API Endpoints

| Endpoint | Method | Purpose | Request Body |
|----------|--------|---------|--------------|
| `/api/support/chat` | POST | Send chat message | `{"message": "...", "conversation": [...]}` |
| `/api/support/generate-article` | POST | Generate help article | `{"topic": "...", "conversation": [...]}` |
| `/api/support/articles` | GET | List all articles | None |
| `/api/support/article/<filename>` | GET | Get specific article | None |

## File Structure

```
app/
├── app.py                    # Main Flask app (updated)
├── support/
│   ├── __init__.py          # Module init
│   ├── routes.py            # API endpoints
│   ├── llm_helper.py        # OpenAI integration
│   ├── context_builder.py   # Doc scanner
│   └── prompts.py           # System prompts
├── static/
│   ├── support-chat.css     # Widget styling
│   └── support-chat.js      # Widget logic
└── templates/
    ├── dashboard.html       # (updated with chat)
    └── bug_form.html        # (updated with chat)

docs/                         # Documentation source
help_articles/                # Generated articles
```

## Key Functions

### Backend (Python)

```python
# llm_helper.py
call_llm(system_prompt, user_message, context)
call_llm_with_history(system_prompt, conversation_history, context)

# context_builder.py
build_context(base_path, query, include_docs, include_code)
scan_directory(directory, extensions)

# routes.py
@support_bp.route('/chat', methods=['POST'])
@support_bp.route('/generate-article', methods=['POST'])
@support_bp.route('/articles', methods=['GET'])
```

### Frontend (JavaScript)

```javascript
// support-chat.js
class SupportChat {
    toggleChat()           // Open/close chat window
    sendMessage()          // Send user message to API
    addMessage()           // Add message to UI
    formatMarkdown()       // Basic markdown rendering
    saveArticle()          // Save proposed article
}
```

## Configuration

### Environment Variables (.env)
```env
OPENAI_API_KEY=sk-...    # Your OpenAI API key
SECRET_KEY=...           # Flask secret key
```

### Customization Points

**Change LLM Model:**
```python
# In llm_helper.py, line ~25
model="gpt-4o-mini"  # Change to gpt-4, gpt-3.5-turbo, etc.
```

**Adjust Context Size:**
```python
# In context_builder.py, line ~117
max_context_length=15000  # Increase/decrease in characters
```

**Modify System Prompt:**
```python
# In prompts.py
SUPPORT_ASSISTANT_PROMPT = """Your custom prompt here..."""
```

**Change Styling:**
```css
/* In support-chat.css */
.support-chat-bubble {
    background: linear-gradient(135deg, #YOUR_COLOR_1, #YOUR_COLOR_2);
}
```

## Testing Commands

```powershell
# Test OpenAI connection
python -c "import openai; openai.api_key='sk-...'; print('OK')"

# Test module import
cd app
python -c "from support import support_bp; print('Support module loaded')"

# Run app
python app.py

# Check for errors
# Look in terminal for Flask logs and browser console (F12) for JS errors
```

## Common Customizations

### Add New File Types to Context
```python
# In context_builder.py
RELEVANT_EXTENSIONS = {'.md', '.txt', '.py', '.html', '.css', '.js', '.json'}
```

### Exclude More Directories
```python
# In context_builder.py
EXCLUDE_DIRS = {
    '__pycache__', 'node_modules', '.git', 'venv',
    'your_custom_dir'  # Add here
}
```

### Change Chat Position
```css
/* In support-chat.css */
.support-chat-bubble {
    bottom: 20px;  /* Distance from bottom */
    right: 20px;   /* Distance from right */
    /* Change to: left: 20px; for left side */
}
```

### Adjust Token Limits
```python
# In llm_helper.py, call_llm function
max_tokens=2000  # Increase for longer responses
temperature=0.7  # 0.0 = deterministic, 1.0 = creative
```

## Cost Management

### Monitor Usage
- Visit https://platform.openai.com/usage
- Set spending limits in account settings
- Use gpt-4o-mini for lowest cost (~$0.002 per query)

### Reduce Costs
```python
# Use cheaper model
model="gpt-3.5-turbo"

# Reduce context size
max_context_length=8000

# Limit response length
max_tokens=1000

# Cache responses (advanced)
# Implement Redis/in-memory cache for common queries
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Chat bubble not showing | Check browser console (F12), verify JS/CSS files loaded |
| "Authentication failed" | Verify OPENAI_API_KEY in .env file |
| "No context found" | Add .md files to docs/ directory |
| Slow responses | Use gpt-3.5-turbo, reduce context size |
| Import errors | Run `pip install openai python-dotenv` |
| "Module 'support' not found" | Check you're in app/ directory |

## Useful Snippets

### Test Chat API with curl
```powershell
curl -X POST http://127.0.0.1:5000/api/support/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "How do I create a bug?"}'
```

### Check OpenAI API Key
```powershell
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY')[:10])"
```

### View Generated Articles
```powershell
ls help_articles
cat help_articles/your-article.md
```

### Clear Conversation History
Refresh the page - history is stored in JavaScript, not persisted

## Key Files to Edit

| Want to... | Edit this file |
|------------|----------------|
| Change system prompt | `app/support/prompts.py` |
| Modify API endpoints | `app/support/routes.py` |
| Adjust LLM behavior | `app/support/llm_helper.py` |
| Change what files are scanned | `app/support/context_builder.py` |
| Style the chat widget | `app/static/support-chat.css` |
| Modify chat functionality | `app/static/support-chat.js` |
| Add chat to new pages | Add CSS/JS includes to template |

## Resources

- **OpenAI API Docs**: https://platform.openai.com/docs
- **OpenAI Pricing**: https://openai.com/pricing
- **Flask Blueprints**: https://flask.palletsprojects.com/en/latest/blueprints/
- **Python dotenv**: https://pypi.org/project/python-dotenv/

## Sample Questions to Ask the Bot

Copy-paste these to test:

```
How do I create a bug report?
What's the difference between reporter and manager roles?
How can I filter bugs by status?
What are the different severity levels?
How do I edit an existing bug?
How do I delete a bug?
What information should I include in a bug report?
Can I assign bugs to other users?
How do I generate a report?
What does "In Progress" status mean?
```

## Next Steps

1. ✅ Get OpenAI API key → https://platform.openai.com/
2. ✅ Install dependencies → `pip install -r requirements-support.txt`
3. ✅ Create .env file with API key
4. ✅ Run app → `python app/app.py`
5. ✅ Test chat widget
6. ✅ Add documentation to `docs/`
7. ✅ Customize styling to match your brand
8. ✅ Test article generation
9. ✅ Set up monitoring for API usage
10. ✅ Deploy to production

## Support

- **Full Documentation**: `docs/SUPPORT_CHAT_README.md`
- **Setup Guide**: `SETUP_SUPPORT_CHAT.md`
- **Architecture**: `ARCHITECTURE.md`
- **Implementation Details**: `SUPPORT_CHAT_IMPLEMENTATION.md`

---

**Quick help?** The chat bubble in your app can answer these questions too! 💬
