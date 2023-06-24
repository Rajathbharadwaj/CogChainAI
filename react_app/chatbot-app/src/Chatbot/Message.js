import React from 'react';

const Message = ({ message }) => (
  <div>
    {message.role === 'system' ? (
      <p>
        <strong>System:</strong> {message.text}
      </p>
    ) : (
      <p>
        <strong>You:</strong> {message.text}
      </p>
    )}
  </div>
);

export default Message;
