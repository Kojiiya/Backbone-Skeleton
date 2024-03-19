// Open/Close Sidebar Popup
const sidebarPopup = document.getElementById('sidebar-popup');
const openSidebarBtn = document.getElementById('open-sidebar');

openSidebarBtn.addEventListener('click', () => {
  sidebarPopup.classList.toggle('open');
});

// Chatbox Functionality
const chatMessages = document.querySelector('.chat-messages');
const chatInput = document.getElementById('message-input');
const sendMessageBtn = document.getElementById('send-message');

sendMessageBtn.addEventListener('click', () => {
  const message = chatInput.value.trim();
  if (message) {
    addMessageToChat(message, 'user');
    sendToChatGPT(message);
    chatInput.value = '';
  }
});

function addMessageToChat(message, sender) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('chat-message', sender);
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendToChatGPT(message) {
  fetch('/generate_chat_response', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt: message })
  })
  .then(response => response.json())
  .then(data => {
      if ('answer' in data) {
          const responseMessage = data.answer;
          addMessageToChat(responseMessage, 'bot');
      } else {
          const errorMessage = "Failed to get response from ChatGPT";
          addMessageToChat(errorMessage, 'error');
          console.error(errorMessage);
      }
  })
  .catch(error => {
      const errorMessage = "Error communicating with ChatGPT: " + error.message;
      addMessageToChat(errorMessage, 'error');
      console.error(errorMessage);
  });
}
