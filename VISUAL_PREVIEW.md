# Support Chat Widget - Visual Preview

## Chat Bubble (Closed State)

```
┌────────────────────────────────────────────────┐
│                                                │
│                    Bug Tracker Dashboard       │
│                                                │
│  ┌──────────────────────────────────────┐     │
│  │  Bugs List                           │     │
│  │  ┌────────────────────────────────┐  │     │
│  │  │ ID | Title | Status | Actions  │  │     │
│  │  ├────────────────────────────────┤  │     │
│  │  │ 1  | Bug   | Open   | Edit Del │  │     │
│  │  └────────────────────────────────┘  │     │
│  └──────────────────────────────────────┘     │
│                                                │
│                                                │
│                                                │
│                                          ┌───┐ │
│                                          │💬 │ │ ← Purple gradient bubble
│                                          └───┘ │
└────────────────────────────────────────────────┘
                                              ▲
                                              │
                                    Bottom-right corner
```

## Chat Window (Open State)

```
┌────────────────────────────────────────────────┐
│                                                │
│                    Bug Tracker Dashboard       │
│                                                │
│  ┌──────────────────────────────────────┐     │
│  │  Bugs List                           │     │
│  └──────────────────────────────────────┘     │
│                                                │
│                          ┌──────────────────┐  │
│                          │ Support Assist. ×│  │ ← Header (purple gradient)
│                          ├──────────────────┤  │
│                          │                  │  │
│                          │ 🤖  Hi! I'm     │  │ ← Bot message
│                          │    your support │  │
│                          │    assistant.   │  │
│                          │                  │  │
│                          │         👤      │  │
│                          │   How do I      │  │ ← User message
│                          │   create a bug? │  │
│                          │                  │  │
│                          │ 🤖  To create   │  │
│                          │    a bug...     │  │ ← Bot response
│                          │                  │  │
│                          ├──────────────────┤  │
│                          │ [__________] ➤  │  │ ← Input area
│                          └──────────────────┘  │
│                                          ┌───┐ │
│                                          │💬 │ │ ← Active bubble (pink gradient)
│                                          └───┘ │
└────────────────────────────────────────────────┘
```

## Detailed Chat Window Layout

```
┌─────────────────────────────────────────────────┐
│ Support Assistant                             × │ ← Header
├─────────────────────────────────────────────────┤
│                                                 │ ← Messages Area
│  ┌──────────────────────────────────────────┐  │   (scrollable)
│  │ 🤖  Welcome Message                      │  │
│  │     • How to use                         │  │
│  │     • Features                           │  │
│  │     • Documentation                      │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│                   ┌──────────────────────────┐ │
│                   │ How do I create a bug?  👤│ │
│                   └──────────────────────────┘ │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │ 🤖  To create a bug report:              │  │
│  │                                          │  │
│  │     1. Click "Create Bug" button        │  │
│  │     2. Fill in the form                 │  │
│  │     3. Click "Submit"                   │  │
│  │                                          │  │
│  │     ┌────────────────────────────────┐  │  │
│  │     │ 💡 Save as help article?       │  │  │
│  │     │           [Save Article]       │  │  │
│  │     └────────────────────────────────┘  │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
├─────────────────────────────────────────────────┤
│ Type your message...              ➤             │ ← Input Area
└─────────────────────────────────────────────────┘
```

## Color Scheme

