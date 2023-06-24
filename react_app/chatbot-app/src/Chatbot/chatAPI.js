import { ChatOpenAI } from 'langchain/chat_models/openai';
import { HumanChatMessage } from 'langchain/schema';

const apiKey = process.env.REACT_APP_OPENAI_API_KEY;
const chat = new ChatOpenAI({ temperature: 0.1, openAIApiKey: apiKey });

export const callChatAPI = async (messages) => {
    try {
      const response = await chat.call(messages);
      // Make sure to return the response object
      return response;
    } catch (error) {
      console.error(error);
      return null; // return null in case of an error
    }
  };
  
