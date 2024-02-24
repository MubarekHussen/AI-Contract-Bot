import React, { useState } from 'react';
import Dropzone from 'react-dropzone';
import axios from 'axios';
import 'tailwindcss/tailwind.css';
import Icon from '@mdi/react';
import { mdiArrowRight } from '@mdi/js';

const ChatMessage = ({ message, isUserQuestion }) => (
  <div className={`flex flex-col ${isUserQuestion ? 'items-end' : 'items-start'} mb-4`}>
    <div className={`pt-6 pb-8 pl-12 pr-2 rounded ${isUserQuestion ? 'bg-blue-50 w-8/12 text-right pr-14' : 'bg-purple-50 w-10/12'}`}>
      <p className="text-2xl">{message}</p>
    </div>
  </div>
);

const Sidebar = ({ onFileUpload, uploadedFiles, onRemoveFile, onUploadFiles }) => (
    <div className="pt-48 bg-gray-100">
      <h2 className="text-blue-500 text-4xl">Upload Your File</h2>
      <Dropzone onDrop={(acceptedFiles) => onFileUpload(acceptedFiles)}>
        {({ getRootProps, getInputProps }) => (
          <div {...getRootProps()} className="border border-blue-500 rounded p-3 my-3 flex justify-center items-center h-48">
            <input {...getInputProps()} />
            <p className="text-lg">Drag and drop your files here, or click to browse your device</p>
          </div>
        )}
      </Dropzone>
      <div className="flex justify-center">
        <button className="text-white bg-blue-500 px-5 py-3 rounded" onClick={onUploadFiles}>
            Upload Files
        </button>
      </div>
      <div>
        <h3 className="text-blue-500 text-3xl pt-5">Uploaded Files:</h3>
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
  const [pendingFiles, setPendingFiles] = useState([]);

  const handleInputChange = (e) => {
    setNewMessage(e.target.value);
  };

  const handleSendMessage = async () => {
    if (newMessage.trim() !== '') {
      const newUserQuestion = {
        message: newMessage,
        isUserQuestion: true,
      };
  
      setMessages([...messages, newUserQuestion]);
  
      try {
        const response = await axios.post('http://localhost:8000/query', { text: newMessage });
  
        const chatbotResponse = {
          message: response.data.Answer,
          isUserQuestion: false,
        };
  
        setMessages([...messages, newUserQuestion, chatbotResponse]);
      } catch (error) {
        console.error('Error sending message:', error);
      }
  
      setNewMessage('');
    }
  };

  const handleFileUpload = (files) => {
    setUploadedFiles([...uploadedFiles, ...files]);
    setPendingFiles([...pendingFiles, ...files]);
  };

  const handleUploadFiles = async () => {
    const formData = new FormData();
  
    pendingFiles.forEach((file) => {
      formData.append('file', file);
    });
  
    try {
      await axios.post('http://localhost:8000/upload', formData);
      setPendingFiles([]);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
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
          onUploadFiles={handleUploadFiles}
        />

      </div>
      <div className="w-2/3 p-3">
        <div>
          {messages.map((msg, index) => (
            <ChatMessage key={index} {...msg} />
          ))}
        </div>
        <form className="fixed bottom-0 w-full bg-gray-100 p-4" onSubmit={handleFormSubmit}>
        <div className="flex h-20 overflow-auto pl-24">
            <input
            type="text"
            className="w-1/2 mr-2 p-2 border rounded text-2xl"
            placeholder="Talk to Assistant"
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