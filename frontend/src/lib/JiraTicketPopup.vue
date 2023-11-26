<script setup>
import Popup from "@/lib/Popup.vue";
import axios from "axios";
</script>

<template>
  <Popup
    @closePopup="$emit('closePopup')"
    popupTitle="New Jira Ticket"
    popupSubtitle="Check the information below to create a new ticket in [name of the JIRA]"
  >
    <form @submit.prevent="submitForm">
      <div>
        <label for="summary">Summary:</label>
        <input id="summary" type="text" v-model="summary" required />
      </div>
      <div class="flexgroup">
        <div>
          <label for="issueType">Issue Type:</label>
          <input id="issueType" type="text" v-model="issueType" required />
        </div>

        <div>
          <label for="priority">Priority:</label>
          <select id="priority" v-model="priority" required>
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>
      </div>

      <div>
        <label for="description">Description:</label>
        <textarea
          rows="4"
          id="description"
          v-model="description"
          required
        ></textarea>
      </div>
      <div class="flexgroup">
        <div>
          <label for="labels">Labels (separate by commas):</label>
          <input type="text" id="labels" v-model="labels" />
        </div>
        <div>
          <label for="dueDate">Due Date:</label>
          <input type="date" id="dueDate" v-model="dueDate" />
        </div>
      </div>
      <div>
        <label class="custom-file-upload" for="attachments"
          >Attachments:
          <div class="flexfiles">
            <span
              class="fileUploaded"
              v-for="(attachment, index) in attachments"
              :key="index"
              >{{ attachment.name }}</span
            >
            <input
              type="file"
              multiple
              id="attachments"
              v-on:change="handleFileUpload"
            />
          </div>
        </label>
      </div>

      <button type="submit">Submit</button>
    </form>
  </Popup>
</template>
<script>
export default {
  data() {
    return {
      summary: "",
      issueType: "",
      priority: "",
      description: "",
      labels: "",
      dueDate: "",
      attachments: null,
    };
  },
  methods: {
    async submitForm() {
      try {
        // Make a GET request to the proxy server
        const response = await axios.get("http://localhost:3001/api");

        console.log(response.data);
        // Handle the response from the external server here
      } catch (error) {
        console.error(error);
        // Handle errors from the proxy or the external server
      }
    },
    handleFileUpload(event) {
      this.attachments = event.target.files;
    },
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";
form {
  display: grid;
  div {
    display: flex;
    flex-direction: column;
    margin-bottom: 0.4rem;

    input,
    textarea,
    button,
    select {
      display: block;
      border: none;
      border-radius: 0.3rem;
      padding: 0.4rem 1.6rem;
    }

    select {
      padding: 0.7rem 1.6rem;
    }

    label {
      letter-spacing: 0.5px;
    }

    input,
    select,
    textarea {
      background-color: darken($light-grey, 7%);
      color: white;
      resize: none;
      outline: none;
    }
  }
  button {
    margin-top: 1.6rem;
    outline: none;
    background-color: $pink;
    // color: white;
    border: none;
    border-radius: 0.3rem;
    padding: 0.4rem 1.6rem;
    font-size: 1.8rem;
    font-family: "SfPro-M", sans-serif;
    letter-spacing: 1px;

    &:hover {
    }
  }
}

.flexgroup {
  display: grid;
  grid-template-columns: 1fr 35%;
  gap: 1.6rem;
}

input[type="file"] {
  background-color: transparent;
  display: none;
}

.custom-file-upload {
  border: 1px solid #666666;
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  cursor: pointer;
  border-radius: 0.3rem;
  margin-top: 0.8rem;

  .flexfiles {
    display: inline-flex;
    margin-left: 0.8rem;
    align-items: center;
    gap: 0.8rem;
    flex-direction: row;
    margin-bottom: 0;
  }
}

.fileUploaded {
  display: inline-block;
  background-color: $light-grey;
  padding: 0.2rem 0.6rem;
  border-radius: 0.3rem;
  color: white;
  font-size: 1.4rem;
}
</style>
