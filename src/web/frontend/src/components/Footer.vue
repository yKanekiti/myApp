<template>
  <v-footer app>
    <v-card-title>
      <div>{{ footerTitle }}</div>
    </v-card-title>
  </v-footer>
</template>

<script>
export default {
  data: function () {
    return {
      footerTitle: "Footerです",
    };
  },
};
</script>

<style scoped>
</style>