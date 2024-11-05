let sessionId = null;

window.onload = startNewChat; // Automatically starts a new session on page load

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function startNewChat() {
    fetch('/new_session')
        .then(response => response.json())
        .then(data => {
            sessionId = data.session_id;
            document.getElementById('chat-box').innerHTML = '';
        })
        .catch(error => {
            console.error('Error starting new chat:', error);
            alert('Failed to start a new chat session.');
        });
}

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value;
    if (message.trim() === '') return;

    addMessageToChat('user', message);
    userInput.value = '';

    // Show loading indicator
    addMessageToChat('bot', 'Loading...');

    fetch(`/chat/${sessionId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        // Clear loading message
        const lastMessage = document.querySelector('#chat-box .message.bot:last-child');
        if (lastMessage) {
            lastMessage.textContent = '';
        }
        addMessageToChat('bot', data.response || 'Sorry, I could not process your request.');
    })
    .catch(error => {
        console.error('Error fetching chat response:', error);
        addMessageToChat('bot', 'An error occurred. Please try again.');
    });
}

function addMessageToChat(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    const messageText = document.createElement('div');
    messageText.classList.add('message-text');
    messageText.textContent = message;
    messageElement.appendChild(messageText);
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function uploadPDF() {
    const form = document.getElementById('upload-form');
    const formData = new FormData(form);

    fetch('/upload_pdf', {  // Ensure the correct endpoint for PDF upload
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.text();
    })
    .then(data => {
        alert('PDF uploaded successfully!');
    })
    .catch(error => {
        console.error('Error uploading PDF:', error);
        alert('Failed to upload PDF.');
    });
}
