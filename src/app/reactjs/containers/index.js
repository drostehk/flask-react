var React = require("react");
var Index = require("../components/index")


var IndexContainer = React.createClass({
  getInitialState: function(){
    return {
      header: 'Here is an example of flask & react',
      body: 'Working..'
    }
  },
  render: function(){
    return (
      <Index header={this.state.header} body={this.state.body}
             children={this.props.children} />
    );
  }
});

module.exports = IndexContainer;
