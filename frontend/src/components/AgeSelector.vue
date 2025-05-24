<template>
  <div>
    <label for="age-group">Select Age Group:</label>
    <select id="age-group" v-model="selectedAgeGroup">
      <option v-for="group in ageGroups" :key="group" :value="group">
        {{ group }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedAgeGroup: null,
      ageGroups: [
        "Early Elementary [5-8]",
        "Late Elementary [9-11]",
        "Middle School [12-14]",
        "High School [15-18]",
      ],
    };
  },
};
</script>

<style scoped>
/* Add styles here */
</style>
