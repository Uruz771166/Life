/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Domain colors
        'domain-self': '#9B59B6',
        'domain-relationships': '#E74C3C',
        'domain-work': '#F39C12',
        'domain-resources': '#27AE60',
        'domain-health': '#3498DB',
        'domain-environment': '#1ABC9C',
        'domain-meaning': '#8E44AD',
        // Spiral colors
        'spiral-beige': '#F5DEB3',
        'spiral-purple': '#800080',
        'spiral-red': '#FF0000',
        'spiral-blue': '#0000FF',
        'spiral-orange': '#FFA500',
        'spiral-green': '#008000',
        'spiral-yellow': '#FFFF00',
        'spiral-turquoise': '#40E0D0',
      },
    },
  },
  plugins: [],
}
