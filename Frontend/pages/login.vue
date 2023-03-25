<template>
  <div
    class="flex h-screen w-full items-center justify-center bg-stone-300 bg-cover bg-no-repeat"
  >
    <div class="text-black">
      <div class="mb-8 flex flex-col items-center">
        <h1 class="mb-3 text-4xl">ログイン</h1>
        // あとでここにロゴを入れる
        <img src="https:～Logo.wine.svg" width="150" alt="" srcset="" />
      </div>
      <form action="#">
        <div class="mb-4 text-lg">
          <input
            v-model="user.userId"
            class="rounded-4xl border-none bg-white-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md"
            type="text"
            name="name"
            placeholder="Email or Username"
          />
        </div>
        <div class="mb-4 text-lg">
          <input
            v-model="user.password"
            class="rounded-4xl border-none bg-white-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md"
            type="Password"
            name="name"
            placeholder="Password"
          />
          <br />
          <a href="" class="text-sm text-rigth font-semibold text-blue-500"
            >Forgot Password?</a
          >
        </div>
        <div class="mt-8 flex justify-center text-lg text-black">
          <button
            type="submit"
            class="rounded-4xl bg-gray-900 bg-opacity-50 px-10 py-2 text-white shadow-xl backdrop-blur-md transition duration-200 rounded-lg duration-300 hover:bg-gray-800"
          >
            Login
          </button>
        </div>
        <div>
          <a>Don't have an account?</a>
          <a href="" class="text-sm text-rigth font-semibold text-blue-500"
            >Sing up</a
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        user: {},
      };
    },
    methods: {
      doLogin() {
        this.$store.dispatch('auth', {
          userId: this.user.userId,
          userToken: 'dummy token',
        });
        this.$router.push(this.$route.query.redirect);
      },
    },
  };
</script>
