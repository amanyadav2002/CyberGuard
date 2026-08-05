/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cyber-bg': '#08090a',
        'cyber-accent': '#00f0ff',
        'cyber-accent-dim': 'rgba(0, 240, 255, 0.15)',
        'cyber-danger': '#ff0055',
        'cyber-danger-dim': 'rgba(255, 0, 85, 0.15)',
        'cyber-success': '#00ff66',
        'cyber-success-dim': 'rgba(0, 255, 102, 0.15)',
        'cyber-warning': '#ffaa00',
        'cyber-warning-dim': 'rgba(255, 170, 0, 0.15)',
        'cyber-card': 'rgba(13, 16, 23, 0.65)',
        'cyber-border': 'rgba(0, 240, 255, 0.2)',
        'cyber-border-danger': 'rgba(255, 0, 85, 0.2)',
        'cyber-border-success': 'rgba(0, 255, 102, 0.2)',
      },
      boxShadow: {
        'neon-accent': '0 0 15px rgba(0, 240, 255, 0.25)',
        'neon-accent-strong': '0 0 25px rgba(0, 240, 255, 0.45)',
        'neon-danger': '0 0 15px rgba(255, 0, 85, 0.25)',
        'neon-success': '0 0 15px rgba(0, 255, 102, 0.25)',
        'neon-warning': '0 0 15px rgba(255, 170, 0, 0.25)',
        'glass': '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
      },
      backdropBlur: {
        'cyber': '12px',
      },
      animation: {
        'pulse-glow': 'pulseGlow 2s infinite ease-in-out',
        'scan': 'scanLine 3s infinite linear',
        'grid-move': 'gridMove 20s infinite linear',
      },
      keyframes: {
        pulseGlow: {
          '0%, 100%': { opacity: '0.6', filter: 'drop-shadow(0 0 2px rgba(0, 240, 255, 0.3))' },
          '50%': { opacity: '1', filter: 'drop-shadow(0 0 10px rgba(0, 240, 255, 0.6))' },
        },
        scanLine: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100%)' },
        },
        gridMove: {
          '0%': { backgroundPosition: '0 0' },
          '100%': { backgroundPosition: '40px 40px' },
        }
      }
    },
  },
  plugins: [],
}
