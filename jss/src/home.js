import React from 'react';
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container text-center">
      <h1>Welcome to Our Beautiful Website</h1>
      <p>
        Discover amazing features and services designed to make your life
        easier. Join us today!
      </p>
      <Button variant="primary">Get Started</Button>
    </div>
  );
};

export default Home;
