<template>
  <q-carousel arrows animated v-model="slide" height="45rem" autoplay infinite>
    <q-carousel-slide
      v-for="bannerItem in bannerItems"
      :key="bannerItem.heading"
      :name="bannerItem.heading"
      :img-src="bannerItem.image"
    >
      <div class="absolute-bottom custom-caption">
        <div class="text-h2">{{ bannerItem.heading }}</div>
        <div class="text-subtitle1">{{ bannerItem.caption }}</div>
      </div>
    </q-carousel-slide>
  </q-carousel>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
import img1 from "../assets/HomeCarousal/1.jpg";
import img2 from "../assets/HomeCarousal/2.jpg";
import img3 from "../assets/HomeCarousal/3.jpg";
import img4 from "../assets/HomeCarousal/4.jpg";

// CONSTANTS
const slide = ref("Purity");

const defaults = [
  {
    heading: "Purity",
    caption: "Made with natural ingredients",
    image: img1,
  },
  {
    heading: "Elegant",
    caption: "Best for elegant skin",
    image: img2,
  },
  {
    heading: "Results",
    caption: "100% effective",
    image: img3,
  },
  {
    heading: "Made for all",
    caption: "Made for all type of skins",
    image: img4,
  },
];

const store = useStore();
// COMPUTED PROPERTIES

const MAP = computed(() => {
  return store.getters["app/getMAP"];
});

const bannerItems = computed(() => {
  const items = store.getters["appinfo/getBannerItems"];
  return items.length ? items : defaults;
});

async function setBannerItems() {
  try {
    await store.dispatch("appinfo/setBannerItems");
    if (bannerItems.value.length > 0) {
      slide.value = bannerItems.value[0]?.heading;
    }
  } catch (err) {
    console.error(err);
  }
}

onMounted(() => {
  setBannerItems();
});
</script>
