module.exports = {
  content: [
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    './static/**/*.js',
  ],

  theme: {

    extend: {
        fontFamily: {
      agbalumo: ['Agbalumo', 'sans-serif'],
    },
    backgroundImage: {
        'grid-pattern': `
          linear-gradient(rgba(0, 0, 0, 0.1) 1px, transparent 1px),
          linear-gradient(90deg, rgba(0, 0, 0, 0.1) 1px, transparent 1px)
        `,
      },
      backgroundSize: {
        'grid-size': '20px 20px',
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

