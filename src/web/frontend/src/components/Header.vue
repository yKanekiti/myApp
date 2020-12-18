<template>
  <div>
    <v-navigation-drawer app v-model="drawer" clipped>
      <!-- ナビゲーションメニュー -->
      <v-container>
        <v-list-item>
          <v-list-item-title>{{ navigationTitle }}</v-list-item-title>
        </v-list-item>
        <v-list nav>
          <v-list-item v-for="item in routerLinkList" v-bind:key="item.name">
            <v-list-item-content>
              <v-btn text v-bind:to="item">{{ item.name }}</v-btn>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-container>
    </v-navigation-drawer>
    <!-- ヘッダ -->
    <v-app-bar app color="primary" dark clipped-left>
      <v-app-bar-nav-icon v-on:click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ headerTitle }}</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      headerTitle: "Headerです",
      navigationTitle: "Navigationです",
      drawer: false,
      /* route.jsで設定したパスをここで使う */
      routerLinkList: [ 
        { name: "home", path: "/" },
        { name: "sub", path: "/sub" },
      ],
    };
  },
};
</script>

<style scoped>
</style>
