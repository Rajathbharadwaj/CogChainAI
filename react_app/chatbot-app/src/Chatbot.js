import React, { useState } from 'react';
import { ChatOpenAI } from 'langchain/chat_models/openai';
import { HumanChatMessage, SystemChatMessage } from 'langchain/schema';

const apiKey = process.env.REACT_APP_OPENAI_API_KEY;
const chat = new ChatOpenAI({ temperature: 0.1, openAIApiKey: apiKey });
const systemMessage = new SystemChatMessage(
    "You are a companion to the user help them with their daily tasks."
);

const Chatbot = () => {
    const [messages, setMessages] = useState([systemMessage]);
    const [userInput, setUserInput] = useState('');

    const handleUserInput = async () => {
        if (userInput.toLowerCase() === 'exit') {
            return;
        }

        try {
            const humanMessage = new HumanChatMessage(userInput);
            const updatedMessages = [...messages, humanMessage];
            const response = await chat.call(updatedMessages);

            console.log(updatedMessages);

            // Append the human message and the chat response in one go
            setMessages(updatedMessages.concat([response]));
        } catch (error) {
            console.error(error);
        }
    };

    const handleInputChange = (event) => {
        setUserInput(event.target.value);
    };

    const handleFormSubmit = (event) => {
        event.preventDefault();
        handleUserInput();
        setUserInput('');
    };

    return (
        <div>
            <div>
                {messages.map((message, index) => (
                    <div key={index}>
                        {message.role === 'system' ? (
                            <p>
                                <strong>System:</strong> {message.content}
                            </p>
                        ) : (
                            <p>
                                <strong>You:</strong> {message.content}
                            </p>
                        )}
                    </div>
                ))}
            </div>
            <form onSubmit={handleFormSubmit}>
                <input
                    type="text"
                    value={userInput}
                    onChange={handleInputChange}
                    placeholder="Type your message..."
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
};

export default Chatbot;
