<script lang="ts" setup>
import {ref} from "vue";
// vue组件
import {
  Search,
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

const errorHandler = () => true
const select_movie = ref('')
const select_model = ref('')
const your_comment = ref('')
const radio1 = ref('')
const radio2 = ref('')
const radio3 = ref('')
// 登录
const dialogVisible = ref(false)
// 内容显示结果
const zhuye_button = ref(true)
const gaofendianyin_button = ref(false)
const shoucang_button = ref(false)
const gerenxinxishezhi_button = ref(false)
const sousuojieguo_button = ref(false)
// 头像栏展示
const denglu_button = ref(false)
//主页标签
const label1 = ref('')
const label2 = ref('')
const label3 = ref('')
//评论
const pinglun_dianyin = ref('')
//电影信息展示
const movie_imformation = ref({
  name: '功夫',
  year: '2004',
  rating: 2,
  rating_sum: '382137',
  tags: '1',
  genre: '2',
  country: '3',
})

import {reactive} from "vue";
import API from "./assets/axiosInstance";
export default {
  name: 'About',
  setup(){
    const  testData = reactive({
      list:[]
    });

    const  getData = function (){
      API({
        url:'/test',
        method:'get'
      }).then((res)=>{
        alert('success!');
        testData.list = res.data.datalist;
      });
    }
    return{
      testData,
      getData,
    }
  }
}

</script>


<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="getData()">test axios 请求数据</button>
    <p>这是请求到的数据{{testData.list}}</p>
  </div>
  <el-row v-if="false">
    <el-container>
      <!--头部-->
      <el-header>
        <el-row>
          <!--网站图标-->
          <el-col :span="4">
            <div class="project-image-div">
              <div class="project-name">
                <img src="./assets/image/project-img.png" style="height: 30px; width: 170px; margin-left: 40px">
              </div>
            </div>
          </el-col>
          <!--搜索框-->
          <el-col :span="8">
            <div class="mt-4">
              <el-input
                  v-model="select_movie"
                  placeholder="搜索你想要的电影"
                  class="input-with-select"
                  show-word-limit
                  type="text"
                  maxlength="400"
                  clearable
              >
                <template #prepend>
                  <el-button :icon="Search" @click="sousuojieguo_button = true"/>
                </template>
                <template #append>
                  <el-select v-model="select_model" placeholder="搜索模式" style="width: 115px" clearable>
                    <el-option label="关键词搜索" value="1"/>
                    <el-option label="智能搜索" value="2"/>
                  </el-select>
                </template>
              </el-input>
            </div>
          </el-col>
          <!--不知道放啥-->
          <el-col :span="8">

          </el-col>
          <!--头像-->
          <el-col :span="4">
            <!--登录-->
            <div class="block" v-if="!denglu_button">
              <el-button text @click="dialogVisible = true">
                登录
              </el-button>
              <el-dialog v-model="dialogVisible" title="登录/注册" width="20%" draggable>
                <el-input v-model="input1" placeholder="请输入账号">
                  <template #prepend>账号</template>
                </el-input>
                <br><br>
                <el-input v-model="input1" placeholder="请输入密码">
                  <template #prepend>密码</template>
                </el-input>
                <template #footer>
                  <span class="dialog-footer">
                    <el-button @click="dialogVisible = false" style="float: left">注册</el-button>
                    <el-button @click="dialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="dialogVisible = false">
                      登录
                    </el-button>
                  </span>
                </template>
              </el-dialog>
            </div>
            <!--用户头像-->
            <div class="block" v-if="denglu_button">
              <el-avatar :size="50"
                         src="https://ts4.cn.mm.bing.net/th?id=OIP-C.wfCatXgWL85ztJ9TFoWjrAHaFj&w=288&h=216&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
                         @error="errorHandler">
                <img src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png"/>
              </el-avatar>
              <div class="user-name">
                <p>江</p>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-container>
        <!--功能栏-->
        <el-aside width="200px">
          <el-menu
              class="el-menu-vertical-demo"
              default-active="2"
          >
            <!--1-->
            <el-menu-item index="2"
                          @click="zhuye_button = true; gaofendianyin_button = false; shoucang_button = false; gerenxinxishezhi_button = false; sousuojieguo_button = false">
              <el-icon>
                <location/>
              </el-icon>
              <span>主页</span>
            </el-menu-item>
            <!--2-->
            <el-menu-item index="1"
                          @click="zhuye_button = false; gaofendianyin_button = true; shoucang_button = false; gerenxinxishezhi_button = false; sousuojieguo_button = false">
              <el-icon>
                <icon-menu/>
              </el-icon>
              <span>高分电影推荐</span>
            </el-menu-item>
            <!--3-->
            <el-menu-item index="3"
                          @click="zhuye_button = false; gaofendianyin_button = false; shoucang_button = true; gerenxinxishezhi_button = false; sousuojieguo_button = false">
              <el-icon>
                <document/>
              </el-icon>
              <span>收藏</span>
            </el-menu-item>
            <!--4-->
            <el-menu-item index="4"
                          @click="zhuye_button = false; gaofendianyin_button = false; shoucang_button = false; gerenxinxishezhi_button = true; sousuojieguo_button = false">
              <el-icon>
                <setting/>
              </el-icon>
              <span>个人信息设置</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-container>
          <!--中间-->
          <el-main>
            <!--搜索结果-->
            <diV v-if="sousuojieguo_button">
              <el-scrollbar max-height="800px">
                <el-space wrap>
                  <el-card v-for="i in 1" :key="i" class="box-card" style="width: 220px">
                    <template #header>
                      <div class="card-header">
                        <span>|</span>
                        <el-button class="button" text>详情</el-button>
                      </div>
                    </template>
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2219011938.webp"
                         style="width: 100%">
                    <div class="text item">
                      功夫
                    </div>
                    <div class="text item"
                         style="font-size: 13px;overflow: hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;">
                      1940年代的上海，自小受尽欺辱的街头混混阿星（周星驰）为了能出人头地，可谓窥见机会的缝隙就往里钻，今次他盯上行动日益猖獗的黑道势力“斧头帮”，想借之大名成就大业。阿星假冒“斧头帮”成员试图在一个叫“猪笼城寨”的地方对居民敲诈，不想引来真的“斧头帮”与“猪笼城寨”居民的恩怨。“猪笼城寨”原是藏龙卧虎之处，居民中有许多身怀绝技者（元华、梁小龙等），他们隐藏于此本是为远离江湖恩怨，不想麻烦自动上身，躲都躲不及。而在观战正邪两派的斗争中，阿星逐渐领悟功夫的真谛。
                    </div>
                  </el-card>
                </el-space>
              </el-scrollbar>
            </diV>
            <!--主页-->
            <div v-else-if="zhuye_button">
              <el-carousel :interval="4000" type="card" height="200px" style="margin-left: 7.5%;width: 85%">
                <el-carousel-item v-for="item in 6" :key="item">
                  <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p692813374.webp">
                </el-carousel-item>
              </el-carousel>
              <div style="margin-left: 7.5%;width: 85%">
                <el-radio-group v-model="radio1" size="large">
                  <el-radio-button label="标签" disabled/>
                  <el-radio-button label="热血"/>
                  <el-radio-button label="动作"/>
                  <el-radio-button label="喜剧"/>
                </el-radio-group>
                <br>
                <el-radio-group v-model="radio2" size="large">
                  <el-radio-button label="时间" disabled/>
                  <el-radio-button label="2022"/>
                  <el-radio-button label="2021"/>
                  <el-radio-button label="2020"/>
                </el-radio-group>
                <br>
                <el-radio-group v-model="radio3" size="large">
                  <el-radio-button label="字母" disabled/>
                  <el-radio-button label="A"/>
                  <el-radio-button label="B"/>
                  <el-radio-button label="C"/>
                  <el-radio-button label="D"/>
                  <el-radio-button label="E"/>
                  <el-radio-button label="F"/>
                  <el-radio-button label="G"/>
                  <el-radio-button label="H"/>
                  <el-radio-button label="I"/>
                  <el-radio-button label="J"/>
                  <el-radio-button label="K"/>
                  <el-radio-button label="L"/>
                  <el-radio-button label="M"/>
                  <el-radio-button label="N"/>
                  <el-radio-button label="O"/>
                  <el-radio-button label="P"/>
                  <el-radio-button label="Q"/>
                  <el-radio-button label="R"/>
                  <el-radio-button label="S"/>
                  <el-radio-button label="T"/>
                  <el-radio-button label="U"/>
                  <el-radio-button label="V"/>
                  <el-radio-button label="W"/>
                  <el-radio-button label="X"/>
                  <el-radio-button label="Y"/>
                  <el-radio-button label="Z"/>
                </el-radio-group>
                <!--显示内容-->
                <el-scrollbar max-height="425px">
                  <el-space wrap>
                    <el-card v-for="i in 100" :key="i" class="box-card" style="width: 200px; height: 265px">
                      <button style="margin: -25px">
                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2219011938.webp"
                             style="width: 100%">
                      </button>
                    </el-card>
                  </el-space>
                </el-scrollbar>
              </div>
            </div>
            <!--高分电影随机推荐-->
            <div v-else-if="gaofendianyin_button" style="margin-left: 7.5%;width: 85%;margin-top: 5%;height: 91.5%">
              <!--信息展示区-->
              <div style="height: 40%;display: flex;flex-direction: row;">
                <div style="width: 203px">
                  <el-image style="width: 203px; height: 293px"
                            src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2219011938.webp"
                            :fit="'fill'"/>
                </div>
                <div>
                  <el-descriptions class="margin-top" title='功夫' :column="1" border>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">得分</div>
                      </template>
                      <el-rate
                          v-model='movie_imformation.rating'
                          disabled
                          text-color="#ff9900"
                      />
                    </el-descriptions-item>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">年份</div>
                      </template>
                      {{ movie_imformation.year }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">评论人数</div>
                      </template>
                      {{ movie_imformation.rating_sum }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">标签</div>
                      </template>
                      {{ movie_imformation.tags }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">类型</div>
                      </template>
                      {{ movie_imformation.genre }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                      <template #label>
                        <div class="cell-item">地区</div>
                      </template>
                      {{ movie_imformation.country }}
                    </el-descriptions-item>
                  </el-descriptions>
                </div>
              </div>
              <!--评论区-->
              <div style="height: 60%">
                <el-space :fill="true" wrap style="width: 100%;height: 100%">
                  <el-card class="box-card">
                    <template #header>
                      <div class="card-header">
                        <span style="margin-right: 60%">评论区</span>
                        <el-button class="button" text>好评区</el-button>
                        <el-button class="button" text>差评区</el-button>
                        <el-button class="button" text>影人评论</el-button>
                        <el-button class="button" text>电影评论</el-button>
                      </div>
                    </template>
                    <div style="height: 330px">
                      <ul zclass="infinite-list" style="overflow: auto">
                        <li v-for="i in count" :key="i"
                            clzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzass="infinite-list-item">
                          {{ i }}
                        </li>
                      </ul>
                    </div>
                  </el-card>
                </el-space>
              </div>
            </div>
            <!--收藏-->
            <div v-else-if="shoucang_button" style="margin-left: 7.5%;width: 85%">

            </div>
            <!--个人信息设置-->
            <div v-else-if="gerenxinxishezhi_button" style="margin-left: 7.5%;width: 85%">

            </div>
          </el-main>
          <!--评论-->
          <el-footer style="height: 100px">
            <el-input
                v-model="your_comment"
                maxlength="200"
                placeholder="留下你的评论吧！"
                show-word-limit
                type="textarea"
                style="height: 70px"
            />
            <el-button type="primary" style="height: 30px;float: right">发表评论</el-button>
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </el-row>
</template>

<style>
html, body {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}
</style>

<style scoped>
.el-header {
  padding: 0;
}

.el-row {
  height: 100%;
  width: 100%;
}

.el-main {
  padding: 0;
}

.block {
  flex: 1;
  display: flex;
  flex-direction: row;
  flex-grow: 0;
  margin-top: 5px;
  margin-left: 5px;
}

:deep(.el-col) {
  height: 100%;
}

.mt-4 {
  margin-top: 13px;
}

.user-name {
  display: flex;
  align-items: center;
  margin-left: 10px;
}


.project-image-div {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}

:deep(.el-textarea__inner) {
  height: 100px;
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

:deep(.el-radio-button__inner) {
  border: 0;
}

</style>
