import React from 'react';

const MessageList = ({ messages }) => {
  return (
    <div>
      {messages.map((message, index) => {
        // Assuming the first message is from the system, the rest are from the user
        const role = index%2 === 0 ? 'system' : 'user';

        // Log each message for debugging
        console.log('Rendering message:', message);

        return (
          <div key={index}>
            <strong>{role === 'system' ? 'System' : 'You'}:</strong> {message.text}
          </div>
        );
      })}
    </div>
  );
};

export default MessageList;
