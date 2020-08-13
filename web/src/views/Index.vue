<template>
  <div>
    <el-row :gutter="10">
      <el-col :xs="8" :sm="12" :md="16" :lg="18" :xl="22">
        <div class="grid-content">
          <el-tabs type="border-card" stretch lazy v-model="tab">
            <el-tab-pane label="知乎" name="zhihu">
              <span slot="label">
                <img
                  src="https://www.zhihu.com/favicon.ico"
                  width="20px"
                  height="20px;"
                  style="vertical-align:middle; margin-bottom:4px;"
                /> 知乎
              </span>
              <el-table
                :data="zhihu_hot_data"
                v-loading="loading"
                empty-text=" "
                :show-header="false"
              >
                <el-table-column>
                  <template slot-scope="slots">
                    <a class="url" :href="slots.row.url">
                      <span>{{ slots.row.title }}</span>
                    </a>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>

            <el-tab-pane label="微博" name="weibo">
              <span slot="label">
                <img
                  src="https://weibo.com/favicon.ico"
                  width="20px"
                  height="20px;"
                  style="vertical-align:middle; margin-bottom:4px;"
                /> 微博
              </span>
              <el-table
                :data="weibo_hot_data"
                v-loading="loading"
                empty-text=" "
                :show-header="false"
              >
                <el-table-column>
                  <template slot-scope="slots">
                    <a class="url" :href="slots.row.url">
                      <span>{{ slots.row.title }}</span>
                    </a>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="V2EX" name="v2ex">
              <span slot="label">
                <img
                  src="https://www.v2ex.com/favicon.ico"
                  width="20px"
                  height="20px;"
                  style="vertical-align:middle; margin-bottom:4px;"
                /> V2EX
              </span>
              <el-table
                :data="v2ex_hot_data"
                v-loading="loading"
                empty-text=" "
                :show-header="false"
              >
                <el-table-column>
                  <template slot-scope="slots">
                    <a class="url" :href="slots.row.url">
                      <span>{{ slots.row.title }}</span>
                    </a>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="吾爱破解" name="52pojie">
              <span slot="label">
                <img
                  src="https://www.52pojie.cn/favicon.ico"
                  width="20px"
                  height="20px;"
                  style="vertical-align:middle; margin-bottom:4px;"
                /> 吾爱破解
              </span>
              <el-table
                :data="pojie52_hot_data"
                v-loading="loading"
                empty-text=" "
                :show-header="false"
              >
                <el-table-column>
                  <template slot-scope="slots">
                    <a class="url" :href="slots.row.url">
                      <span>{{ slots.row.title }}</span>
                    </a>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
export default {
  name: "index",
  data() {
    return {
      tab: "zhihu",
      loading: true,
      zhihu_hot_data: [],
      weibo_hot_data: [],
      v2ex_hot_data: [],
      pojie52_hot_data: [],
    };
  },
  watch: {
    tab: function (val) {
      //监听切换状态-计划单
      this.loading = true;
      if (val == "zhihu") {
        this.zhihu_hot();
      } else if (val == "weibo") {
        this.weibo_hot();
      } else if (val == "v2ex") {
        this.v2ex_hot();
      } else if (val == "52pojie") {
        this.pojie52_hot();
      }
    },
  },
  methods: {
    go(url) {
      window.location.href = url;
    },
    //获取知乎热榜
    zhihu_hot() {
      this.$http.get_zhihu().then((res) => {
        if (res.data.code == 200) {
          this.zhihu_hot_data = res.data.data;
          this.loading = false;
        }
      });
    },
    weibo_hot() {
      this.$http.get_weibo().then((res) => {
        if (res.data.code == 200) {
          this.weibo_hot_data = res.data.data;
          this.loading = false;
        }
      });
    },
    v2ex_hot() {
      this.$http.get_v2ex().then((res) => {
        if (res.data.code == 200) {
          this.v2ex_hot_data = res.data.data;
          this.loading = false;
        }
      });
    },
    pojie52_hot() {
      this.$http.get_52pojie().then((res) => {
        if (res.data.code == 200) {
          this.pojie52_hot_data = res.data.data;
          this.loading = false;
        }
      });
    },
  },
  created() {
    this.zhihu_hot();
  },
};
</script>
<style scoped>
.url {
  font-size: 20px;
  text-decoration: none;
  color: rgb(54, 54, 54);
}
.url:visited {
  color: rgb(153, 154, 153) !important;
}
.el-table td {
  padding: 15px 0px !important;
}
</style>