/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {
      colors:{
        Red: "#fc4f57",
        Black:"#070600",
        Whitish: "#F7F7FF",
        Darkish:"#385a64",
        Blue:"#279AF1",
        DarkGreenish:"#012009a4",
        DeepDarkBlue: '#090120a4',
        Grayish: '#e1e1e1',
        Dark:'#10262c',
        Green: 'rgb(35, 236, 35)'
      }
    },
  },
  plugins: [],
}
