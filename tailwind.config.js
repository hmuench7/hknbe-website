/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',  // Django templates
    './static/**/*.js',       // JavaScript files
  ],
  theme: {
    extend: {
      colors: {
        primary: '#007BFF',  // IEEE-HKN blue
        secondary: '#6C757D', // Gray
      },
    },
  },
  plugins: [],
};


