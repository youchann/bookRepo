export const Mixin = {
  created: function () {
    this.setStyle();
    this.setName();
  },
  methods: {
    setStyle() {
      this.style = "font-size:30px; color: red;";
    },
    setName() {
      this.name = "Mixin Test";
    }
  }
};