### Chat Bubble
- **Default**: Purple gradient (#667eea → #764ba2)
- **Active**: Pink gradient (#f093fb → #f5576c)
- **Hover**: Slightly larger with deeper shadow

### Chat Window
- **Header**: Purple gradient (#667eea → #764ba2)
- **Background**: Light gray (#f7f8fa)
- **User Messages**: Purple gradient (#667eea → #764ba2)
- **Bot Messages**: White (#ffffff)
- **Input Border**: Gray (#d1d5db), Blue on focus (#667eea)

## Animations

### Slide Up (Chat Window Opening)
```
Initial State:
  opacity: 0
  translateY: 20px

Final State:
  opacity: 1
  translateY: 0

Duration: 0.3s ease
```

### Fade In (New Messages)
```
Initial State:
  opacity: 0
  translateY: 10px

Final State:
  opacity: 1
  translateY: 0

Duration: 0.3s ease
```

### Loading Dots
```
● ● ●  →  • ○ ○  →  ○ • ○  →  ○ ○ •  →  ● ● ●
(Continuous animation while waiting for response)
```

### Hover Effect (Bubble)
```
Default:
  scale: 1.0
  shadow: 0 4px 12px rgba(0,0,0,0.15)

Hover:
  scale: 1.1
  shadow: 0 6px 16px rgba(0,0,0,0.2)

Transition: 0.3s ease
```

## States & Interactions

### 1. Initial Load
```
[Page Loads] → [Bubble Appears] → [User sees 💬]
```

### 2. Opening Chat
```
[User Clicks Bubble] → [Window Slides Up] → [Bubble Changes Color]
                     → [Welcome Message Visible]
                     → [Input Focused]
```

### 3. Sending Message
```
[User Types] → [Hits Enter/Clicks ➤] → [Message Appears (User)]
                                     → [Input Clears]
                                     → [Loading Dots Appear]
                                     → [Scroll to Bottom]
```

### 4. Receiving Response
```
[API Returns] → [Loading Dots Remove] → [Bot Message Appears]
             → [Scroll to Bottom]
             → [Check for "Proposed Article"]
             → [Show "Save Article" Button if detected]
```

### 5. Closing Chat
```
[User Clicks ×] → [Window Slides Down] → [Bubble Returns to Default Color]
                → [Conversation Preserved in Memory]
```

## Responsive Behavior

### Desktop (> 768px)
```
Chat Window:
  Width: 380px
  Height: 550px
  Position: Fixed bottom-right
  Bottom: 90px
  Right: 20px
```

### Mobile (< 768px)
```
Chat Window:
  Width: calc(100vw - 20px)
  Height: calc(100vh - 100px)
  Position: Fixed bottom-right
  Bottom: 80px
  Right: 10px
  
Adjustments:
  - Larger input area
  - Bigger touch targets
  - Full-width messages
```

## Message Types

### 1. Bot Welcome Message
```
┌────────────────────────────────────────┐
│ 🤖  Hi! I'm your support assistant.   │
│                                        │
│     I can help you with:               │
│     • How to use the bug tracker       │
│     • Creating and managing bugs       │
│     • Features and workflows           │
│     • Finding documentation            │
│                                        │
│     What can I help you with today?    │
└────────────────────────────────────────┘
```

### 2. User Message
```
                    ┌────────────────────┐
                    │ How do I create    │
                    │ a bug report?   👤 │
                    └────────────────────┘
```

### 3. Bot Response with Markdown
```
┌────────────────────────────────────────┐
│ 🤖  To create a bug report:            │
│                                        │
│     **Steps:**                         │
│     1. Click "Create Bug"              │
│     2. Fill in:                        │
│        • Title                         │
│        • Description                   │
│        • Severity                      │
│     3. Click "Submit"                  │
│                                        │
│     See: [Getting Started](link)       │
└────────────────────────────────────────┘
```

### 4. Bot Response with Proposed Article
```
┌────────────────────────────────────────┐
│ 🤖  To create a bug report...          │
│                                        │
│     [response text here]               │
│                                        │
│     ┌────────────────────────────┐    │
│     │ 💡 Save as help article?   │    │
│     │         [Save Article]     │    │
│     └────────────────────────────┘    │
└────────────────────────────────────────┘
```

### 5. Loading State
```
┌────────────────────────────────────────┐
│ 🤖  ● ● ●                              │
└────────────────────────────────────────┘
```

### 6. Success Message
```
┌────────────────────────────────────────┐
│ 🤖  ✅ Great! I've saved the help      │
│     article "Creating Bugs".           │
│                                        │
│     You can find it at:                │
│     help_articles/creating-bugs.md     │
└────────────────────────────────────────┘
```

## Typography

```
Font Family: System default (inherits from app)
  - Sans-serif stack

Font Sizes:
  - Chat Header: 18px (bold)
  - Message Content: 14px
  - Input Text: 14px
  - Button Text: 12px
  - Code Blocks: 13px

Line Heights:
  - Body Text: 1.5
  - Headers: 1.2

Font Weights:
  - Headers: 600 (semibold)
  - Normal: 400
  - Bold: 700
```

## Accessibility Features

- **ARIA Labels**: All interactive elements labeled
- **Keyboard Navigation**: Tab through elements
- **Enter Key**: Send message
- **Escape Key**: Close chat (can be added)
- **Focus Indicators**: Clear visual focus states
- **Color Contrast**: WCAG AA compliant
- **Screen Reader**: Semantic HTML structure

## Browser Compatibility

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+
✅ Mobile Safari (iOS 14+)
✅ Chrome Mobile (Android 10+)

CSS Features Used:
- Flexbox
- CSS Grid
- Gradients
- Animations
- Custom properties (can be added)
- Border-radius

## Implementation Details

```css
/* Key CSS Classes */
.support-chat-bubble      /* The circular button */
.support-chat-window      /* The chat panel */
.chat-header              /* Purple header bar */
.chat-messages            /* Scrollable message area */
.chat-message             /* Individual message wrapper */
.message-avatar           /* Emoji avatars */
.message-content          /* Message text bubble */
.chat-input-area          /* Input section */
.chat-input               /* Text input field */
.chat-send-btn            /* Send button */
```

```javascript
// Key JavaScript Class
class SupportChat {
    constructor()        // Initialize
    createChatWidget()   // Build HTML
    toggleChat()         // Open/close
    sendMessage()        // Handle send
    addMessage()         // Display message
    showLoading()        // Show dots
    hideLoading()        // Remove dots
    formatMarkdown()     // Parse markdown
}
```

This visual reference helps you understand what the chat widget looks like and how it behaves!
