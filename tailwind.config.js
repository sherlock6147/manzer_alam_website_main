/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./manzer_alam_main_website/**/*.{html,js}"],
  theme: {extend: {
    fontFamily: {
      'ubuntu-mono': ["'Ubuntu Mono'",'mono','sans-serif'],
      'gugi': ["'Gugi'",'mono','sans-serif'],
      'raleway': ["'Raleway'",'sans-serif'],
    }
  },
  },
  plugins: [],
}
