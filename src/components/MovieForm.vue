<template>
    <form id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3"> 
            <label for="title" class="form-label">Movie Title</label> 
            <input type="text" name="title" class="form-control" /> 
        </div> 
        <div class="form-group mb-3"> 
            <label for="description" class="form-label">Movie Description</label> 
            <textarea name="description" class="form-control"></textarea> 
        </div> 
        <div class="form-group mb-3"> 
            <label for="poster" class="form-label">Movie Poster</label> 
            <input type="file" id="poster" name="poster" class="form-control" accept=".jpg, .jpeg, .png" /> 
        </div> 

        <button type="submit" name="submit" class="btn">Save Movie</button>
    </form>
</template>

<script setup>
    import { ref, onMounted } from "vue"; 
    let csrf_token = ref(""); 
    
    function getCsrfToken() { 
        fetch('/api/v1/csrf-token') 
        .then((response) => response.json()) 
        .then((data) => { 
            console.log(data); 
            csrf_token.value = data.csrf_token; 
        })
    }
    onMounted(() => {
        getCsrfToken(); 
    }); 

    function saveMovie() {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
    
        fetch("/api/v1/movies", { 
            method: 'POST',
            body : form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        }) 
        .then(function (response) { 
            return response.json(); 
        }) 
        .then(function (data) { 
            // display a success message 
            console.log(data); 
        }) 
        .catch(function (error) { 
            console.log(error); 
        });
        
    }
</script>

<style>
/* Add any component specific styles here */
</style>