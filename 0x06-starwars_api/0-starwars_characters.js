#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (movieId == null) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details. Status code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((charUrl) => {
    request(charUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character details. Status code:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
