<template>
    <form method="POST" enctype="multipart/form-data"  @submit.prevent="saveMovie" id="movieForm">
        <!---Success and Error Messages-->
        <div v-if="successMessage" class="success"> {{ successMessage }} </div>
        
        <div v-if="errorMessage.length > 0" class="error">
            <ul>
                <li v-for="(message, index) in errorMessage" :key="index"> {{ message }} </li>
            </ul>
        </div>

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

        <button type="submit" name="submit" class="btn">Submit</button>
    </form>
</template>

<script setup>
    import { ref, onMounted } from "vue"; 
    let csrf_token = ref("");
    
    const successMessage = ref('');
    const errorMessage = ref([]);
    
    function getCsrfToken() { 
        fetch('/api/v1/csrf-token') 
        .then((response) => response.json()) 
        .then((data) => { 
            console.log(data); 
            csrf_token.value = data.csrf_token; 
        })
        .catch(error => { 
            console.log('Error fetching CSRF token:', error); 
        }); 
    }
    onMounted(() => {
        getCsrfToken(); 
    }); 

    function saveMovie() {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

         errorMessage.value = [];   // Clear error message space before processing the form
         successMessage.value = '';  // Clear success message

         // Client-Side Validation
         let title = form_data.get('title');
         let description = form_data.get('description');
         let poster = form_data.get('poster');

         if (!title || !title.trim()) {
        errorMessage.value.push('Error in the Title field - This field is required.');
        }

        if (!description || !description.trim()) {
            errorMessage.value.push('Error in the Description field - This field is required.');
        }

        if (!poster || poster.size === 0) {
            errorMessage.value.push('Error in the Photo field - This field is required.');
        }
    
        fetch("/api/v1/movies", { 
            method: 'POST',
            body : form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        }) 
        .then(response => response.json())
        .then((data) => { 
            if (data.message){
                // Success message
                successMessage.value = "File Upload Successful";
                errorMessage.value = [];

                movieForm.reset();  // Reset the movie form

            } else if (data.errors) {
                // Error message
                successMessage.value = '';
                
                // Handle both object + string formats safely
                errorMessage.value = [];

                if (Array.isArray(data.errors)) {
                    data.errors.forEach(error => {
                        if (typeof error === 'string') {
                            errorMessage.value.push(error);
                        } else {
                            const key = Object.keys(error)[0];
                            const value = error[key];
                            errorMessage.value.push(`Error in the ${key} field - ${value}`);
                        } 
                    });
                } else {
                // If errors come as object
                    for (let field in data.errors) {
                        let messages = data.errors[field];
                        messages.forEach(msg => {
                            errorMessage.value.push(`Error in the ${field} field - ${msg}`);
                        });
                    }
                }
            }
        })  
    }
</script>

<style>
/* Add any component specific styles here */
#movieForm{
    margin: 15px 50px 10px 50px;
  }

.add-movie h2{
    margin: 5px 50px;
}

.success{
    background-color: rgb(87, 219, 87);
    border-radius: 5px;
    color: wheat;
    font-size: 14px;
    padding: 5px 10px;
}

.error{
    background-color: #ce7a82;
    border-radius: 5px;
    color: wheat;
    font-size: 14px;
    padding: 5px 10px;
    margin-bottom: 15px;
}

.btn{
    color: white;
    background-color: rgb(17, 161, 161);
    padding: 5px 12px;
}

.btn:hover{
    background-color: rgb(48, 102, 102);
    color: white;
}

</style>