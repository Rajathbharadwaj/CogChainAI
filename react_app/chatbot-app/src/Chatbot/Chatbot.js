import React, { useState } from 'react';
import MessageList from './MessageList';
import InputForm from './InputForm';
import { callChatAPI } from './chatAPI';
import { SystemChatMessage } from 'langchain/schema';

const systemMessage = new SystemChatMessage(
  "You are a companion to the user help them with their daily tasks."
);

const Chatbot = () => {
  const [messages, setMessages] = useState([systemMessage]);

  const handleUserInput = async (userInput) => {
    const humanMessage = { text: userInput };

    // Call the chat API and get the response
    const response = await callChatAPI([...messages, humanMessage]);

    // Assuming the response contains the chatbot's message in a 'text' property
    const chatbotMessage = { text: response.text || 'API response error' };

    // Update the messages state
    const newMessages = [...messages, humanMessage, chatbotMessage];
    setMessages(newMessages);
    
  };

  return (
    <div>
      <MessageList messages={messages} />
      <InputForm onSubmit={handleUserInput} />
    </div>
  );
};

export default Chatbot;
