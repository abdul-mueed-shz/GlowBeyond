<template>
  <q-banner
    class="bg-primary text-white text-center row"
    style="min-height: 32rem"
  >
    <div class="col-6">
      <div :class="headerClass" class="q-mb-lg">
        {{ MAP.HOMEPAGE.GREETINGS.HEADING }}
      </div>
      <div :class="bodyClass">
        {{ MAP.HOMEPAGE.GREETINGS.BODY }}
      </div>
    </div>
  </q-banner>
</template>

<script setup>
import { computed, ref } from "vue";
import { useStore } from "vuex";
import { useQuasar } from "quasar";
// CONSTANTS

const $store = useStore();
const $q = useQuasar();
// COMPUTED PROPERTIES
const headerClass = computed(() => {
  return $q.screen.width > 700 ? " text-h2 " : " text-h4";
});
const bodyClass = computed(() => {
  return $q.screen.width > 700 ? " text-h4 " : " text-h5";
});

const MAP = computed(() => {
  return $store.getters["app/getMAP"];
});
const miniState = computed(() => {
  return $store.getters["app/getMiniState"];
});
</script>
