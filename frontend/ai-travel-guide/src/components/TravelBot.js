import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([]); // Store chat history
  const [userInput, setUserInput] = useState(""); // Store user input
  const [loading, setLoading] = useState(false); // Loading state

  // Handle user input submission
  const sendMessage = async () => {
    if (!userInput.trim()) return;

    // Append user message to chat history
    const newMessages = [...messages, { role: "user", content: userInput }];
    setMessages(newMessages);
    setUserInput("");
    setLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/chatbot/", {
        prompt: userInput,
      });

      // Append chatbot response to chat history
      setMessages([...newMessages, { role: "bot", content: response.data.response }]);
    } catch (error) {
      console.error("Error:", error);
      setMessages([...newMessages, { role: "bot", content: "Error: Unable to fetch response." }]);
    }

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-header">AI Travel Chatbot ✈️</div>
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.role}`}>
            <strong>{msg.role === "user" ? "You" : "Bot"}:</strong> {msg.content}
          </div>
        ))}
        {loading && <div className="chat-message bot">Bot: Typing...</div>}
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask me anything..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
