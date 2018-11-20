import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import { IoIosThermometer } from 'react-icons/io'

import { Button } from 'evergreen-ui'
import Aquarium from './Components/Aquarium'

import { LineChart, Line } from 'recharts';


const data = [
    { name: 142, uv: 36.3 },
    { name: 196, uv: 70.3 },
];

ReactDOM.render(
  <div>
    <LineChart width={500} height={500} data={data}>
      <Line type="monotone" dataKey="uv" stroke="#8884d8" />
    </LineChart>
  </div>,
  document.getElementById('root')
)


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
