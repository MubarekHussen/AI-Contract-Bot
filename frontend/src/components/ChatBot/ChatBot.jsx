import React, { useState } from 'react';
import Dropzone from 'react-dropzone';
import axios from 'axios';
import 'tailwindcss/tailwind.css'; // Import Tailwind CSS
import Icon from '@mdi/react';
import { mdiArrowRight } from '@mdi/js';

const ChatMessage = ({ message, isUserQuestion }) => (
    <div className={`flex flex-col ${isUserQuestion ? 'items-start' : 'items-end'}`}>
      <div className={`p-2 rounded ${isUserQuestion ? 'bg-blue-200' : 'bg-green-200'}`}>
        <p className="text-3xl">{message}</p> {/* Add text size class here */}
      </div>
    </div>
);

  const Sidebar = ({ onFileUpload, uploadedFiles, onRemoveFile }) => (
    <div className="pt-96 bg-gray-100">
      <h2 className="text-blue-500 text-4xl">Upload Your File</h2>
      <Dropzone onDrop={(acceptedFiles) => onFileUpload(acceptedFiles)}>
        {({ getRootProps, getInputProps }) => (
          <div {...getRootProps()} className="border border-blue-500 rounded p-3 my-3 flex justify-center items-center h-48">
            <input {...getInputProps()} />
            <p className="text-lg">Drag and drop your files here, or click to browse your device</p>
          </div>
        )}
      </Dropzone>
      <div>
        <h3 className="text-blue-500 text-3xl">Uploaded Files:</h3>
        <ul>
          {uploadedFiles.map((file, index) => (
            <li key={index} className="my-2 flex justify-between items-center">
              {file.name}
              <button className="text-white bg-red-500 px-2 py-1 rounded" onClick={() => onRemoveFile(index)}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );

const ChatBot = () => {
  const [newMessage, setNewMessage] = useState('');
  const [messages, setMessages] = useState([
    {
      message: 'How can I help you today?',
      isUserQuestion: false,
    },
  ]);
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const handleInputChange = (e) => {
    setNewMessage(e.target.value);
  };

  const handleSendMessage = async () => {
    if (newMessage.trim() !== '') {
      const newUserQuestion = {
        message: newMessage,
        isUserQuestion: true,
      };

      const formData = new FormData();
      formData.append('user_question', newMessage);

      uploadedFiles.forEach((file) => {
        formData.append('files', file);
      });

      const chatbotResponse = {
        message: '',
        isUserQuestion: false,
      };

      try {
        const response = await axios.post('http://localhost:5000/api/chat', formData);

        chatbotResponse.message = response.data.response;
      } catch (error) {
        console.error('Error sending message:', error);
      }

      setMessages([...messages, newUserQuestion, chatbotResponse]);
      setNewMessage('');
      setUploadedFiles([]);
    }
  };

  const handleFileUpload = (files) => {
    setUploadedFiles([...uploadedFiles, ...files]);
  };

  const handleRemoveFile = (index) => {
    const updatedFiles = [...uploadedFiles];
    updatedFiles.splice(index, 1);
    setUploadedFiles(updatedFiles);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    handleSendMessage();
  };

  return (
    <div className="flex w-full h-full m-20 pt-16">
      <div className="w-1/3 p-3 bg-gray-100 overflow-auto">
        <Sidebar
          onFileUpload={handleFileUpload}
          uploadedFiles={uploadedFiles}
          onRemoveFile={handleRemoveFile}
        />
      </div>
      <div className="w-2/3 p-3">
        <div>
          {messages.map((msg, index) => (
            <ChatMessage key={index} {...msg} />
          ))}
        </div>
        <form className="fixed bottom-0 w-full bg-gray-100 p-4" onSubmit={handleFormSubmit}>
        <div className="flex h-20 overflow-auto">
            <input
            type="text"
            className="w-1/2 mr-2 p-2 border rounded text-3xl"
            placeholder="Type your question here..."
            value={newMessage}
            onChange={handleInputChange}
            />
            <button className="w-1/7 bg-gray-800 text-white px-4 py-2 rounded text-lg" type="submit">
            <Icon path={mdiArrowRight} size={3} />
            </button>
        </div>
        </form>
      </div>
    </div>
  );
};

export default ChatBot;