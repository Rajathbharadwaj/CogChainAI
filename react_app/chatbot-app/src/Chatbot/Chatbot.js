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
        if (userInput.toLowerCase() === 'exit') {
          return;
        }
      
        try {
          const humanMessage = { role: 'user', content: userInput };
          
          // Call the chat API and get the response
          const response = await callChatAPI([...messages, humanMessage]);
          
          // Assuming the response has the chatbot's message in the 'content' property
          const chatbotMessage = { role: 'system', content: response.content };
      
          // Use functional form of setMessages to avoid stale state
          setMessages(prevMessages => [...prevMessages, humanMessage, chatbotMessage]);
        } catch (error) {
          console.error(error);
        }
      };
      

    return (
        <div>
            <MessageList messages={messages} />
            <InputForm onSubmit={handleUserInput} />
        </div>
    );
};

export default Chatbot;
