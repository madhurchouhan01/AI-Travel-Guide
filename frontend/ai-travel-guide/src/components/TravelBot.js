import React, { useState } from "react";
import ReactMarkdown from "react-markdown"; // Import markdown renderer
import axios from "axios";
import "./TravelBot.css";

const TravelBot = () => {
  const [messages, setMessages] = useState([]); // Chat history
  const [userInput, setUserInput] = useState(""); // User input
  const [loading, setLoading] = useState(false); // Loading state
  const [isOpen, setIsOpen] = useState(false); // Chatbot visibility state

  // Toggle chatbot visibility
  const toggleChatbot = () => {
    setIsOpen(!isOpen);
  };

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

      // Append chatbot response (formatted Markdown) to chat history
      setMessages([...newMessages, { role: "bot", content: response.data.response }]);
    } catch (error) {
      console.error("Error:", error);
      setMessages([...newMessages, { role: "bot", content: "⚠️ Error: Unable to fetch response." }]);
    }

    setLoading(false);
  };

  return (
    <div>
      {/* Floating Chat Button */}
      <button className="chatbot-button" onClick={toggleChatbot}>
        💬 Chat
      </button>

      {/* Chatbot Window */}
      <div className={`chat-container ${isOpen ? "open" : "closed"}`}>
        <div className="chat-header">
          <span>Travel Buddy</span>
          <button className="close-btn" onClick={toggleChatbot}>✖</button>
        </div>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <div key={index} className={`chat-message ${msg.role}`}>

              <ReactMarkdown>{msg.content.text || msg.content}</ReactMarkdown>
            </div>
          ))}
          {loading && <div className="chat-message bot">🤖 Typing...</div>}
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
    </div>
  );
};

export default TravelBot;
