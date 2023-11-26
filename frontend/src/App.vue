<script setup>
import TheQuestionInput from "@/components/TheQuestionInput.vue";
import TheSuggestions from "@/components/TheSuggestions.vue";
import TheUserTypeSelection from "@/components/TheUserTypeSelection.vue";
import JiraPopup from "@/lib/JiraTicketPopup.vue";
import TheAnswer from "@/components/TheAnswer.vue";
import axios from "axios";
import { store } from "@/states";
</script>

<template>
  <JiraPopup
    @closePopup="isPopupVisible = false"
    popupTitle="New Jira Ticket"
    popupSubtitle="Check the information below to create a new ticket in [name of the JIRA]"
    v-if="isPopupVisible"
  ></JiraPopup>
  <main>
    <div class="container">
      <div class="title">
        <h1>TARDIS AI Chatbot</h1>
        <h2>Powered by COLTS</h2>
      </div>
      <TheUserTypeSelection></TheUserTypeSelection>
      <TheQuestionInput
        @questionSubmitted="(e) => getAnswer(e)"
        :isResponseLoading="isResponseLeading"
      ></TheQuestionInput>
      <TheSuggestions
        v-if="!answer[0]"
        @suggestedPromptSubmitted="(e) => getAnswer(e)"
      ></TheSuggestions>
      <TheAnswer v-if="answer[0]" :answer="answer"></TheAnswer>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      selectedRole: "beginner",
      isPopupVisible: false,

      isResponseLeading: false,
      answer: [],
    };
  },

  methods: {
    async getAnswer(prompt) {
      this.isResponseLeading = true;
      // axios request
      try {
        const response = await axios.get("http://localhost:8080/test", {
          params: {
            data: prompt,
            persona: ["beginner", "developer", "business analyst"].indexOf(
              store.selectedRole
            ),
          },
        });
        console.log(response.data.data.answer);
        this.isResponseLeading = false;
        this.answer.unshift(response.data.data);
      } catch (error) {
        console.error(error);
      }
    },
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
  width: clamp(45rem, 90rem, 100rem);
  margin: 0 auto;
}
</style>
