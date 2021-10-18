<template>
  <div>
    <el-menu router mode="horizontal" active-text-color="red">
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
      </el-menu-item>
      <span style="position: absolute;padding-top: 20px;right: 43%;font-size: 20px;font-weight: bold">BlueJade -- Second Hand First Choice</span>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "NavMenu",
  data () {
    return {
      navList: [
        {name: '/index', navItem: 'text1'},
        {name: '/define', navItem: 'text2'},
        {name: '/define', navItem: 'text3'},
        {name: '/login', navItem: 'personal'}
      ],
      keywords: ''
    }
  },
}
</script>

<style scoped>
@import "../../styles/bg.css";
.el-menu {
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
