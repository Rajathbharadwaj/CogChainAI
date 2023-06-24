import { ChatOpenAI } from "langchain/chat_models/openai";
import { HumanChatMessage, SystemChatMessage } from "langchain/schema";
import { config } from 'dotenv';
import readline from 'readline';

// Load environment variables
config();

// Initialize ChatOpenAI
const chat = new ChatOpenAI({ temperature: 0.7 });

// Create a readline interface for console input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// Predefined context
const systemMessage = new SystemChatMessage("You are a companion to the user who wants to commit to doing somethig. It will be discussed in the next message with the user. You should provide a plan for the user to follow and take the reports from the user on the progress. You should also provide the user with the motivation to continue. In the review, you should add text 'performance:{good/bad}' to the message. Also, focus that the user should not be distracted from the goal. and is not lying about the progress. User will report with 'Update: {text}'");
// Function to get user input and get AI response
const converseWithAI = async (previousMessages = [systemMessage]) => {
    rl.question('You: ', async (userInput) => {
        if (userInput.toLowerCase() === 'exit') {
            rl.close();
            return;
        }

        try {
            // Add the user's message to the previous messages
            previousMessages.push(new HumanChatMessage(userInput));

            // Send messages to chat model and get AI response
            const response = await chat.call(previousMessages);
            console.log('AI:', response.text);

            // Add the AI's response to the previous messages
            previousMessages.push(response);

            // Continue the conversation
            converseWithAI(previousMessages);
        } catch (error) {
            console.error(error);
        }
    });
};

// Start the conversation
converseWithAI();
