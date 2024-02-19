<script lang="ts" setup>

</script>
<template>


<router-view id="router_view" />
</template>


<style>
#router_view {
    width: 100%;
    min-height: 100%;
    height: fit-content;
    background-color: #E8EBF1;
}

body,
html {
    width: 100%;
    height: 100%;
    margin: 0px;
}
*{
    margin: 0px;
    padding: 0px;
}
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    font-family: "Cairo", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c2c2c;
    width: 100%;
    height: 100%;
}
</style>