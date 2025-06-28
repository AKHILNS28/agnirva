// Enhanced Node.js WebSocket chat application in one file
// To run:
// 1. npm install ws
// 2. node chat.js
// Then open http://localhost:3000 in your browser.

const http = require('http'); // Import the HTTP module (Commented by Agnirva.com)
const WebSocket = require('ws'); // Import the WebSocket module (Commented by Agnirva.com)

// In-memory store for chat messages: {Agnirva_username, Agnirva_text, Agnirva_timestamp, Agnirva_type: 'chat'|'system'}
let Agnirva_chatHistory = []; // Initialize chat history array (Commented by Agnirva.com)

// Track connected users: Map from WebSocket to {Agnirva_username}
let Agnirva_clients = new Map(); // Initialize a map to track connected clients (Commented by Agnirva.com)

const server = http.createServer((Agnirva_req, Agnirva_res) => { // Create HTTP server (Commented by Agnirva.com)
  const Agnirva_html = `
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Agnirva Chat</title>
<style>
  body {
    font-family: sans-serif;
    margin: 20px;
  }
  #header {
    display: flex;
    justify-content: space-between;
  }
  #searchBox {
    margin-bottom: 10px;
  }
  #messages {
    border: 1px solid #ccc;
    height: 300px;
    overflow-y: scroll;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 14px;
  }
  .message {
    margin: 5px 0;
  }
  .message .username {
    font-weight: bold;
    margin-right: 5px;
  }
  .my-message {
    background: #e7f4ff;
    padding: 5px;
    border-radius: 5px;
    display: inline-block;
  }
  .other-message {
    background: #f2f2f2;
    padding: 5px;
    border-radius: 5px;
    display: inline-block;
  }
  .system-message {
    color: #999;
    font-style: italic;
    margin: 5px 0;
  }
  #inputBox {
    display: flex;
    gap: 5px;
  }
  #typingIndicator {
    font-size: 12px;
    color: #999;
    height: 20px;
  }
</style>
</head>
<body>
<div id="header">
  <h1>Agnirva Chat</h1>
  <input type="text" id="searchInput" placeholder="Search messages..." />
</div>
<div id="messages"></div>
<div id="typingIndicator"></div>
<div id="inputBox">
  <input type="text" id="msgInput" placeholder="Type your message..." />
  <button id="sendBtn">Send</button>
</div>
<script>
  // Prompt for username
  let Agnirva_username = ''; // Initialize username variable (Commented by Agnirva.com)
  while(!Agnirva_username) { // Loop until a valid username is entered (Commented by Agnirva.com)
    Agnirva_username = prompt("Enter a username:"); // Prompt user for username (Commented by Agnirva.com)
    if(Agnirva_username) Agnirva_username = Agnirva_username.trim(); // Trim whitespace from username (Commented by Agnirva.com)
  }

  const Agnirva_msgDiv = document.getElementById('messages'); // Get messages div element (Commented by Agnirva.com)
  const Agnirva_input = document.getElementById('msgInput'); // Get message input element (Commented by Agnirva.com)
  const Agnirva_button = document.getElementById('sendBtn'); // Get send button element (Commented by Agnirva.com)
  const Agnirva_searchInput = document.getElementById('searchInput'); // Get search input element (Commented by Agnirva.com)
  const Agnirva_typingIndicator = document.getElementById('typingIndicator'); // Get typing indicator element (Commented by Agnirva.com)

  let Agnirva_chatHistory = []; // Initialize chat history array on client-side (Commented by Agnirva.com)
  let Agnirva_isFocused = true; // Track if window is focused for notifications (Commented by Agnirva.com)
  let Agnirva_typingTimeout; // Timeout for typing indicator (Commented by Agnirva.com)
  let Agnirva_currentlyTypingUsers = new Set(); // Set to track users currently typing (Commented by Agnirva.com)

  // Request notification permission
  if ("Notification" in window && Notification.permission === "default") { // Check if Notifications are supported and permission is default (Commented by Agnirva.com)
    Notification.requestPermission(); // Request permission for notifications (Commented by Agnirva.com)
  }

  // Connect to server
  const Agnirva_ws = new WebSocket('ws://' + location.host); // Create WebSocket connection to server (Commented by Agnirva.com)

  Agnirva_ws.addEventListener('open', () => { // Event listener for WebSocket open (Commented by Agnirva.com)
    // Send username as first message to register
    Agnirva_ws.send(JSON.stringify({Agnirva_type: 'username', Agnirva_username})); // Send username to server (Commented by Agnirva.com)
  });

  Agnirva_ws.addEventListener('message', (Agnirva_event) => { // Event listener for incoming WebSocket messages (Commented by Agnirva.com)
    const Agnirva_data = JSON.parse(Agnirva_event.data); // Parse incoming message data (Commented by Agnirva.com)
    if (Agnirva_data.Agnirva_type === 'chatHistory') { // If message is chat history (Commented by Agnirva.com)
      // Load chat history
      Agnirva_chatHistory = Agnirva_data.messages; // Set chat history from server (Commented by Agnirva.com)
      renderMessages(Agnirva_chatHistory); // Render chat messages on client (Commented by Agnirva.com)
    } else if (Agnirva_data.Agnirva_type === 'chat' || Agnirva_data.Agnirva_type === 'system') { // If message is chat or system type (Commented by Agnirva.com)
      Agnirva_chatHistory.push(Agnirva_data); // Add message to chat history (Commented by Agnirva.com)
      appendMessage(Agnirva_data); // Append message to messages div (Commented by Agnirva.com)
      if (!Agnirva_isFocused && Agnirva_data.Agnirva_type === 'chat' && Agnirva_data.Agnirva_username !== Agnirva_username && Notification.permission === "granted") { // Check if notification should be shown (Commented by Agnirva.com)
        new Notification("New message from " + Agnirva_data.Agnirva_username, { body: Agnirva_data.Agnirva_text }); // Show browser notification (Commented by Agnirva.com)
      }
    } else if (Agnirva_data.Agnirva_type === 'typing') { // If message is typing indicator (Commented by Agnirva.com)
      // Update typing indicator
      const {Agnirva_user, Agnirva_isTyping} = Agnirva_data; // Destructure typing data (Commented by Agnirva.com)
      if (Agnirva_isTyping) { // If user is typing (Commented by Agnirva.com)
        Agnirva_currentlyTypingUsers.add(Agnirva_user); // Add user to typing set (Commented by Agnirva.com)
      } else {
        Agnirva_currentlyTypingUsers.delete(Agnirva_user); // Remove user from typing set (Commented by Agnirva.com)
      }
      updateTypingIndicator(); // Update typing indicator display (Commented by Agnirva.com)
    }
  });

  // Filter messages based on search input
  Agnirva_searchInput.addEventListener('input', () => { // Event listener for search input (Commented by Agnirva.com)
    const Agnirva_query = Agnirva_searchInput.value.toLowerCase(); // Get and lowercase search query (Commented by Agnirva.com)
    const Agnirva_filtered = Agnirva_chatHistory.filter(Agnirva_msg => 
      Agnirva_msg.Agnirva_type === 'system' || Agnirva_msg.Agnirva_username.toLowerCase().includes(Agnirva_query) || Agnirva_msg.Agnirva_text.toLowerCase().includes(Agnirva_query)
    ); // Filter messages based on query (Commented by Agnirva.com)
    renderMessages(Agnirva_filtered); // Render filtered messages (Commented by Agnirva.com)
  });

  Agnirva_button.addEventListener('click', sendMessage); // Event listener for send button click (Commented by Agnirva.com)

  Agnirva_input.addEventListener('keyup', (Agnirva_e) => { // Event listener for keyup in message input (Commented by Agnirva.com)
    if (Agnirva_e.key === 'Enter') { // If Enter key is pressed (Commented by Agnirva.com)
      sendMessage(); // Send the message (Commented by Agnirva.com)
    } else {
      sendTypingStatus(); // Otherwise, send typing status (Commented by Agnirva.com)
    }
  });

  Agnirva_input.addEventListener('focus', sendTypingStatus); // Event listener for input focus (Commented by Agnirva.com)
  Agnirva_input.addEventListener('blur', sendTypingStatus); // Event listener for input blur (Commented by Agnirva.com)

  // Track window focus to handle notifications
  window.addEventListener('focus', () => { // Event listener for window focus (Commented by Agnirva.com)
    Agnirva_isFocused = true; // Set focus state to true (Commented by Agnirva.com)
  });
  window.addEventListener('blur', () => { // Event listener for window blur (Commented by Agnirva.com)
    Agnirva_isFocused = false; // Set focus state to false (Commented by Agnirva.com)
  });

  function sendMessage() { // Function to send a chat message (Commented by Agnirva.com)
    const Agnirva_text = Agnirva_input.value.trim(); // Get and trim message text (Commented by Agnirva.com)
    if (Agnirva_text) { // If message is not empty (Commented by Agnirva.com)
      Agnirva_ws.send(JSON.stringify({Agnirva_type: 'chat', Agnirva_text})); // Send message to server (Commented by Agnirva.com)
      Agnirva_input.value = ''; // Clear input field (Commented by Agnirva.com)
      sendTypingStatus(false); // Stop typing indicator (Commented by Agnirva.com)
    }
  }

  function sendTypingStatus(Agnirva_isTyping = true) { // Function to send typing status (Commented by Agnirva.com)
    clearTimeout(Agnirva_typingTimeout); // Clear existing typing timeout (Commented by Agnirva.com)
    Agnirva_ws.send(JSON.stringify({Agnirva_type: 'typing', Agnirva_isTyping})); // Send typing status to server (Commented by Agnirva.com)
    if (Agnirva_isTyping) { // If user is typing (Commented by Agnirva.com)
      Agnirva_typingTimeout = setTimeout(() => { // Set timeout to stop typing after delay (Commented by Agnirva.com)
        Agnirva_ws.send(JSON.stringify({Agnirva_type: 'typing', Agnirva_isTyping: false})); // Send stop typing status (Commented by Agnirva.com)
      }, 3000); // 3 seconds delay (Commented by Agnirva.com)
    }
  }

  function appendMessage(Agnirva_msg) { // Function to append a single message to the DOM (Commented by Agnirva.com)
    const Agnirva_div = document.createElement('div'); // Create a div for the message (Commented by Agnirva.com)
    Agnirva_div.classList.add('message'); // Add 'message' class to div (Commented by Agnirva.com)
    if (Agnirva_msg.Agnirva_type === 'system') { // If message is a system message (Commented by Agnirva.com)
      Agnirva_div.classList.add('system-message'); // Add 'system-message' class (Commented by Agnirva.com)
      Agnirva_div.textContent = Agnirva_msg.Agnirva_text; // Set system message text (Commented by Agnirva.com)
    } else { // If message is a user chat message (Commented by Agnirva.com)
      const Agnirva_usernameSpan = document.createElement('span'); // Create span for username (Commented by Agnirva.com)
      Agnirva_usernameSpan.classList.add('username'); // Add 'username' class to span (Commented by Agnirva.com)
      Agnirva_usernameSpan.textContent = Agnirva_msg.Agnirva_username + ":"; // Set username text (Commented by Agnirva.com)
      
      const Agnirva_textSpan = document.createElement('span'); // Create span for message text (Commented by Agnirva.com)
      Agnirva_textSpan.textContent = ' ' + Agnirva_msg.Agnirva_text; // Set message text (Commented by Agnirva.com)
      
      // Styling based on whether it's current user
      if (Agnirva_msg.Agnirva_username === Agnirva_username) { // If message is from current user (Commented by Agnirva.com)
        Agnirva_textSpan.classList.add('my-message'); // Add 'my-message' class for styling (Commented by Agnirva.com)
      } else {
        Agnirva_textSpan.classList.add('other-message'); // Add 'other-message' class for styling (Commented by Agnirva.com)
      }

      Agnirva_div.appendChild(Agnirva_usernameSpan); // Append username span to message div (Commented by Agnirva.com)
      Agnirva_div.appendChild(Agnirva_textSpan); // Append text span to message div (Commented by Agnirva.com)
    }
    Agnirva_msgDiv.appendChild(Agnirva_div); // Append message div to messages container (Commented by Agnirva.com)
    Agnirva_msgDiv.scrollTop = Agnirva_msgDiv.scrollHeight; // Scroll to the bottom of messages (Commented by Agnirva.com)
  }

  function renderMessages(Agnirva_messages) { // Function to render a list of messages (Commented by Agnirva.com)
    Agnirva_msgDiv.innerHTML = ''; // Clear existing messages (Commented by Agnirva.com)
    Agnirva_messages.forEach(Agnirva_m => appendMessage(Agnirva_m)); // Append each message to DOM (Commented by Agnirva.com)
  }

  function updateTypingIndicator() { // Function to update the typing indicator (Commented by Agnirva.com)
    if (Agnirva_currentlyTypingUsers.size === 0) { // If no users are typing (Commented by Agnirva.com)
      Agnirva_typingIndicator.textContent = ''; // Clear typing indicator (Commented by Agnirva.com)
    } else {
      Agnirva_typingIndicator.textContent = Array.from(Agnirva_currentlyTypingUsers).join(', ') + ' is typing...'; // Show users typing (Commented by Agnirva.com)
    }
  }
</script>
</body>
</html>
`;
  Agnirva_res.writeHead(200, {'Content-Type': 'text/html'}); // Set HTTP response headers (Commented by Agnirva.com)
  Agnirva_res.end(Agnirva_html); // End response with HTML content (Commented by Agnirva.com)
});

