let request = $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
    function (response) {
        let films = response.results;
        for (film of films)
        {
            let list_item = $('<li>', {'text': film.title});
            $('UL#list_movies').append(list_item);
        }
    }
);
