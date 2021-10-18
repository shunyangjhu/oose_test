<template>
  <div class="bg">
    <el-container class="container">
      <el-main>
    <el-row style="height: auto;">
      <!--<search-bar></search-bar>-->
      <el-tooltip effect="dark" placement="right"
                  v-for="item in commodities"
                  :key="item.commodityId">
        <p slot="content" style="font-size: 14px;margin-bottom: 6px;">{{item.commodityName}}</p>
        <p slot="content" style="font-size: 13px;margin-bottom: 6px">
          <span>{{item.seller}}</span> /
          <span>{{item.postDate}}</span> /
          <span>{{item.location}}</span> /
          <span v-if="item.forSale ==='True'">For Sale</span>
          <span v-else>Free</span>
        </p>
        <p slot="content" style="width: auto; max-width: 300px;" class="brief">{{item.brief}}</p>

        <el-card class="commodityItem"
                 bodyStyle="padding:10px" shadow="hover">
          <div class="cover">
            <a :href="'commodityItem/'+item.commodityId"><img :src="item.cover" alt="Item Picture"></a>
          </div>
          <div class="info">
            <div class="title">
              <a :href="'commodityItem/'+item.commodityId">{{item.commodityName}}</a>
            </div>
            <div class="title">
              <a class="seller" :href="'community/'+item.sellerId">{{item.seller}}</a>
            </div>
            <div class="title">
              <a class="seller" v-if="item.forSale ==='True'">For Sale</a>
              <a class="seller" v-else>Free</a>
            </div>
            <div class="title">
              <a class="seller">{{ item.location }}</a>
            </div>
            <div class="title">
              <a class="seller" v-bind:href="'contact/' + item.sellerId">Contact me <i class="far fa-comment" /></a>
            </div>
          </div>
<!--          <a class="seller" href="">{{item.seller}}</a>-->
<!--          <a class="seller" v-bind:href="'contact/' + item.id">Contact the seller</a>-->
        </el-card>
      </el-tooltip>
    </el-row>

    <el-row style="background-color: #444;">
      <el-pagination
          :current-page="1"
          :page-size="10"
          :total="20">
      </el-pagination>
    </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: 'CommodityListPage',
  data () {
    return {
      commodities: [
        {
          commodityId: 1,
          cover: 'https://awofficefurniture.com/wp-content/uploads/2019/01/Pre-Owned-Immaculate-Condition-Herman-Miller-Aeron-B-Version-2.png',
          commodityName: 'Office Chair',
          seller: 'David W.',
          sellerId: '56',
          postDate: '2021-10-01',
          forSale: 'True',
          location: 'JHU Homewood Campus',
          brief: 'This is a used office chair just been used for 3 months. I am getting an new chair so I am giving away this for $20.'
        },
        {
          commodityId: 2,
          cover: 'https://5.imimg.com/data5/EF/OI/MY-26227500/hp-laptops-500x500.jpg',
          commodityName: 'Computer Monitor',
          seller: 'Alex T.',
          sellerId: '23',
          postDate: '2021-9-17',
          forSale: 'False',
          location: 'JHU Homewood Campus',
          brief: 'This is a used Dell computer monitor, it has been used for 3 years. ' +
              'I am moving out and I do not want it anymore, so I am giving away this for free. You just need to pick it up at campus.'
        },
        {
          commodityId: 3,
          cover: 'https://image.made-in-china.com/44f3j00GtkUIalcVHoK/Modern-Fashion-Design-Round-Table-Lamp-14W-3-' +
              'Light-Color-Settings-10-Levels-of-Dimming-Brightness-Acrylic-Craft-Black-Used-in-Bedroom-Living-Room-Desk-Office.jpg',
          commodityName: 'Lamp',
          seller: 'Pin H.',
          sellerId: '99',
          postDate: '2021-08-30',
          forSale: 'False',
          location: 'JHU Homewood Campus / DC',
          brief: 'This is a used lamp which has been used for 2 years. I am giving away this for free.'
        },

      ],
       test: [],
    }
  },
  //in dev
  // created() {
  //   axios.get('')
  //       .then((response) => {
  //         console.log(response.data)
  //         this.test = response.data
  //       })
  //       .catch(error => {
  //         console.log(error)
  //       })
  // },
  methods() {
    //in dev
  },
  mounted() {
    let fontAwesomeScript = document.createElement('script')
    fontAwesomeScript.setAttribute('src', 'https://kit.fontawesome.com/fc49f22fc9.js')
    fontAwesomeScript.setAttribute('crossorigin', 'anonymous')
    document.head.appendChild(fontAwesomeScript)
  }
}
</script>

<style scoped>
 @import "../../styles/bg.css";
.commodityItem{
  width: 235px;
  margin-bottom: 20px;
  margin-right: 15px;
  height: 308px;
  float: left;
  text-align: center;
}

.cover {
  width: 200px;
  height: 200px;
  margin-bottom: 7px;
  overflow: hidden;
  cursor: pointer;
}

img {
  width: 100%;
  height: 100%;
  /*margin: 0 auto;*/
}

.title {
  font-size: 14px;
  /*text-align: left;*/
}

.seller {
  color: #333;
  width: 102px;
  font-size: 13px;
  margin-bottom: 6px;
  /*text-align: left;*/
}

.brief {
  display: block;
  line-height: 17px;
}

a {
  text-decoration: none;
}

a:link, a:visited, a:focus {
  color: #3377aa;
}
</style>

