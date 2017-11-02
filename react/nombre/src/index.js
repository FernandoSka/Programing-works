import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import Counter from './Counter.js';
export default Counter

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
