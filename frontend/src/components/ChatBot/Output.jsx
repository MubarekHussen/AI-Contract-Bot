import React from 'react';

const Output = ({ messages }) => {
    return (
      <div className='border border-gray-300 rounded p-4 mb-4 h-64 overflow-auto'>
        {messages.map((message, index) => (
          <div key={index} className={`mb-2 ${message.isUser ? 'text-right' : 'text-left'}`}>
            <div className={`bg-blue-100 rounded-md p-2 shadow-md inline-block ${message.isUser ? 'float-right' : 'float-left'}`}>
              <p className='text-sm'>{message.text}</p>
            </div>
          </div>
        ))}
      </div>
    );
};
  
export default Output;