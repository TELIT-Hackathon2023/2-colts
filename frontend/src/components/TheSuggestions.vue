<script setup>
import { store } from "@/states.js";
</script>
<template>
  <section>
    <div class="suggestions">
      <div
        v-for="(card, index) in cards"
        :key="index"
        class="suggestions__card"
      >
        <h3>
          {{ card.title }}
        </h3>
        <p>
          {{ card.content }}
        </p>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "TheSuggestions",

  computed: {
    cards() {
      switch (store.selectedRole) {
        case "beginner":
          return [
            {
              title: "TLDR",
              content: "What is TARDIS? What can I use it for?",
            },
            {
              title: "Getting started",
              content: "How to onboard my application to Tardis?",
            },
            {
              title: "Limitations",
              content: "Which limitations does TARDIS have in terms of API’s?",
            },
          ];
          break;
        case "developer":
          return [
            {
              title: "Exposing an API",
              content: "How exactly can I create a team in Mission Control?",
            },
            {
              title: "Circuit breaker",
              content: "Does Tardis provide a circuit breaker functionality?",
            },
            {
              title: "CloudWalker",
              content:
                "How can I configure recipient client to expose multiple filetypes?",
            },
          ];
          break;
        case "business analyst":
          return [
            {
              title: "Exposing an API",
              content: "How exactly can I create a team in Mission Control?",
            },
            {
              title: "Circuit breaker",
              content: "Does Tardis provide a circuit breaker functionality?",
            },
            {
              title: "CloudWalker",
              content:
                "How can I configure recipient client to expose multiple filetypes?",
            },
          ];
          break;
      }
    },
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";

.suggestions {
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 2.4rem;

  &__card {
    background-color: $grey;
    padding: 1.6rem;
    border-radius: $border-radius-small;
    transition: all 150ms ease-out;
    &:hover {
      cursor: pointer;
      background-color: transparent;
    }

    h3 {
      margin-bottom: 1rem;
      letter-spacing: 1px;
    }

    p {
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      color: rgba(255, 255, 255, 0.6);
    }
  }
}
</style>
