import React from 'react';
import { Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Pricing.css';

const Pricing = () => {
  return (
    <div className="pricing-container text-center">
      <h1>Our Amazing Pricing Plans</h1>
      <div className="d-flex justify-content-center">
        <Card className="plan mx-2">
          <Card.Body>
            <Card.Title>Basic Plan</Card.Title>
            <Card.Text>$10/month</Card.Text>
            <ul>
              <li>Feature 1</li>
              <li>Feature 2</li>
              <li>Feature 3</li>
            </ul>
            <Button variant="primary">Choose Plan</Button>
          </Card.Body>
        </Card>
        <Card className="plan mx-2">
          <Card.Body>
            <Card.Title>Premium Plan</Card.Title>
            <Card.Text>$20/month</Card.Text>
            <ul>
              <li>All Basic Plan Features</li>
              <li>Additional Feature 1</li>
              <li>Additional Feature 2</li>
            </ul>
            <Button variant="primary">Choose Plan</Button>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
};

export default Pricing;
