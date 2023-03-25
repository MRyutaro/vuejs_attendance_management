<template>
  <h3>ログイン成功 {{ $store.state.userId }}</h3>
</template>
<script>
  export default {
    data() {
      return {
        message: '',
      };
    },
    created: function () {
      this.fetchLoginok();
    },
    methods: {
      fetchLoginok() {
        const uri = 'http://localhost:3000/loginok';
        this.axios.get(uri).then((response) => {
          this.message = response.data.message;
        });
      },
    },
  };
</script>
