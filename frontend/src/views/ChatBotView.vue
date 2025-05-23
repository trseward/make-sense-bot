<template>
  <div class="container min-vh-100 d-flex flex-column justify-content-center align-items-center bg-light">
    <div class="card shadow w-100" style="max-width: 500px;">
      <div class="card-body">
        <h1 class="card-title h3 text-center mb-4">Make Sense Bot</h1>
        <form @submit.prevent="submitPrompt">
          <div class="mb-3">
            <label for="age-group" class="form-label">Select Age Group:</label>
            <select v-model="selectedAgeGroup" id="age-group" class="form-select">
              <option disabled value="">-- Select Age Group --</option>
              <option v-for="group in ageGroups" :key="group.value" :value="group.value">
                {{ group.label }}
              </option>
            </select>
          </div>
          <div class="mb-3">
            <label for="subject-prompt" class="form-label">Subject Prompt</label>
            <textarea v-model="subjectPrompt" id="subject-prompt" class="form-control" rows="4" placeholder="Enter your subject prompt here..."></textarea>
          </div>
          <button type="submit" class="btn btn-primary w-100">Summarize</button>
        </form>
        <div v-if="errorMessage" class="alert alert-danger mt-3 text-center">{{ errorMessage }}</div>
        <div v-if="summary" class="card mt-4">
          <div class="card-body">
            <h2 class="card-title h5 mb-2">Summary</h2>
            <p class="card-text">{{ summary }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { submitPrompt } from '../services/api';

export default {
  name: 'ChatBotView',
  data() {
    return {
      ageGroups: [
        { label: 'Early Elementary (5-8)', value: 'Early Elementary' },
        { label: 'Late Elementary (9-11)', value: 'Late Elementary' },
        { label: 'Middle School (12-14)', value: 'Middle School' },
        { label: 'High School (15-18)', value: 'High School' }
      ],
      selectedAgeGroup: '',
      subjectPrompt: '',
      summary: '',
      errorMessage: ''
    };
  },
  methods: {
    async submitPrompt() {
      this.errorMessage = '';
      this.summary = '';
      if (!this.selectedAgeGroup) {
        this.errorMessage = 'Please select an age group before submitting your question.';
        return;
      }
      if (!this.subjectPrompt.trim()) {
        this.errorMessage = 'Please enter a subject prompt.';
        return;
      }
      try {
        const result = await submitPrompt(this.selectedAgeGroup, this.subjectPrompt);
        this.summary = result.summary || 'No summary returned.';
      } catch (err) {
        this.errorMessage = 'An error occurred while fetching the summary.';
      }
    }
  }
};
</script>

