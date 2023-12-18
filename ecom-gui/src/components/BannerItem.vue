<template>
  <q-carousel arrows animated v-model="slide" height="45rem" autoplay>
    <q-carousel-slide name="first" img-src="../assets/HomeCarousal/1.jpg">
      <div class="absolute-bottom custom-caption">
        <div class="text-h2">Purity</div>
        <div class="text-subtitle1">Made with natural ingredients</div>
      </div>
    </q-carousel-slide>
    <q-carousel-slide name="second" img-src="../assets/HomeCarousal/2.jpg">
      <div class="absolute-bottom custom-caption">
        <div class="text-h2">Elegant</div>
        <div class="text-subtitle1">Best for elegant skin</div>
      </div>
    </q-carousel-slide>
    <q-carousel-slide name="third" img-src="../assets/HomeCarousal/3.jpg">
      <div class="absolute-bottom custom-caption">
        <div class="text-h2">Results</div>
        <div class="text-subtitle1">100% effective</div>
      </div>
    </q-carousel-slide>
    <q-carousel-slide name="fourth" img-src="../assets/HomeCarousal/4.jpg">
      <div class="absolute-bottom custom-caption">
        <div class="text-h2">Made for all</div>
        <div class="text-subtitle1">Made for all type of skins</div>
      </div>
    </q-carousel-slide>
  </q-carousel>
  <!-- <q-banner
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
  </q-banner> -->
</template>

<script setup>
import { computed, ref } from "vue";
import { useStore } from "vuex";
import { useQuasar } from "quasar";
// CONSTANTS
const slide = ref("first");

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
