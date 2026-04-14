<template>
    <h2 class="view-movies">Movies</h2>
    <div class="movie-list">
        <div class="movie" v-for="movie in movies" :key="movie.id">
            
            <img :src="'/api/v1/posters/' + movie.poster" alt="Movie Poster" />
          
            <div class="movie-details">
                <h3 class="title-details">{{ movie.title }}</h3>
                <p class="description-details">{{ movie.description }}</p>
            </div>
         
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

<style>
.view-movies{
    margin: 15px 50px 10px 50px;
    font-size: 24px;
}

.movie-list{

}
</style>