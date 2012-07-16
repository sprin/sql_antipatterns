//== Statement ==

// Has attributes:
// `name` (the name of the statement
// `alchemy_stmt` (an SQL Alchemy statement as a string)
// `sql_stmt` (the Alchemy statement compiled to an SQL statement as a string)
// `results` (the rows returned by the query)
window.Statement = Backbone.Model.extend({
  
  urlRoot: '/exec'

});

//== StatementList Collection ==
window.StatementList = Backbone.Collection.extend({

  model: Statement

});

$(document).ready(function(){
  //== StatementView ==

  // Represents a single statement in a list of statements.
  window.StatementView = Backbone.View.extend({


    template: Handlebars.compile($('#statement-form-template').html()),

    events: {
      // Show the form when the "Add Note" link is clicked
      "click .inject-stmt": "execStmt"
    },

    initialize: function(){
      this.statement = this.options.statement;
      _.bindAll(this, 'render', 'updateResults');
      // ###Bindings

      // Re-render on changes to the Note.
      this.statement.on('change', this.render);
    },

    // ###Render
    // with Statement data.
    render: function(){
      console.log('rendering StatementView');
      var render_content = this.template({
        alchemy_stmt: this.statement.get('alchemy_stmt'),
        sql_stmt: this.statement.get('sql_stmt'),
        results: this.statement.get('results')
      });
      this.$el.html(render_content);
      return this;
    },

    // ###Execute statement
    execStmt: function(e){
      console.log('executing statement');
      e.preventDefault();
      // Iterate over each formfield and corresponding input and set the
      // model value to the form input value.
      this.statement.set(
          'alchemy_stmt', this.$(".alchemy-stmt textarea").val(),
          // Silence the change events since `save` will trigger one.
          {silent: true});
      this.statement.save(
        {},
        {error: this.handleErrors, success: this.updateResults});
    },

    updateResults: function(model, response) {
      console.log('success! results:');
      console.log(response);
      this.statement.set({
        results: JSON.stringify(response, null, 2)
      });
    },

    handleErrors: function(model, response) {
      console.log('fail!');
    }
  });

  window.SqlaView = Backbone.View.extend({

    initialize: function(){
      this.inject_new = new StatementView({
        el: '#inject-new',
        statement: new Statement
      })
    }
  });

  window.sqla_view = new SqlaView();
});


