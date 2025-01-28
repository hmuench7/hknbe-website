/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#007BFF',  // IEEE-HKN blue
        secondary: '#6C757D', // Gray
      },
    },
  },
  darkMode: 'class', // Ensure this line is set
  plugins: [],
}
