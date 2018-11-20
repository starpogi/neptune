import React from 'react';
import ReactDOM from 'react-dom';
import Aquarium from './Aquarium';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Aquarium />, div);
  ReactDOM.unmountComponentAtNode(div);
});
