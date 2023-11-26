<script setup>
import ButtonLink from "@/lib/ButtonLink.vue";
import axios from "axios";
</script>
<template>
  <section>
    <div class="input__field">
      <input
        type="text"
        v-model="inputText"
        placeholder="Write your question "
      />
      <ButtonLink
        @click="$emit('questionSubmitted', inputText)"
        :type="'secondary'"
      >
        <svg
          v-if="!isResponseLoading"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6 icon"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6 icon spin"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
          />
        </svg>
      </ButtonLink>
    </div>
  </section>
</template>
<script>
export default {
  name: "TheQuestionInput",
  data() {
    return {
      inputText: "",
    };
  },
  props: {
    isResponseLoading: Boolean,
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";
section {
  margin-bottom: 4.2rem;
}
.container {
  .input {
    &__field {
      background-color: $grey;
      padding: 0.6rem 0.6rem 0.6rem 2rem;

      display: grid;
      grid-template-columns: 1fr auto;
      border-radius: 0.8rem;
      gap: 1.6rem;
    }
  }

  input {
    font-size: 1.8rem;
    background-color: transparent;
    border: none;
    outline: none;
    width: 100%;
    color: $white;
  }
  .icon {
    height: 2.4rem;
    width: 2.4rem;
  }
}

::placeholder {
  color: rgba(255, 255, 255, 0.4);
  opacity: 1; /* Firefox */
}

::-ms-input-placeholder {
  /* Edge 12 -18 */
  color: rgba(255, 255, 255, 0.4);
}

@supports not selector(:focus-visible) {
  .input__field:focus {
    outline: 2px solid $pink;
    outline-offset: 4px;
  }
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Apply the animation to the icon with a delay between spins */
.spin {
  display: inline-block;
  animation: spin 2s linear infinite; /* 4s duration, linear timing, infinite repetition */
}
</style>
