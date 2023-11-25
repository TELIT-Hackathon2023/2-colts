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
  data() {
    return {
      cards: [
        { title: "1", content: "a" },
        { title: "2", content: "b" },
        { title: "3", content: "c" },
      ],
    };
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";

.suggestions {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 2.4rem;

  &__card {
    background-color: $grey;
    padding: 1.6rem;
    border-radius: $border-radius-small;
  }
}
</style>
