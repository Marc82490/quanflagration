$(function(){
    configure()
});

function configure(){
    $("#q").typeahead({
        highlight: false,
        minLength: 1
    },
    {
        display: function(suggestion) { return suggestion.ticker_symbol; },
        limit: 10,
        source: search,
        templates: {
            sugesstion: Handlebars.compile(
                "<div>" +
                "{{ ticker_symbol }}" +
                "</div>"
            )
        }
    }
    );

    $("#q").focus();
}

function search(query, syncResults, asyncResults)
{
    // get places matching query (asynchronously)
    var parameters = {
        q: query
    };
    $.getJSON(Flask.url_for("search"), parameters)
    .done(function(data, textStatus, jqXHR) {
     
        // call typeahead's callback with search results (symbols)
        asyncResults(data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {

        // log error to browser's console
        console.log(errorThrown.toString());

        // call typeahead's callback with no results
        asyncResults([]);
    });
}
