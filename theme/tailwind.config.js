module.exports = {

  content: [
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    './static/**/*.js',
  ],
  darkMode: 'class',
  theme: {

    extend: {
        fontFamily: {
      agbalumo: ['Agbalumo', 'sans-serif'],
    },


    },
  },
  plugins: [
      require('tailwindcss-animate'),
      require('daisyui'),
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),


  ],

  daisyui: {
    themes: true,
  }
}

