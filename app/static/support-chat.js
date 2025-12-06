/**
 * Support Chat Widget
 * Handles the chat UI and communication with the backend support API
 */

class SupportChat {
    constructor() {
        this.isOpen = false;
        this.conversationHistory = [];
        this.isLoading = false;

        this.init();
    }

    init() {
        // Create chat widget HTML
        this.createChatWidget();

        // Bind event listeners
        this.bindEvents();
    }

    createChatWidget() {
        const chatHTML = `
            <!-- Chat Bubble Button -->
            <button class="support-chat-bubble" id="chatBubble" aria-label="Open support chat">
                💬
            </button>
            
            <!-- Chat Window -->
            <div class="support-chat-window" id="chatWindow">
                <div class="chat-header">
                    <h3>Support Assistant</h3>
                    <button class="chat-close" id="chatClose" aria-label="Close chat">×</button>
                </div>
                
                <div class="chat-messages" id="chatMessages">
                    <div class="chat-message bot">
                        <div class="message-avatar bot">🤖</div>
                        <div class="message-content">
                            <p>Hi! I'm your support assistant. I can help you with:</p>
                            <ul>
                                <li>How to use the bug tracker</li>
                                <li>Creating and managing bug reports</li>
                                <li>Understanding features and workflows</li>
                                <li>Finding documentation</li>
                            </ul>
                            <p>What can I help you with today?</p>
                        </div>
                    </div>
                </div>
                
                <div class="chat-input-area">
                    <input 
                        type="text" 
                        class="chat-input" 
                        id="chatInput" 
                        placeholder="Type your message..."
                        aria-label="Chat message input"
                    />
                    <button class="chat-send-btn" id="chatSend" aria-label="Send message">
                        ➤
                    </button>
                </div>
            </div>
        `;

        // Append to body
        document.body.insertAdjacentHTML('beforeend', chatHTML);

        // Cache DOM elements
        this.elements = {
            bubble: document.getElementById('chatBubble'),
            window: document.getElementById('chatWindow'),
            close: document.getElementById('chatClose'),
            messages: document.getElementById('chatMessages'),
            input: document.getElementById('chatInput'),
            sendBtn: document.getElementById('chatSend')
        };
    }

