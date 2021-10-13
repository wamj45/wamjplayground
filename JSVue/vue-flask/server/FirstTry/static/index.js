var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Whasts up!',
        description: 'How you doin? (Thiss be the description)',
        link: "https://www.microcenter.com/",
        site: "Microcenter",
        cond: 135,
        arrPlayers: ["Hopkins", "Williams", "Mahomes", "Allen"]
    }
});


var app5 = new Vue({
        el: "#app-5",
        delimiters: ['[[', ']]'],
        data: {
          message: "wuriuce"
        },
        methods: {
          reverseMessage: function () {
            this.message = this.message.split("").reverse().join("");
          }
        }
      });
