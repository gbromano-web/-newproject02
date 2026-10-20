/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{html,js}'],
  theme: {
        extend: {
          colors: {
            // Monochrome palette taken from the RND Athlete logo
            ink: '#000000',       // Logo black — page background
            carbon: '#111111',    // Cards, nav, raised surfaces
            graphite: '#262626',  // Borders, dividers
            steel: '#5C5C5C',     // Disabled, inactive
            smoke: '#A3A3A3',     // Secondary text
            chalk: '#E6E6E6',     // Hover state for white buttons
            // white (#FFFFFF) = logo white — headlines, primary actions
            signal: '#FF3B30',    // Functional only: errors and low stock
          },
          fontFamily: {
            display: ['Archivo', 'Arial Black', 'sans-serif'],
            sans: ['Inter', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
          },
          keyframes: {
            speed: { '0%': { transform: 'translateX(-100%)' }, '100%': { transform: 'translateX(100%)' } },
            rise:  { '0%': { opacity: 0, transform: 'translateY(24px)' }, '100%': { opacity: 1, transform: 'translateY(0)' } },
          },
          animation: {
            speed: 'speed 3.2s linear infinite',
            rise: 'rise .7s cubic-bezier(.2,.7,.2,1) both',
          },
        },
      },
};
