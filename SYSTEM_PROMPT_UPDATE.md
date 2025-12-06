# Support Chat System Prompt Update - Summary

## Changes Made

### 1. Updated System Prompt (`app/support/prompts.py`)

**Previous format:**
```
**Proposed Help Article:**
[Title of the article]
[Brief outline or draft content]
```

**New structured format:**
```
=== PROPOSED_HELP_ARTICLE ===
Title: <clear, user-facing title>
Summary: <2–3 sentence summary of what this article covers>
Steps:
1. ...
2. ...
3. ...
Common issues & fixes:
- Issue: ...
  Fix: ...
- Issue: ...
  Fix: ...
=== END_PROPOSED_HELP_ARTICLE ===
```

### 2. Enhanced AI Behavior Rules

The new system prompt includes:

✅ **Clear responsibilities** - Help end users with "how do I..." questions  
✅ **Context awareness** - Use repo/docs context for accurate answers  
✅ **Documentation referencing** - Cite existing docs when applicable  
✅ **Gap detection** - Propose articles for common/undocumented questions  
✅ **Security** - Never expose internal paths, traces, or credentials  
✅ **Honesty** - Admit when unsure, ask for clarification  
✅ **Conciseness** - Short, practical answers with bullet points  
✅ **Friendly tone** - Act like a helpful product specialist  

### 3. Updated Frontend Detection (`app/static/support-chat.js`)

**New detection logic:**
```javascript
checkForProposedArticle(content) {
    // Detect the new structured format
    if (content.includes('=== PROPOSED_HELP_ARTICLE ===')) {
        // Extract article block and title
        // Show "Save Article" button
    }
    // Fallback to old format for backwards compatibility
    else if (content.includes('**Proposed Help Article:**')) {
        // Old detection logic
    }
}
```

**Features:**
- Detects new structured format with clear markers
- Extracts title using regex: `Title:\s*(.+)`
- Maintains backwards compatibility with old format
- Shows user-friendly "Save Article" button

### 4. Enhanced Backend Processing (`app/support/routes.py`)

**New helper function:**
```python
def extract_proposed_article(response_text):
    """
    Extract the proposed help article from the assistant's response.
    Returns: (has_article: bool, article_content: str, title: str)
    """
```

**Updated `/api/support/generate-article` endpoint:**
- Checks conversation history for proposed articles
- Extracts structured content directly if available
- Falls back to LLM generation if not found
- Uses extracted title from the article block

### 5. Added Test Suite (`test_support_chat.py`)

**Tests include:**
- ✅ Module imports verification
- ✅ System prompt configuration check
- ✅ Article extraction with valid format
- ✅ No article detection
- ✅ Malformed article handling

**Run tests:**
```powershell
python test_support_chat.py
```

## Benefits of New Format

### 1. **Structured & Predictable**
- Clear markers (`===`) make detection reliable
- Consistent format for all proposed articles
- Easy to parse and extract

### 2. **Better User Experience**
- Title is clearly identified
- Summary provides context
- Steps are numbered and clear
- Common issues section helps troubleshooting

### 3. **Improved Backend Processing**
- Direct extraction from conversation
- No need to regenerate with LLM
- Faster article saving
- Cost-effective (fewer API calls)

### 4. **Security & Safety**
- Explicitly instructs AI to avoid exposing sensitive info
- Translates technical details to user-friendly language
- Prevents raw stack traces or credentials in responses

### 5. **Backwards Compatibility**
- Old format (`**Proposed Help Article:**`) still works
- Gradual migration path
- No breaking changes

## How It Works

### User Flow

```
1. User: "How do I bulk edit bugs?"
   ↓
2. AI detects: Question is common + docs are missing
   ↓
3. AI responds with:
   - Friendly answer explaining current workflow
   - === PROPOSED_HELP_ARTICLE === block with full article
   ↓
4. Frontend detects article markers
   ↓
5. Shows "💡 Save this as a help article?" button
   ↓
6. User clicks "Save Article"
   ↓
7. Backend extracts article from conversation
   ↓
8. Saves to help_articles/bulk-editing-bugs.md
   ↓
9. Article becomes available for future queries
```

### Technical Flow

```
Frontend (support-chat.js)
    ↓
checkForProposedArticle()
    ↓ [detects === markers]
Extract title & show button
    ↓ [user clicks]
POST /api/support/generate-article
    ↓
Backend (routes.py)
    ↓
extract_proposed_article()
    ↓ [finds article in conversation]
Save directly to file
    ↓ [no LLM call needed]
Return success
```

## Example Interaction

### User Question
```
How do I filter bugs by priority?
```

