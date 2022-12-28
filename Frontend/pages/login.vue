<template>
<div class="flex h-screen w-full items-center justify-center bg-gray-300 bg-cover bg-no-repeat" style="background-image:url('')">
    <div class="text-black">
      <div class="mb-8 flex flex-col items-center">
        <h1 class="mb-3 text-4xl">ログイン</h1>
        // あとでここにロゴを入れる
        <img src="https:～Logo.wine.svg" width="150" alt="" srcset="" />
      </div>
      <form action="#">
        <div class="mb-4 text-lg">
          <input class="rounded-4xl border-none bg-white-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md" type="text" name="name" placeholder="email" />
        </div>
        <div class="mb-4 text-lg">
          <input class="rounded-4xl border-none bg-white-400 bg-opacity-50 px-6 py-2 text-center text-inherit placeholder-slate-200 shadow-lg outline-none backdrop-blur-md" type="Password" name="name" placeholder="password" />
        </div>
        <div class="mt-8 flex justify-center text-lg text-black">
          <button type="submit" class="rounded-4xl bg-black-600 bg-opacity-50 px-10 py-2 text-white shadow-xl backdrop-blur-md transition-colors duration-300 hover:bg-gray-600">Login</button>
        </div>
      </form>
    </div>
  </div>

</template>