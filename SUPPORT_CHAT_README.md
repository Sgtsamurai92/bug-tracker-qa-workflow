# 🤖 AI Support Chat Widget - Complete Implementation

> A beautiful, intelligent support chat powered by OpenAI that provides contextual help based on your documentation and code.

![Status](https://img.shields.io/badge/status-ready-brightgreen) ![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange)

---

## ✨ Features

- 💬 **Beautiful Chat Widget** - Unobtrusive bubble that opens to a full chat interface
- 🧠 **Context-Aware AI** - Reads your docs and code to provide accurate answers
- 📝 **Auto Documentation** - Detects gaps and generates new help articles
- 🎨 **Gradient Design** - Modern purple/pink gradients with smooth animations
- 📱 **Mobile Responsive** - Works perfectly on all devices
- ⚡ **Fast & Efficient** - Uses lightweight GPT-4o-mini model
- 🔒 **Secure** - Environment variables, input validation, error handling
- 📚 **Smart Context** - Automatically scans docs and includes relevant code

---

## 🚀 Quick Start (5 Minutes)

### 1. Install Dependencies
```powershell
pip install openai python-dotenv
```

### 2. Add Your OpenAI API Key
Create `.env` file in project root:
```env
OPENAI_API_KEY=sk-your-api-key-here
SECRET_KEY=your-flask-secret-key
```

**Get API Key:** https://platform.openai.com/api-keys

### 3. Run the Application
```powershell
cd app
python app.py
```

### 4. Test It Out
1. Open http://127.0.0.1:5000
2. Log in with: `reporter@example.com` / `password123`
3. Look for the purple chat bubble 💬 in bottom-right
4. Click and ask: *"How do I create a bug report?"*

**That's it!** 🎉

---

## 📁 What Was Built

### Backend (Python/Flask)
```
app/support/
├── routes.py            # 4 API endpoints for chat, articles
├── llm_helper.py        # OpenAI integration & conversation handling
├── context_builder.py   # Scans docs/code, builds context
└── prompts.py           # System prompts for the AI assistant
```

### Frontend (JavaScript/CSS)
```
app/static/
├── support-chat.js      # Chat widget logic (371 lines)
└── support-chat.css     # Beautiful styling (346 lines)
```

### Documentation
```
docs/
├── getting-started.md        # User guide for bug tracker
└── SUPPORT_CHAT_README.md    # Full technical documentation

SETUP_SUPPORT_CHAT.md         # Quick setup guide
ARCHITECTURE.md               # System architecture diagrams
QUICK_REFERENCE.md            # Developer cheat sheet
VISUAL_PREVIEW.md             # UI mockups and styling
SUPPORT_CHAT_IMPLEMENTATION.md # Complete implementation details
```

---

## 🎯 How It Works

```
1. User clicks chat bubble 💬
2. Types question: "How do I create a bug?"
3. Frontend sends to: POST /api/support/chat
4. Backend:
   - Scans docs/ directory for markdown files
   - Scans help_articles/ for generated content
   - Optionally includes source code
   - Builds context string (max 15KB)
   - Sends to OpenAI GPT-4o-mini with context
5. AI generates contextual response
6. Frontend displays answer with markdown formatting
7. If AI detects doc gap, shows "Save Article" button
8. User can save → Creates new help article
```

---

## 📖 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/support/chat` | POST | Send message, get AI response |
| `/api/support/generate-article` | POST | Generate & save help article |
| `/api/support/articles` | GET | List all help articles |
| `/api/support/article/<filename>` | GET | Get specific article content |

### Example Request
```powershell
curl -X POST http://localhost:5000/api/support/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "How do I delete a bug?"}'
```

---

## 🎨 Customization

### Change Colors
Edit `app/static/support-chat.css`:
```css
.support-chat-bubble {
    background: linear-gradient(135deg, #YOUR_COLOR_1, #YOUR_COLOR_2);
}
```

### Change AI Model
Edit `app/support/llm_helper.py`:
```python
model="gpt-4"  # Options: gpt-4, gpt-3.5-turbo, gpt-4-turbo
```

### Adjust Context Size
Edit `app/support/context_builder.py`:
```python
max_context_length=15000  # Increase or decrease
```

### Modify System Prompt
Edit `app/support/prompts.py`:
```python
SUPPORT_ASSISTANT_PROMPT = """Your custom instructions..."""
```

---

## 💰 Cost Estimation

Using **gpt-4o-mini** (recommended):
- Input: ~$0.00015 per 1K tokens
- Output: ~$0.0006 per 1K tokens
- **Per conversation**: ~$0.002-0.004
- **Monthly (small team)**: ~$5-15

Set spending limits at: https://platform.openai.com/account/billing/limits

---

## 🔧 Configuration

### Environment Variables
```env
# Required
OPENAI_API_KEY=sk-...              # Your OpenAI API key

# Optional
SECRET_KEY=...                     # Flask secret key
FLASK_ENV=development              # development or production
```

### File Structure
```
bug-tracker-qa-workflow/
├── .env                           # Your secrets (not in git)
├── app/
│   ├── app.py                     # Main Flask app (updated)
│   ├── support/                   # Support module
│   ├── static/                    # CSS/JS for chat
│   └── templates/                 # HTML (updated)
├── docs/                          # Documentation source
├── help_articles/                 # Generated articles
└── [documentation files...]
```

---

## 📚 Documentation Guide

### For Complete Details
- **[SETUP_SUPPORT_CHAT.md](SETUP_SUPPORT_CHAT.md)** - Full setup instructions
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture & diagrams
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Developer cheat sheet
- **[docs/SUPPORT_CHAT_README.md](docs/SUPPORT_CHAT_README.md)** - Technical documentation
- **[VISUAL_PREVIEW.md](VISUAL_PREVIEW.md)** - UI mockups

### For Users
- **[docs/getting-started.md](docs/getting-started.md)** - How to use the bug tracker

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] Chat bubble appears on dashboard
- [ ] Bubble opens chat window on click
- [ ] Can type and send messages
- [ ] Bot responds with contextual answers
- [ ] Messages are formatted nicely
- [ ] Loading animation shows while waiting
- [ ] Can save proposed articles
- [ ] Articles appear in help_articles/
- [ ] Works on mobile devices

