<template>
  <v-app>
    <Header></Header>
    <Content></Content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Content from "./components/Content";
export default {
  name: "App",
  components: {
    Header,
    Content,
    Footer,
  },
};
</script>
