var React = require('react');
var ReactRouter = require('react-router');
var Link = ReactRouter.Link;
import { Icon, Input, Menu, Segment } from 'semantic-ui-react';

function Index(props){
  return (
    <div>
      <Header />
      <div className="ui main container">
        {props.children}
      </div>
    </div>
  )
};

var Header = React.createClass({
  getInitialState: function(){
    return ({
      activeItem: 'home'
    });
  },
  handleItemClick: function(e, { name }){
    this.setState({ activeItem: name })
  },
  render: function() {
    const {activeItem} = this.state;
    return (
      <Segment inverted>
        <Menu inverted pointing secondary>
          <Menu.Item name="home" active={activeItem === 'home'}
                     onClick={this.handleItemClick} as={Link} to="/"/>
          <Menu.Menu position='right'>
            <Menu.Item name="profile" active={activeItem === 'profile'}
                       onClick={this.handleItemClick} as={Link}
                       to="/settings/user" />
            <Menu.Item name='logout' active={activeItem === 'logout'}
                       as='a' href="/logout" />
          </Menu.Menu>
        </Menu>
      </Segment>
    )
  }
});

module.exports = Index;
