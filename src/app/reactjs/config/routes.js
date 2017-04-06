var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var hashHistory = ReactRouter.hashHistory;
var IndexRoute = ReactRouter.IndexRoute;

var Index = require('../containers/index');
var Dashboard = require('../containers/dashboard');


var routes = (
  <Router history={hashHistory}>
    <Route path='/' component={Index}>
      <IndexRoute component={Dashboard} />
      <Route path='/dashboard' component={Dashboard} />
    </Route>
  </Router>
);

module.exports = routes;
