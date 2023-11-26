<script setup>
import ButtonLink from "../lib/ButtonLink.vue";
import axios from "axios";
</script>
<template>
  <section>
    <div class="container">
      <input
        type="text"
        v-model="inputText"
        placeholder="Write your question "
      />
      <ButtonLink @click="getAnswer"
        ><svg
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
  methods: {
    async getAnswer() {
      // axios request
      try {
        const response = await axios.get("http://localhost:8080/test");
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";
section {
  margin-bottom: 4.2rem;
}
.container {
  background-color: rgb(64, 64, 64);
  padding: 0.6rem 0.6rem 0.6rem 2rem;

  display: grid;
  grid-template-columns: 1fr auto;
  border-radius: 0.8rem;
  gap: 1.6rem;
}

input {
  background-color: transparent;
  border: none;
  outline: none;
  width: 100%;
}
.icon {
  height: 2rem;
  width: 2rem;
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
</style>
