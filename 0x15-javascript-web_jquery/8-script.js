$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (response) {
    const films = response.results;
    for (const film of films) {
      const listItem = $('<li>', { text: film.title });
      $('UL#list_movies').append(listItem);
    }
  }
);
