<template>
  <section
    class="popsection"
    @click="(e) => (e.target === e.currentTarget ? $emit('closePopup') : '')"
  >
    <div class="container">
      <div class="popup-window">
        <header>
          <h2 class="popup__title">{{ popupTitle }}</h2>
          <p class="popup__subtitle">{{ popupSubtitle }}</p>
        </header>
        <slot></slot>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  props: {
    popupTitle: String,
    popupSubtitle: String,
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";
section {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  background-color: rgba(0, 0, 0, 0.654);
  backdrop-filter: blur(5px);
  transition: all 0.5s ease;
  @include center-content;
}

header {
  margin-bottom: 1.8rem;
}

.container {
  width: clamp(45rem, 60rem, 100rem);
}
.popup {
  &__title {
    margin-bottom: 1.2rem;
  }
  &__subtitle {
    color: rgba(255, 255, 255, 0.616);
  }
}
.popup-window {
  padding: 2.4rem;
  background-color: $grey;
  border-radius: 1.4rem;
}
</style>