    bindEvents() {
        // Toggle chat window
        this.elements.bubble.addEventListener('click', () => this.toggleChat());
        this.elements.close.addEventListener('click', () => this.toggleChat());

        // Send message on button click
        this.elements.sendBtn.addEventListener('click', () => this.sendMessage());

        // Send message on Enter key
        this.elements.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !this.isLoading) {
                this.sendMessage();
            }
        });
    }

    toggleChat() {
        this.isOpen = !this.isOpen;

        if (this.isOpen) {
            this.elements.window.classList.add('open');
            this.elements.bubble.classList.add('active');
            this.elements.input.focus();
        } else {
            this.elements.window.classList.remove('open');
            this.elements.bubble.classList.remove('active');
        }
    }

    async sendMessage() {
        const message = this.elements.input.value.trim();

        if (!message || this.isLoading) {
            return;
        }

        // Clear input
        this.elements.input.value = '';

        // Add user message to UI
        this.addMessage(message, 'user');

        // Add to conversation history
        this.conversationHistory.push({
            role: 'user',
            content: message
        });

        // Show loading indicator
        this.showLoading();

        try {
            // Call backend API
            const response = await fetch('/api/support/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    conversation: this.conversationHistory
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Remove loading indicator
            this.hideLoading();

            // Add bot response to UI
            this.addMessage(data.reply, 'bot');

            // Add to conversation history
            this.conversationHistory.push({
                role: 'assistant',
                content: data.reply
            });

            // Check if response contains a proposed article
            this.checkForProposedArticle(data.reply);

        } catch (error) {
            console.error('Error sending message:', error);
            this.hideLoading();
            this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }
    }

    addMessage(content, type = 'bot') {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${type}`;

        const avatar = type === 'bot' ? '🤖' : '👤';
        const avatarClass = type === 'bot' ? 'bot' : 'user';

        // Parse markdown-like content for bot messages
        const formattedContent = type === 'bot' ? this.formatMarkdown(content) : this.escapeHtml(content);

        messageDiv.innerHTML = `
            <div class="message-avatar ${avatarClass}">${avatar}</div>
            <div class="message-content">${formattedContent}</div>
        `;

        this.elements.messages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    showLoading() {
        this.isLoading = true;
        this.elements.sendBtn.disabled = true;

        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'chat-message bot';
        loadingDiv.id = 'loadingMessage';
        loadingDiv.innerHTML = `
            <div class="message-avatar bot">🤖</div>
            <div class="message-content message-loading">
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
                <div class="loading-dot"></div>
            </div>
        `;

        this.elements.messages.appendChild(loadingDiv);
        this.scrollToBottom();
    }

    hideLoading() {
        this.isLoading = false;
        this.elements.sendBtn.disabled = false;

        const loadingMsg = document.getElementById('loadingMessage');
        if (loadingMsg) {
            loadingMsg.remove();
        }
    }

    scrollToBottom() {
        this.elements.messages.scrollTop = this.elements.messages.scrollHeight;
    }

    checkForProposedArticle(content) {
        // Detect the new structured format: === PROPOSED_HELP_ARTICLE ===
        if (content.includes('=== PROPOSED_HELP_ARTICLE ===')) {

            // Extract the article block
            const startMarker = '=== PROPOSED_HELP_ARTICLE ===';
            const endMarker = '=== END_PROPOSED_HELP_ARTICLE ===';

            const startIdx = content.indexOf(startMarker);
            const endIdx = content.indexOf(endMarker);

            if (startIdx !== -1 && endIdx !== -1) {
                const articleBlock = content.substring(startIdx + startMarker.length, endIdx).trim();

                // Extract title from the article block
                const titleMatch = articleBlock.match(/Title:\s*(.+)/);
                const topic = titleMatch ? titleMatch[1].trim() : 'Help Article';

                this.showSaveArticleOption(topic);
            }
        }
        // Fallback to old format for backwards compatibility
        else if (content.includes('**Proposed Help Article:**') ||
            content.includes('**Proposed Article:**')) {

            const lines = content.split('\n');
            let topic = 'Help Article';

            for (let i = 0; i < lines.length; i++) {
                if (lines[i].includes('**Proposed') && i + 1 < lines.length) {
                    topic = lines[i + 1].replace(/[#*[\]]/g, '').trim();
                    break;
                }
            }

            this.showSaveArticleOption(topic);
        }
    }

    showSaveArticleOption(topic) {
        const lastMessage = this.elements.messages.lastElementChild;
        const messageContent = lastMessage.querySelector('.message-content');

        const articleDiv = document.createElement('div');
        articleDiv.className = 'proposed-article';
        articleDiv.innerHTML = `
            <div class="proposed-article-header">
                <span class="proposed-article-title">💡 Save this as a help article?</span>
                <button class="save-article-btn" data-topic="${this.escapeHtml(topic)}">
                    Save Article
                </button>
            </div>
        `;

        messageContent.appendChild(articleDiv);

        // Add click handler for save button
        const saveBtn = articleDiv.querySelector('.save-article-btn');
        saveBtn.addEventListener('click', () => this.saveArticle(topic));
    }

    async saveArticle(topic) {
        try {
            const response = await fetch('/api/support/generate-article', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    topic: topic,
                    conversation: this.conversationHistory
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            if (data.success) {
                this.addMessage(
                    `✅ Great! I've saved the help article "${data.title}". You can find it at: ${data.article_path}`,
                    'bot'
                );
            } else {
                this.addMessage('Sorry, I couldn\'t save the article. Please try again.', 'bot');
            }

        } catch (error) {
            console.error('Error saving article:', error);
            this.addMessage('Sorry, I encountered an error saving the article.', 'bot');
        }
    }

    formatMarkdown(text) {
        // Simple markdown-like formatting (basic implementation)
        let formatted = this.escapeHtml(text);

        // Bold: **text**
        formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

        // Italic: *text*
        formatted = formatted.replace(/\*(.+?)\*/g, '<em>$1</em>');

        // Code: `code`
        formatted = formatted.replace(/`(.+?)`/g, '<code>$1</code>');

        // Line breaks
        formatted = formatted.replace(/\n/g, '<br>');

        // Lists (simple detection)
        formatted = formatted.replace(/^- (.+?)(<br>|$)/gm, '<li>$1</li>');
        formatted = formatted.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

        return formatted;
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize chat widget when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new SupportChat();
    });
} else {
    new SupportChat();
}
