<template>
  <q-list>
    <menu-item v-if="!item.subMenu" :item="item"> </menu-item>
    <q-expansion-item
      v-else-if="!props.miniState"
      :icon="item.icon.name"
      :label="item.label"
      class="q-ml-sm text-weight-medium"
    >
      <menu-item
        v-for="expansionItem in item.subMenu"
        :key="expansionItem.name"
        :item="expansionItem"
      ></menu-item>
    </q-expansion-item>
    <menu-item
      v-else
      v-for="subItem in item.subMenu"
      :key="subItem.name"
      :item="subItem"
    ></menu-item>
  </q-list>
</template>

<script setup>
import MenuItem from "./MenuItem.vue";
import { computed } from "vue";

const props = defineProps({
  item: {
    type: Object,
    required: true,
  },
  miniState: {
    type: Boolean,
    required: true,
  },
});

// Computed Properties
const item = computed(() => {
  return props.item;
});
</script>
