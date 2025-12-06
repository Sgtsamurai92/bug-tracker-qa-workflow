# Support Chat Setup - Quick Start

## Prerequisites
- Python 3.8+ installed
- OpenAI API account and key
- Existing bug tracker application

## Installation Steps

### 1. Install Dependencies
```powershell
pip install openai python-dotenv
```

Or use the requirements file:
```powershell
pip install -r requirements-support.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root (if it doesn't exist):

```powershell
# Create .env file
New-Item -Path .env -ItemType File -Force
```

Add the following content:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
SECRET_KEY=your-flask-secret-key-here
```

**To get your OpenAI API key:**
1. Visit https://platform.openai.com/
2. Sign in or create an account
3. Go to "API Keys" section
4. Click "Create new secret key"
5. Copy the key and paste it in your `.env` file

### 3. Verify Installation

Check that the support module is loaded:

```powershell
cd app
python -c "from support import support_bp; print('Support module loaded successfully!')"
```

### 4. Run the Application

```powershell
# From project root
cd app
python app.py
```

The application should start on `http://127.0.0.1:5000`

### 5. Test the Support Chat

1. Open your browser to `http://127.0.0.1:5000`
2. Log in with test credentials:
   - Email: `reporter@example.com`
   - Password: `password123`
3. Look for the purple chat bubble in the bottom-right corner
4. Click it to open the chat window
5. Try asking: "How do I create a bug report?"

## Verification Checklist

- [ ] Dependencies installed
- [ ] `.env` file created with OpenAI API key
- [ ] Application starts without errors
- [ ] Chat bubble appears on dashboard
- [ ] Chat window opens when clicking bubble
- [ ] Bot responds to messages
- [ ] No JavaScript errors in browser console

## Troubleshooting

### Error: "Import 'openai' could not be resolved"
**Solution:** Install the openai package
```powershell
pip install openai
```

### Error: "OPENAI_API_KEY not found"
**Solution:** Check your `.env` file exists and contains:
```env
OPENAI_API_KEY=sk-...
```

### Chat bubble doesn't appear
**Solution:** 
1. Check browser console for errors (F12)
2. Verify `support-chat.js` and `support-chat.css` are in `app/static/`
3. Ensure templates include the CSS/JS files

### "No documentation or context files found"
**Solution:** Add markdown files to the `docs/` directory or root directory

### API Rate Limit Error
**Solution:** 
- Wait a few minutes and try again
- Check your OpenAI account has available credits
- Upgrade your OpenAI plan if needed

## File Structure Verification

Ensure you have these files:

```
bug-tracker-qa-workflow/
├── .env (YOUR API KEY HERE)
├── .env.example (template)
├── requirements-support.txt
├── app/
│   ├── app.py (updated with support_bp)
│   ├── support/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── llm_helper.py
│   │   ├── context_builder.py
│   │   └── prompts.py
│   ├── static/
│   │   ├── support-chat.css
│   │   └── support-chat.js
│   └── templates/
│       ├── dashboard.html (updated)
│       └── bug_form.html (updated)
├── docs/
│   ├── getting-started.md
│   └── SUPPORT_CHAT_README.md
└── help_articles/ (empty, will be populated)
```

## Next Steps

Once everything is working:

1. **Add More Documentation**: Create markdown files in `docs/` directory
2. **Customize Prompts**: Edit `app/support/prompts.py` to match your needs
3. **Adjust Styling**: Modify `app/static/support-chat.css` for your brand
4. **Test Article Generation**: Ask the bot to create a help article
5. **Monitor Usage**: Check OpenAI dashboard for API usage and costs

## Cost Management

To keep costs low:

1. **Use gpt-4o-mini** (default, cheapest)
2. **Limit context size** (default 15KB)
3. **Monitor usage** on OpenAI dashboard
4. **Set spending limits** in OpenAI account settings

Expected costs for small team: **$5-10/month**

## Security Best Practices

- ✅ Never commit `.env` to git (already in .gitignore)
- ✅ Use different API keys for dev/prod
- ✅ Rotate keys periodically
- ✅ Monitor API usage for anomalies
- ✅ Add rate limiting in production

## Support

For issues or questions:
1. Check `docs/SUPPORT_CHAT_README.md` for detailed documentation
2. Review error messages in browser console (F12)
3. Check Flask application logs
4. Verify OpenAI API status: https://status.openai.com/

## Summary

You've successfully set up an AI-powered support chat that:
- ✅ Provides contextual help based on your documentation
- ✅ Can generate new help articles on-demand
- ✅ Maintains conversation history
- ✅ Works beautifully on all pages

Happy chatting! 💬
