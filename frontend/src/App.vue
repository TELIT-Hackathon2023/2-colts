<script setup>
import ButtonLink from "@/lib/ButtonLink.vue";
import TheQuestionInput from "@/components/TheQuestionInput.vue";
</script>

<template>
  <h1>Tvoja mama</h1>
  <ButtonLink>lol</ButtonLink>
  <TheQuestionInput></TheQuestionInput>
</template>

<style lang="scss">
@import "@/assets/styles/reset.scss";
@import "@/assets/styles/abstracts.scss";

body {
  background-color: $body-background-color;
  font-family: "SfPro-R", sans-serif;
  color: $body-color;
}

.container {
  max-width: 100rem;
  margin: 0 auto;
}
</style>
