<script setup>
import TheQuestionInput from "@/components/TheQuestionInput.vue";
import TheSuggestions from "./components/TheSuggestions.vue";
</script>

<template>
  <main>
    <div class="container">
      <div class="title">
        <h1>TARDIS AI Chatbot</h1>
        <h2>Powered by COLTS</h2>
      </div>
      <TheQuestionInput></TheQuestionInput>
      <TheSuggestions></TheSuggestions>
    </div>
  </main>
</template>

<style lang="scss">
@import "@/assets/styles/reset.scss";
@import "@/assets/styles/abstracts.scss";

body {
  background-color: $body-background-color;
  font-family: "SfPro-R", sans-serif;
  color: $body-color;
}

main {
  min-height: 100vh;
  @include center-content;
}

.title {
  text-align: center;
  padding-bottom: 5.6rem;

  h1 {
    font-size: 5.6rem;
    letter-spacing: 2px;
    font-family: "SfPro-B", sans-serif;
    line-height: 1.2;
  }

  h2 {
    font-size: 1.8rem;
    letter-spacing: 1px;
    font-family: "SfPro-M", sans-serif;
    color: $light-grey;
  }
}
.container {
  padding: 0 2.4rem;
  width: clamp(50rem, 80rem, 100rem);
  margin: 0 auto;
}
</style>
