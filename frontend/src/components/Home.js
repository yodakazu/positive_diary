import React, { useState } from 'react';
import './Home.css';

const Home = () => {
  const [content, setContent] = useState('');
  const [date, setDate] = useState('');
  const [imageurl, setImageurl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const diaryEntry = { content, date, imageurl };

    try {
      const response = await fetch('http://localhost:8000/diaries/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(diaryEntry),
      });

      if (response.ok) {
        console.log('Diary entry saved successfully');
        setContent('');
        setDate('');
        setImageurl('');
      } else {
        console.error('Error saving diary entry');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="heading">Welcome to Home Page</h1>
      <p className="paragraph">This is a simple React component template.</p>

      <form onSubmit={handleSubmit}>
      <div className="form-group">
          <label htmlFor="content">Content:</label>
          <textarea
            id="content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
          ></textarea>
        </div>
        <div className="form-group">
          <label htmlFor="date">Date:</label>
          <input
            type="date"
            id="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="imageurl">Image URL:</label>
          <input
            type="url"
            id="imageurl"
            value={imageurl}
            onChange={(e) => setImageurl(e.target.value)}
          />
        </div>
        <button type="submit">Save Diary Entry</button>
      </form>
    </div>
  );
};

export default Home;