### AI Response
```
To filter bugs by priority, here's what you can do:

Currently, the bug tracker shows all bugs in a table. You can:
1. Look at the Priority column to see each bug's priority
2. Manually scan for High, Medium, or Low priority items
3. Use your browser's search (Ctrl+F) to find specific priorities

However, there isn't a built-in priority filter yet, though this would be 
a useful feature for managing bugs efficiently.

=== PROPOSED_HELP_ARTICLE ===
Title: Filtering Bugs by Priority
Summary: Learn how to find and work with bugs based on their priority level. 
While a dedicated filter isn't available yet, this article shows you practical 
workarounds to focus on high-priority items.
Steps:
1. Navigate to the dashboard page
2. Look at the Priority column in the bugs table
3. Use Ctrl+F (browser search) to find "High" or "Critical" priorities
4. Click on a bug to view or edit it
5. Consider using status + priority together to organize your workflow
Common issues & fixes:
- Issue: Can't find high-priority bugs quickly
  Fix: Sort bugs manually by scanning the Priority column, or use browser search
- Issue: Need to work on only critical bugs
  Fix: Create a process where critical bugs are assigned immediately upon creation
=== END_PROPOSED_HELP_ARTICLE ===

Would you like me to save this as a help article for future reference?
```

### What Happens Next
1. Frontend shows "Save Article" button
2. User clicks it
3. Article saved to `help_articles/filtering-bugs-by-priority.md`
4. Future users asking the same question will see this article referenced

## Testing

### Run Test Suite
```powershell
python test_support_chat.py
```

### Expected Output
```
✓ All modules imported successfully
✓ System prompt is correctly configured
✓ Test 1: Valid article format - PASSED
✓ Test 2: No article in response - PASSED
✓ Test 3: Malformed article - PASSED
✓ ALL TESTS PASSED
```

### Manual Testing
1. Start the app: `cd app && python app.py`
2. Open chat widget
3. Ask: "How do I do something not in the docs?"
4. Verify AI includes `=== PROPOSED_HELP_ARTICLE ===` block
5. Click "Save Article" button
6. Check `help_articles/` directory for new file

## Files Modified

| File | Changes | Purpose |
|------|---------|---------|
| `app/support/prompts.py` | Updated system prompt | Define AI behavior with new format |
| `app/static/support-chat.js` | Updated `checkForProposedArticle()` | Detect new article format |
| `app/support/routes.py` | Added `extract_proposed_article()` | Extract articles from responses |
| `test_support_chat.py` | Created test suite | Verify system works correctly |
| `QUICK_REFERENCE.md` | Added prompt format section | Developer documentation |

## Configuration

### Location
**System Prompt:** `app/support/prompts.py` (line 5)

### Customization
Edit the prompt to:
- Change tone (formal, casual, technical)
- Add company-specific context
- Modify article structure
- Add/remove behavior rules
- Adjust output format

### Example: Change Article Format
```python
=== PROPOSED_HELP_ARTICLE ===
## <title>
**Summary:** <summary>
**How To:**
- Step 1
- Step 2
**Troubleshooting:**
| Problem | Solution |
| --- | --- |
| ... | ... |
=== END_PROPOSED_HELP_ARTICLE ===
```

## Troubleshooting

### Article Not Being Detected
1. Check console for: `content.includes('=== PROPOSED_HELP_ARTICLE ===')`
2. Verify markers are exact (case-sensitive, spacing)
3. Ensure `=== END_PROPOSED_HELP_ARTICLE ===` is present

### Wrong Title Extracted
1. Check title format: `Title: Your Title Here`
2. Verify no extra characters before "Title:"
3. Check regex in `extract_proposed_article()`

### Old Format Still Used
1. Restart Flask application
2. Clear browser cache
3. Check `prompts.py` was saved correctly
4. Run test suite to verify

## Next Steps

1. ✅ **System prompt updated** with new structured format
2. ✅ **Frontend detection** enhanced with backwards compatibility
3. ✅ **Backend extraction** optimized to use proposed articles
4. ✅ **Test suite** created and passing

**Ready to use!** The chat will now:
- Provide better-structured article proposals
- Save articles more efficiently
- Maintain consistent formatting
- Offer improved user experience

## Support

### Questions?
- Check `QUICK_REFERENCE.md` for developer tips
- Review `docs/SUPPORT_CHAT_README.md` for full documentation
- Run `python test_support_chat.py` to diagnose issues

### Need to Customize?
- Edit `app/support/prompts.py` for behavior changes
- Modify article format in the prompt
- Adjust detection in `support-chat.js`
- Update extraction in `routes.py`

---

**Updated:** December 6, 2025  
**Status:** ✅ Tested and Working  
**Version:** 2.0 (Structured Article Format)
