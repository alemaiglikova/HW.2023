import React from 'react';
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Register.css';

const Register = () => {
  return (
    <div className="register-container text-center">
      <h1>Join Our Amazing Community</h1>
      <p>Sign up to access all of our wonderful features and services.</p>
      <form>
        <input type="text" placeholder="Name" className="mb-2" />
        <br />
        <input type="email" placeholder="Email" className="mb-2" />
        <br />
        <input type="password" placeholder="Password" className="mb-2" />
        <br />
        <Button variant="primary" type="submit">
          Register
        </Button>
      </form>
    </div>
  );
};

export default Register;
