import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const [content, setContent] = useState('');
  const [date, setDate] = useState('');
  const [imageurl, setImageurl] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    // ローカルストレージからトークンを取得し、ログイン状態を確認
    const token = localStorage.getItem('authToken');
    if (token) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const userId = localStorage.getItem('userId');
    const diaryEntry = { content, date, imageurl, user_id: userId };

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

  const handleLogout = () => {
    // ローカルストレージからトークンを削除してログアウト
    localStorage.removeItem('authToken');
    localStorage.removeItem('userId');
    setIsLoggedIn(false);
    navigate('/login'); // ログインページにリダイレクト
  };

  if (!isLoggedIn) {
    return (
      <div className="container">
        <h1 className="heading">Welcome to Home Page</h1>
        <p className="paragraph">You need to log in to post a diary entry.</p>
        <Link to="/login">Go to Login Page</Link>
        <p className="paragraph">You need to sign up to first login.</p>
        <Link to="/signup">Go to Signup Page</Link>
      </div>
    );
  }

  return (
    <div className="container">
      <h1 className="heading">Welcome to Home Page</h1>
      <button onClick={handleLogout}>Logout</button>
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
