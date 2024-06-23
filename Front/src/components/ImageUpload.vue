<template>
  <v-container class="image-upload">
    <!-- Image upload form -->
    <v-form @submit.prevent="handleSubmit">
      <v-row align="center">
        <v-col>
          <!-- File input for uploading images -->
          <v-file-input
            v-model="file"
            label="Télécharger une image"
            accept="image/*"
            prepend-icon="mdi-folder"
            @change="handleImageChange"
          ></v-file-input>
        </v-col>
        <v-col cols="auto">
          <!-- Button to clear fields -->
          <v-btn icon @click="clearFields" color="#201c1c" dark class="refresh-button">
            <v-icon>mdi-refresh-circle</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <!-- Button to extract text from image -->
      <v-btn :loading="isExtracting" type="submit" color="#201c1c" dark>
        {{ isExtracting ? 'Extraction en cours...' : 'Extraire le texte' }}
      </v-btn>
    </v-form>

    <!-- Display image and extracted text -->
    <v-row v-if="image" class="mt-4">
      <!-- If text is not extracted, show full width image -->
      <v-col v-if="!extractedText" cols="12">
        <v-card style="border: 1px solid black; padding: 10px;">
          <v-card-title>Image</v-card-title>
          <v-card-text>
            <v-img :src="image" aspect-ratio="16/9" class="mb-4"></v-img>
          </v-card-text>
        </v-card>
      </v-col>
      <!-- If text is extracted, show image and text side by side -->
      <v-col v-if="extractedText" cols="12" md="6">
        <v-card class="relative-card" style="border: 1px solid black; padding: 10px;">
          <v-card-title>Image</v-card-title>
          <v-card-text>
            <v-img :src="image" aspect-ratio="16/9" class="mb-4"></v-img>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col v-if="extractedText" cols="12" md="6">
        <!-- Card to display extracted text -->
        <v-card class="relative-card" style="border: 2px solid black; padding: 10px;">
          <v-card-title>
            <!-- Button to convert text to speech -->
            <v-btn v-if="extractedText" :loading="isConverting" icon @click="convertTextToSpeech" class="top-left-icon" color="#201c1c" dark>
              <v-icon>{{ isConverting ? 'mdi-loading' : 'mdi-volume-high' }}</v-icon>
            </v-btn>
            Texte
            <!-- Button to copy extracted text to clipboard -->
            <v-btn v-if="extractedText" icon @click="copyText" class="copy-button" color="#201c1c" dark>
              <v-icon>{{ copyStatus === 'copied' ? 'mdi-check' : 'mdi-content-copy' }}</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text>
            <!-- Display extracted text -->
            <pre>{{ extractedText }}</pre>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2';
import clipboardCopy from 'clipboard-copy';

// Reactive variables
const image = ref(null);
const file = ref(null);
const extractedText = ref('');
const copyStatus = ref(''); // 'copied' or ''
const isExtracting = ref(false); // To track extraction state
const isConverting = ref(false); // To track text-to-speech conversion state

// Function to handle form submission
const handleSubmit = async () => {
  if (!file.value) {
    // Show warning if no image selected
    Swal.fire({
      icon: 'warning',
      title: 'Aucune image sélectionnée',
      text: 'Veuillez d\'abord sélectionner une image',
    });
    return;
  }

  isExtracting.value = true; // Set extracting state to true

  // Create form data to send the image
  const formData = new FormData();
  formData.append('image', file.value);

  try {
    // Send a POST request to the Flask API
    const response = await axios.post('http://localhost:5000/api/ocr', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    // Set the extracted text from the response
    extractedText.value = response.data.text;
    isExtracting.value = false; // Set extracting state to false

    // Check if extracted text is empty and show a warning popup
    if (!extractedText.value.trim()) {
      Swal.fire({
        icon: 'warning',
        title: 'Aucun texte extrait',
        text: 'Aucun texte n\'a été trouvé dans l\'image téléchargée',
      });
    }
  } catch (error) {
    console.error('Error extracting text:', error);
    Swal.fire({
      icon: 'error',
      title: 'Extraction échouée',
      text: 'Échec de l\'extraction du texte de l\'image',
    });
    isExtracting.value = false; // Set extracting state to false
  }
};

// Function to handle image input change event
const handleImageChange = (event) => {
  const fileObj = event.target.files[0];
  if (fileObj) {
    file.value = fileObj;

    // Display selected image preview
    const reader = new FileReader();
    reader.onload = (e) => {
      image.value = e.target.result;
    };
    reader.readAsDataURL(fileObj);
  }
};

// Function to clear all fields and reset states
const clearFields = () => {
  file.value = null;
  image.value = null;
  extractedText.value = '';
  isExtracting.value = false;
  isConverting.value = false;
};

// Function to copy extracted text to clipboard
const copyText = () => {
  clipboardCopy(extractedText.value)
    .then(() => {
      copyStatus.value = 'copied';
      setTimeout(() => {
        copyStatus.value = '';
      }, 2000); // Revert the icon back after 2 seconds
    })
    .catch((error) => {
      console.error('Error copying text:', error);
    });
};

// Function to convert extracted text to speech
const convertTextToSpeech = async () => {
  if (!extractedText.value) {
    // Show warning if no text to convert
    Swal.fire({
      icon: 'warning',
      title: 'Aucun texte disponible',
      text: 'Veuillez d\'abord extraire le texte',
    });
    return;
  }

  isConverting.value = true; // Set converting state to true

  try {
    // Send a POST request to convert text to speech
    const response = await axios.post('http://localhost:5000/api/text-to-speech', {
      text: extractedText.value,
    }, {
      responseType: 'blob'
    });

    // Play the generated audio
    const audioBlob = new Blob([response.data], { type: 'audio/mpeg' });
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    audio.play();
    isConverting.value = false; // Set converting state to false
  } catch (error) {
    console.error('Error converting text to speech:', error);
    Swal.fire({
      icon: 'error',
      title: 'Conversion échouée',
      text: 'Échec de la conversion du texte en discours',
    });
    isConverting.value = false; // Set converting state to false
  }
};
</script>

<style scoped>
.image-upload {
  max-width: 800px;
  margin: auto;
  text-align: center;
}

.v-img {
  max-width: 100%;
  height: auto;
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
}

.relative-card {
  position: relative;
}

.copy-button {
  position: absolute;
  top: 5px;
  right: 10px;
}

.top-left-icon {
  position: absolute;
  top: 5px;
  left: 16px;
}

.refresh-button {
  position: relative;
  top: -8px;
}
</style>
