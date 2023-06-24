import React from 'react';

const Message = ({ message }) => (
  <div>
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
);

export default Message;
