<script setup>
import { store } from "@/states.js";
</script>
<template>
  <section>
    I am a:
    <form>
      <div v-for="(role, index) in roles" :key="index">
        <input
          v-model="store.selectedRole"
          type="radio"
          :id="role"
          :value="role"
          style="display: none"
        />
        <label
          :class="['role-button', store.selectedRole === role ? 'active' : '']"
          :for="role"
          >{{ role }}</label
        >
      </div>
    </form>
  </section>
</template>
<script>
export default {
  data() {
    return {
      roles: ["beginner", "developer", "business analyst"],
    };
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";

label {
  cursor: pointer;
}

section {
  margin-bottom: 1.2rem;
}

form {
  display: inline-flex;
  gap: 1rem;
  margin-left: 0.4rem;
}

.role-button {
  background-color: $grey;
  letter-spacing: 1px;
  padding: 0.2rem 1rem;
  border-radius: 0.4rem;
  color: rgba(255, 255, 255, 0.688);
  display: inline-block;

  input {
    line-height: 1.8;
  }

  &:hover {
    cursor: pointer;
  }
}

.active {
  outline: 1px solid $pink;
  box-shadow: 0 0 1.2rem rgba($color: $pink, $alpha: 0.5);
}
</style>
