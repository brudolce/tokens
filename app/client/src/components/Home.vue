<template>
  <div>
    <div class="head">
      <div>
      <b-form-input v-model="text" placeholder="Enter the term you are looking for"></b-form-input>
      <b-button
        type="submit"
        variant="primary"
        @click='gettokens()'
        >
        Go!
        </b-button>
        </div>
    </div>
    <div class="pictures">
      <img  width='1240.5px' height='1754.5px' v-for='(value,index) in pictures' :src='value' :alt='index' :key='index'>
    </div>
    <div v-if='highlights'>
      <div class='highlight'
            v-for='(element,index) in highlights'
            :key='index'
            v-bind:style="{ 'left': element.x1/2  + 'px', 'width': ((element.x2 - element.x1)/2) + 'px', 'top': (element.y2/2) + ((element.page-1)*1754.5) + 50 + 'px', 'height': ((element.y1 - element.y2)/2) + 'px' }"
          >
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      text: '',
      tokens: '',
      pictures: Array.from({ length: 11 }, (_, index) => 'http://localhost:5000/api/image/' + (1 + index)),
      highlights: false
    }
  },
  methods: {
    gettokens () {
      axios
        .get(`http://localhost:5000/api/tokens/${this.text}`)
        .then((res) => {
          this.tokens = res.data.tokens
          // reactive data
          this.highlights = Object.values(this.tokens)
          console.log(res, 'highlights', this.highlights)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    }
  }
}
</script>

<style>
.head {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
}
.pictures {
  display: flex;
  flex-direction: column
}
.head > div {
  display: flex;
  width: 30vw
}
.highlight{
  position:absolute;
  background-color: yellow;
  opacity: 0.4;
}

</style>
