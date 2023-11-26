<script setup>
import ButtonLink from "@/lib/ButtonLink.vue";
import TheQuestionInput from "@/components/TheQuestionInput.vue";
import TheSuggestions from "@/components/TheSuggestions.vue";
import TheUserTypeSelection from "@/components/TheUserTypeSelection.vue";
import { store } from "@/states";
</script>

<template>
  <main>
    <div class="container">
      <div class="title">
        <h1>TARDIS AI Chatbot</h1>
        <h2>Powered by COLTS</h2>
      </div>
      <TheUserTypeSelection></TheUserTypeSelection>
      <TheQuestionInput></TheQuestionInput>
      <TheSuggestions></TheSuggestions>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      selectedRole: "beginner",
    };
  },
};
</script>

<style lang="scss">
@import "@/assets/styles/reset.scss";
@import "@/assets/styles/abstracts.scss";

body {
  background-color: $body-background-color;
  font-family: "SfPro-R", sans-serif;
  color: $body-color;
}

.container {
  padding: 0 2.4rem;
  width: clamp(50rem, 90rem, 100rem);
  margin: 0 auto;
}
</style>