### Test Questions
```
✓ How do I create a bug report?
✓ What's the difference between reporter and manager?
✓ How can I filter bugs by status?
✓ What are severity levels?
✓ How do I edit a bug?
```

---

## 🐛 Troubleshooting

### Chat bubble not appearing
1. Open browser console (F12)
2. Check for JavaScript errors
3. Verify files loaded: `support-chat.js`, `support-chat.css`
4. Clear browser cache

### "Authentication failed" error
1. Check `.env` file exists
2. Verify `OPENAI_API_KEY` is set correctly
3. Test key: Visit https://platform.openai.com/
4. Ensure key has available credits

### "No context found" warning
1. Add markdown files to `docs/` directory
2. Check file permissions
3. Verify `BASE_PATH` configuration in `app.py`

### Slow responses
1. Switch to `gpt-3.5-turbo` (faster but less capable)
2. Reduce `max_context_length` to 8000
3. Check OpenAI API status: https://status.openai.com/

---

## 🔒 Security Best Practices

✅ **Already Implemented:**
- `.env` in `.gitignore`
- Environment variable loading
- Error handling without exposing internals
- Input validation

⚠️ **Recommended for Production:**
- Add rate limiting to API endpoints
- Implement user authentication on chat endpoints
- Set up CORS properly
- Add request logging
- Rotate API keys regularly
- Monitor usage for anomalies

---

## 🚦 Next Steps

### Immediate
1. ✅ Get OpenAI API key
2. ✅ Install dependencies
3. ✅ Test basic chat functionality
4. ✅ Add your own documentation to `docs/`

### Short-term
5. Customize styling to match your brand
6. Adjust system prompt for your use case
7. Test article generation feature
8. Set up API usage monitoring

### Long-term
9. Add semantic search for better context retrieval
10. Implement caching for common questions
11. Add user feedback system
12. Create analytics dashboard
13. Fine-tune model on your specific docs

---

## 🆘 Getting Help

### Resources
- **OpenAI API Docs**: https://platform.openai.com/docs
- **OpenAI Pricing**: https://openai.com/pricing
- **Flask Docs**: https://flask.palletsprojects.com/
- **OpenAI Status**: https://status.openai.com/

### In This Repository
- Check the documentation files listed above
- Review code comments in source files
- Look at example markdown in `docs/getting-started.md`

---

## 🎯 Key Features Summary

| Feature | Status | Location |
|---------|--------|----------|
| Chat Widget UI | ✅ Complete | `static/support-chat.js`, `static/support-chat.css` |
| Backend API | ✅ Complete | `support/routes.py` |
| OpenAI Integration | ✅ Complete | `support/llm_helper.py` |
| Context Builder | ✅ Complete | `support/context_builder.py` |
| Article Generation | ✅ Complete | API endpoint + frontend button |
| Documentation | ✅ Complete | Multiple .md files |
| Mobile Support | ✅ Complete | Responsive CSS |
| Error Handling | ✅ Complete | Throughout codebase |

---

## 📊 Project Stats

- **Lines of Code**: ~1,500+ (backend + frontend)
- **Files Created**: 15+
- **API Endpoints**: 4
- **Documentation Pages**: 6
- **Dependencies**: 2 (openai, python-dotenv)
- **Setup Time**: ~5 minutes
- **Cost**: ~$5-15/month for small team

---

## 📝 License

Part of the Bug Tracker application. Use as needed for your project.

---

## 🙏 Credits

Built with:
- **OpenAI GPT-4o-mini** - AI responses
- **Flask** - Backend framework
- **Vanilla JavaScript** - Frontend logic
- **CSS3** - Beautiful styling

---

## 🎉 You're All Set!

The support chat is now fully integrated into your bug tracker app. Just add your OpenAI API key and start chatting!

**Need help?** Ask the chat widget itself! 💬

---

**Made with ❤️ for better customer support**
