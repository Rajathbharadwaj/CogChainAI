import React from 'react';

const MessageList = ({ messages }) => {
  return (
    <div>
      {messages.map((message, index) => (
        <div key={index}>
          <strong>{message.role === 'system' ? 'System' : 'You'}:</strong> {message.content}
        </div>
      ))}
    </div>
  );
};

export default MessageList;
