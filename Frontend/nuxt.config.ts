import svgLoader from 'vite-svg-loader';
export default defineNuxtConfig({
  postcss: {
    plugins: { tailwindcss: {} },
  },
  css: ['~/css/tailwind.css'],
  modules: ['@nuxtjs/tailwindcss'],
  vite: {
    plugins: [
      svgLoader({
        svgo: false,
      }),
    ],
  },
});
