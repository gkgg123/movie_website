<template>
<div class="container h-100 mt-5 maindiv">
  <div class="text-dark w-100 h-100 m-0" style="height:100rm;">

    <div class="pt-4">
      <h1 class="text-white font-weight-bold">{{ community.name }}</h1>
      <div class="d-flex justify-content-end px-5">
        <button data-toggle="modal" :data-target="'#Modal'" class="btn btn-outline-primary">글쓰기</button>

      </div>
    </div>
    
    <ArticleCreateModal :communityid="community.id" @createArticle="getArticles(community.id)"/>

    <div id="community" class="container bg-light">
      <div class="row">
        <div class="MenuLeft col-2">
          <p class="mb-4 text-light menu text-center p-1" >커뮤니티 게시판</p>
          <ul class="px-4">
            <li v-for="community in communityList" :key="community.id" class="menu-item" :id="`community${community.id}`" @click="setCommnuity(community)">{{ community.name }}</li>
          </ul>
        </div>

        <div class="px-5 col-10">
          <router-view :community="community" :articles="articles"></router-view>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import ArticleCreateModal from '@/components/communitys/ArticleCreateModal.vue'
import Axios from 'axios'
const BASE_URL = 'http://127.0.0.1:8000/'
const API_URL = BASE_URL+'api/v1/community/'

export default {
  name: 'CommunityView',
  data() {
    return {
      articles: null,
      community: {
        name: '자유게시판',
        id: 1
      },
      communityList: [],
    }
  },
  components: {
    ArticleCreateModal,
  },
  methods: {
    getCommunityList() {
      Axios.get(API_URL)
        .then((res)=>{
          this.communityList = res.data
        })
    },
    getArticles(id) {
      Axios.get(API_URL+id)
        .then((res)=>{
          this.articles = res.data
          this.articles.forEach(element => {
            element.content = element.content.replace(/(\n|\r\n)/g, '<br>');
          });
        })
    },
    setCommnuity(community) {
      this.$router.push({ path:'/community', params: {community}},this.test,this.test)
      this.community = community
      this.getArticles(this.community.id)
    },
    test() {
      console.log('1')
    }
  },
  created() {
    this.getCommunityList()
    this.getArticles(this.community.id)
  }
}

</script>

<style>
  .menu {
    padding-left: 20px;
    background: #163c53;
    color: #fff;
    border-top: 2px solid #008db3;
  }
  .MenuLeft {
    height: 540px;
    background: #10232c;
    padding: 0;
    padding-bottom: 370px;
  }
  .menu-item {
    display: block;
    padding: 0px 0px 0px 10px;
    color: #7a96a7;
    border-bottom: 1px solid #384a56;
    line-height: 30px;
    list-style-type: none;
  }
  /* .communityback{
    background-image: url('../../assets/background.jpg') !important;
    opacity : 0.75;
  } */
</style> 