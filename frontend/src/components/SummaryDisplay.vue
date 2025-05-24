<template>
  <div>
    <h2>Summary</h2>
    <p v-if="summary">{{ summary }}</p>
    <p v-else>No summary available.</p>
  </div>
</template>

<script>
export default {
  props: {
    summary: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
/* Add styles here */
</style>
