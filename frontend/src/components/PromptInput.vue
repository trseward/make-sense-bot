<template>
  <div>
    <label for="prompt">Enter Subject Prompt:</label>
    <textarea id="prompt" v-model="prompt" placeholder="Type your subject prompt here..."></textarea>
  </div>
</template>

<script>
export default {
  data() {
    return {
      prompt: "",
    };
  },
};
</script>

<style scoped>
/* Add styles here */
</style>
