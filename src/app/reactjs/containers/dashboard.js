var React = require('react');
var ReactRouter = require('react-router');

import {Segment} from 'semantic-ui-react';

var Dashboard = React.createClass({
  getInitialState: function(){
    return ({
    });
  },
  render: function() {
    return (
      <Segment >
        From here all depends on the project
      </Segment>
    )
  }
});

module.exports = Dashboard;
