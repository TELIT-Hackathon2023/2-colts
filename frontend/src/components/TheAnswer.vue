<template>
  <section>
    <h3>Chat</h3>
    <div class="chat">
      <div v-for="(pair, index) in answer" :key="index" class="chat__entry">
        <header>
          <span class="question">
            {{ pair.initial }}
          </span>
          <div class="buttons">
            <button class="reaction">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z"
                />
              </svg>
            </button>
            <button class="reaction">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M7.5 15h2.25m8.024-9.75c.011.05.028.1.052.148.591 1.2.924 2.55.924 3.977a8.96 8.96 0 01-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398C20.613 14.547 19.833 15 19 15h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 00.303-.54m.023-8.25H16.48a4.5 4.5 0 01-1.423-.23l-3.114-1.04a4.5 4.5 0 00-1.423-.23H6.504c-.618 0-1.217.247-1.605.729A11.95 11.95 0 002.25 12c0 .434.023.863.068 1.285C2.427 14.306 3.346 15 4.372 15h3.126c.618 0 .991.724.725 1.282A7.471 7.471 0 007.5 19.5a2.25 2.25 0 002.25 2.25.75.75 0 00.75-.75v-.633c0-.573.11-1.14.322-1.672.304-.76.93-1.33 1.653-1.715a9.04 9.04 0 002.86-2.4c.498-.634 1.226-1.08 2.032-1.08h.384"
                />
              </svg>
            </button>
            <button class="reaction">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path
                  d="M11.53,2C11.53,4.4 13.5,6.35 15.88,6.35H17.66V8.05C17.66,10.45 19.6,12.39 22,12.4V2.84A0.84,0.84 0 0,0 21.16,2H11.53M6.77,6.8C6.78,9.19 8.72,11.13 11.11,11.14H12.91V12.86C12.92,15.25 14.86,17.19 17.25,17.2V7.63C17.24,7.17 16.88,6.81 16.42,6.8H6.77M2,11.6C2,14 3.95,15.94 6.35,15.94H8.13V17.66C8.14,20.05 10.08,22 12.47,22V12.43A0.84,0.84 0 0,0 11.63,11.59L2,11.6Z"
                />
              </svg>
            </button>
          </div>
        </header>
        <div class="body">
          <p>
            {{ pair.answer }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  props: {
    answer: String,
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";

.chat {
  background-color: black;
  border-radius: 1.6rem;
  gap: 2.4rem;
  padding: 2.4rem;
  height: 37rem;
  overflow: scroll;

  header {
    padding: 1.4rem;
    background-color: $light-grey;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .body {
    padding: 2.4rem;
    overflow: hidden;
  }
  &__entry {
    background-color: $grey;
    border-radius: 1.2rem;
    overflow: hidden;
    // height: 23rem;
    margin-bottom: 2.4rem;
    white-space: pre-wrap;

    .question {
      font-family: "SfPro-M", sans-serif;
    }
  }
}
.buttons {
  display: flex;
  gap: 0.8rem;
  color: white;
}
.reaction {
  height: 2.8rem;
  width: 2.8rem;
  background-color: transparent;
  border: none;
  padding: 0.3rem;
  border-radius: 0.3rem;
  &:hover {
    background-color: $grey;
    color: $pink;
    fill: $pink;
  }
}
</style>
