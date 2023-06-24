import React from 'react';
import Message from './Message';

const MessageList = ({ messages }) => (
  <div>
    {messages.map((message, index) => (
      <Message key={index} message={message} />
    ))}
  </div>
);

export default MessageList;
