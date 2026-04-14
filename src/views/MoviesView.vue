<template>
    <h2 class="view-movies">Movies</h2>
    <div class="movie-list">
        <div class="movie" v-for="movie in movies" :key="movie.id">
          <img :src="'/api/v1/posters/' + movie.poster" alt="Movie Poster" />
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.description }}</p>
        </div>
    </div>

</template>

<script setup>
    import { ref, onMounted } from "vue"; 
    let movies = ref([]);

    function fetchMovies(){
        fetch( '/api/v1/movies', { method: 'GET'})
        .then((response) => response.json()) 
        .then((data) => { 
            movies.value = data.movies
        })
        .catch(error => { 
            console.log(error); 
        }); 
    }
    onMounted(() => {
        fetchMovies(); 
    }); 
</script>