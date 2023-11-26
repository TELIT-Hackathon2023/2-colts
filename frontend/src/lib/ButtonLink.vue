<template>
  <button
    v-if="element === 'button' && isValidType"
    :class="['reset', typeClasses, sizeClasses]"
  >
    <slot></slot>
  </button>
  <!-- <router-link
    v-else-if="element === 'routerLink' && isValidType"
    :to="to"
    :class="['reset', typeClasses, sizeClasses]"
  >
    <slot></slot>
  </router-link> -->
  <a
    v-else-if="element === 'link' && isValidType"
    :href="href"
    :class="['reset', typeClasses, sizeClasses]"
  >
    <slot></slot>
  </a>
</template>
<script>
export default {
  name: "ButtonLink",

  props: {
    element: {
      type: String,
      validator: (value) => ["link", "button", "routerLink"].includes(value),
      default: "link", // Default to 'link' for regular link behavior
    },

    type: {
      type: String,
      validator: (value) =>
        ["primary", "secondary", "tertiary"].includes(value),
      default: "primary",
    },

    size: {
      type: String,
      validator: (value) => ["small", "medium", "big"].includes(value),
      default: "medium",
    },

    to: {
      type: String,
    },

    href: {
      type: String,
      default: "#",
    },
  },
  computed: {
    isValidType() {
      return ["primary", "secondary", "tertiary"].includes(this.type);
    },

    typeClasses() {
      return {
        primary: this.type === "primary",
        secondary: this.type === "secondary",
        tertiary: this.type === "tertiary",
      };
    },
    sizeClasses() {
      return {
        small: this.size === "small",
        medium: this.size === "medium",
        big: this.size === "big",
      };
    },
  },
};
</script>
<style lang="scss" scoped>
@import "@/assets/styles/abstracts.scss";

.reset {
  // reset button properties
  display: inline-flex;
  gap: 1rem;
  border: none;
  padding: 0;
  margin: 0;
  outline: none;
  background-color: none;

  // add general formatting
  font-weight: 500;
  letter-spacing: 0.5px;
  border-radius: 0.6rem;

  // animations
  transition: color 0.2s ease-out, background-color 0.2s ease-out;
}

.small {
  font-size: 1.6rem;
  padding: 0.4rem 1.4rem;
}

.medium {
  font-size: 1.8rem;
  padding: 0.6rem 1.6rem;
}

.big {
  font-size: 1.8rem;
  padding: 1rem 2.4rem;
}

.primary {
  color: white;
  background-color: $blue;
  border: 2px solid $blue;

  &:hover {
    color: $blue;
    background-color: white;
  }
}

.secondary {
  color: $blue;
  background-color: rgb(227, 227, 227);

  &.medium {
    padding: 0.8rem 1.6rem;
  }

  &.small {
    padding: 0.6rem 1.4rem;
  }

  &.big {
    padding: 1.2rem 2.4rem;
  }

  &:hover {
    background-color: white;
    border-color: white;
  }
}

.tertiary {
  color: pink;
}
</style>
