<template>
  <v-app>
    <v-main>
      <!-- Main container for the application -->
      <v-container fluid class="app-container">
        <v-row justify="center">
          <v-col cols="12" md="8">
            <!-- Card for the main content -->
            <v-card class="content-card" style="border: 1px solid black;">
              <h1 class="mb-4">Extracteur de Texte</h1>
              <!-- Include the ImageUpload component -->
              <ImageUpload />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import ImageUpload from './components/ImageUpload.vue';


</script>

<style scoped>
.app-container {
  background-color: #f8f4fc; /* Light purple background */
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content-card {
  background-color: white;
  padding: 20px;
  text-align: center;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); /* Optional: Adds a subtle shadow */
}

h1 {
  color: #2c3e50; /* Dark text color */
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 20px;
}
</style>
