import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Home from './Home';
import Pricing from './Pricing';
import About from './About';
import Register from './Register';

function App() {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/pricing">Pricing</Link></li>
                        <li><Link to="/about">About</Link></li>
                        <li><Link to="/register">Register</Link></li>
                    </ul>
                </nav>

                <hr />

                <Route exact path="/" component={Home} />
                <Route path="/pricing" component={Pricing} />
                <Route path="/about" component={About} />
                <Route path="/register" component={Register} />
            </div>
        </Router>
    );
}

export default App;