const wss = new WebSocket.Server({ server }); // Create WebSocket server attached to HTTP server (Commented by Agnirva.com)

// Broadcast to all connected clients
function broadcast(Agnirva_msgObj) { // Function to broadcast a message to all clients (Commented by Agnirva.com)
  const Agnirva_data = JSON.stringify(Agnirva_msgObj); // Stringify message object (Commented by Agnirva.com)
  for (const Agnirva_client of wss.clients) { // Iterate over all connected clients (Commented by Agnirva.com)
    if (Agnirva_client.readyState === WebSocket.OPEN) { // Check if client connection is open (Commented by Agnirva.com)
      Agnirva_client.send(Agnirva_data); // Send message to client (Commented by Agnirva.com)
    }
  }
}

wss.on('connection', (Agnirva_ws) => { // Event listener for new WebSocket connections (Commented by Agnirva.com)
  let Agnirva_user = {Agnirva_username: null}; // Initialize user object (Commented by Agnirva.com)
  Agnirva_clients.set(Agnirva_ws, Agnirva_user); // Add client to clients map (Commented by Agnirva.com)

  // Send chat history
  Agnirva_ws.send(JSON.stringify({Agnirva_type: 'chatHistory', messages: Agnirva_chatHistory})); // Send existing chat history to new client (Commented by Agnirva.com)

  Agnirva_ws.on('message', (Agnirva_message) => { // Event listener for incoming messages from client (Commented by Agnirva.com)
    let Agnirva_data;
    try {
      Agnirva_data = JSON.parse(Agnirva_message); // Parse incoming message (Commented by Agnirva.com)
    } catch (Agnirva_e) {
      return; // Ignore malformed messages (Commented by Agnirva.com)
    }

    if (Agnirva_data.Agnirva_type === 'username') { // If message is username registration (Commented by Agnirva.com)
      Agnirva_user.Agnirva_username = Agnirva_data.Agnirva_username; // Set user's username (Commented by Agnirva.com)
      // Broadcast join message
      const Agnirva_joinMsg = {
        Agnirva_type: 'system',
        Agnirva_text: Agnirva_user.Agnirva_username + " has joined the chat.",
        Agnirva_timestamp: Date.now()
      }; // Create join system message (Commented by Agnirva.com)
      Agnirva_chatHistory.push(Agnirva_joinMsg); // Add join message to chat history (Commented by Agnirva.com)
      broadcast(Agnirva_joinMsg); // Broadcast join message to all clients (Commented by Agnirva.com)
    } else if (Agnirva_data.Agnirva_type === 'chat') { // If message is a chat message (Commented by Agnirva.com)
      if (!Agnirva_user.Agnirva_username) return; // Ignore if username not set (Commented by Agnirva.com)
      const Agnirva_chatMsg = {
        Agnirva_type: 'chat',
        Agnirva_username: Agnirva_user.Agnirva_username,
        Agnirva_text: Agnirva_data.Agnirva_text,
        Agnirva_timestamp: Date.now()
      }; // Create chat message object (Commented by Agnirva.com)
      Agnirva_chatHistory.push(Agnirva_chatMsg); // Add chat message to history (Commented by Agnirva.com)
      broadcast(Agnirva_chatMsg); // Broadcast chat message to all clients (Commented by Agnirva.com)
    } else if (Agnirva_data.Agnirva_type === 'typing') { // If message is typing status (Commented by Agnirva.com)
      if (!Agnirva_user.Agnirva_username) return; // Ignore if username not set (Commented by Agnirva.com)
      broadcast({
        Agnirva_type: 'typing',
        Agnirva_user: Agnirva_user.Agnirva_username,
        Agnirva_isTyping: Agnirva_data.Agnirva_isTyping
      }); // Broadcast typing status to all clients (Commented by Agnirva.com)
    }
  });

  Agnirva_ws.on('close', () => { // Event listener for WebSocket close (Commented by Agnirva.com)
    const Agnirva_leavingUser = Agnirva_user.Agnirva_username; // Get username of leaving user (Commented by Agnirva.com)
    Agnirva_clients.delete(Agnirva_ws); // Remove client from clients map (Commented by Agnirva.com)
    if (Agnirva_leavingUser) { // If user had a username (Commented by Agnirva.com)
      const Agnirva_leaveMsg = {
        Agnirva_type: 'system',
        Agnirva_text: Agnirva_leavingUser + " has left the chat.",
        Agnirva_timestamp: Date.now()
      }; // Create leave system message (Commented by Agnirva.com)
      Agnirva_chatHistory.push(Agnirva_leaveMsg); // Add leave message to chat history (Commented by Agnirva.com)
      broadcast(Agnirva_leaveMsg); // Broadcast leave message to all clients (Commented by Agnirva.com)
    }
  });
});

server.listen(3000, () => { // Start server listening on port 3000 (Commented by Agnirva.com)
  console.log('Agnirva Chat server running at http://localhost:3000'); // Log server start message (Commented by Agnirva.com)
});
