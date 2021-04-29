<template>
  <div id="app">
    <!-- 面包屑区域 -->
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>模板管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/templateList' }">模板列表</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/documentList' }">文档管理</el-breadcrumb-item>
        <el-breadcrumb-item>{{ chosenDocument.document_name }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 主体区域 -->
    <el-card class="box-card">
      <!-- v-model="" -->
      <el-tabs tab-position="top" style="overflow: auto;">
        <!-- 文档基本信息编辑区域 -->
        <el-tab-pane label="需求文档基本信息编辑" name="0" v-loading="loadingTag">
          <el-form v-bind:model="chosenDocument" label-width="auto">
            <el-form-item label="文档名称">
              <el-col :span="11">
                <el-input v-model="chosenDocument.document_name"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="所属模板">
              <el-col :span="11">
                <el-input v-model="chosenDocument.template_name" :disabled="true"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="文档简介">
              <el-col :span="11">
                <el-input type="textarea" v-model="chosenDocument.introduction" autosize></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="最后修改时间">
              <el-col :span="11">
                <el-input v-model="chosenDocument.last_time" :disabled="true"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="用户需求数据集列表">
              <div v-if="chosenDocument.comments_file_list.length <= 0">暂无数据</div>
              <el-tag v-for="(fileName, i) in chosenDocument.comments_file_list" :key="(fileName, i)" closable @close="deleteCommentsFile(fileName, i)">{{fileName}}</el-tag>
              <!-- <el-col :span="11">
                <template>
                  <el-table :data="chosenDocument.comments_file_list"
                    max-height="400">
                    <el-table-column></el-table-column>
                    <el-table-column fixed="right">
                      <el-button @click.native.prevent="deleteRow(scope.$index, tableData)"
                        type="text" size="small">
                        移除
                      </el-button>
                    </el-table-column>
                  </el-table>
                </template>
              </el-col> -->
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="editDocument()">提交更改</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <!-- 文档内容编辑 -->
        <el-tab-pane label="文档内容编辑" name="1" v-loading="loadingTag">
          <el-row :gutter="20" style="margin-bottom: 20px;">
            <el-col :span="6">
              <div><span style="color: black;">目录</span></div>
            </el-col>
            <el-col :span="18"></el-col>
          </el-row>
          <el-row :gutter="20">
            <!-- 文档目录区 -->
            <el-col :span="6">
              <el-tag :key="(line, i)" v-for="(line, i) in chosenDocument.outline" closable
               @click="outlintIndex = i" effect="plain" @close="deleteOutline(line, i)">
              {{ line }}
              </el-tag>
            </el-col>
            <el-col :span="10">
              <el-form label-width="auto" v-if="outlintIndex >= 0">
                <el-form-item label="大纲">
                  <el-input v-model="chosenDocument.outline[outlintIndex]"></el-input>
                </el-form-item>
                <el-form-item label="内容">
                  <el-input v-model="chosenDocument.contents[outlintIndex]" type="textarea" :autosize="{minRows: 5,maxRows: 10}"></el-input>
                </el-form-item>
                <el-form-item label="">
                  <el-button type="primary" @click="editDocument()">提交更改</el-button>
                </el-form-item>
              </el-form>
            </el-col>
            <!-- 需求表格区 -->
            <!-- <el-col :span="18"> -->
              <!-- 加key是为了刷新子页面 -->
              <!-- https://segmentfault.com/q/1010000015992883 -->
              <!-- https://blog.csdn.net/u010176097/article/details/81252417 -->
              <!-- <router-view :key="$route.fullPath" @fresh="fresh"></router-view> -->
            <!-- </el-col> -->
          </el-row>
        </el-tab-pane>
        <!-- 用户需求分析区域 -->
        <el-tab-pane label="用户反馈管理和分析" name="2" v-loading="loadingTag">
          <!-- 用户需求文件下拉列表 -->
          <!-- 选择一个用户需求 -->
          <el-row :gutter="20">
            <el-col :span="6">
              <el-select v-model="comments_file_name" clearable filterable placeholder="请选择一个用户需求数据集">
                <el-option
                 v-for="comments in chosenDocument.comments_file_list"
                 :key="comments"
                 :label="comments"
                 :value="comments">
                </el-option>
              </el-select>
            </el-col>
            <!-- 用户需求分类按钮 -->
            <el-col :span="4">
              <el-button type="warning" round @click="uploadCommentsFile()">用户需求上传</el-button>
            </el-col>
            <el-col :span="4">
              <el-button type="primary" round @click="doClassification()">用户需求分类</el-button>
            </el-col>
            <!-- 用户需求词云按钮 -->
            <el-col :span="4">
              <el-button type="info" round @click="getWordCloud()">生成词云</el-button>
            </el-col>
            <!-- 用户需求分类表格 -->
            <el-table></el-table>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>/* eslint-disable */
// ProjectHomePage.vue
  export default {
    created() {
      this.document_id = this.$route.query.document_id
      this.getDocument()
    },
    data() {
      return {
        // loading tag
        loadingTag: false,
        document_id: '',
        chosenDocument: {
          _id: '',
          document_name: '',
          template_name: '',
          introduction: '',
          last_time: "",
          outline: [],
          contents: [],
          comments_file_list: []
        },
        comments_file_name: '',
        // show outline and content
        outlintIndex: -1
      }
    },
    methods: {
      getDocument: async function() {
        if (this.document_id.length === 0) {
          return this.$message.error('错误！')
        }
        this.loadingTag = true
        // console.log(this.$route.query.document_id);
        // console.log(this.document_id)
        const {
          data: res
        } = await this.$http({
          method: 'get',
          url: '/document/profile',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          },
          params: {
            document_id: this.document_id
          }
        })
        if (res.meta.status === 200) {
          this.$message.success(res.meta.msg)
          this.chosenDocument = res.data.document
        } else {
          this.$message.error(res.meta.msg)
        }
        this.loadingTag = false
        this.outlintIndex = -1
      },
      editDocument: function() {
        this.$messageBox('确认提交该模板？(该操作不可逆)', {
          type: 'warning'
        }).then(async () => {
          const {
            data: res
          } = await this.$http({
            method: "post",
            url: "/document/edit",
            headers: {
              'Authorization': window.sessionStorage.getItem('token')
            },
            data: {
              document: this.chosenDocument
            }
          })
          if (res.meta.status === 200) {
            this.$message.success(res.meta.msg)
            this.getDocument()
          } else {
            this.$message.error(res.meta.msg)
          }
        }).catch(() => {
          this.$message.info('已取消删除')
        })
      },
      // 删除表格某一行
      deleteRow: function(index, rows) {
        rows.splice(index, 1);
      },
      deleteOutline: function(line, index) {
        this.$messageBox('确认删除\"' + line + '\"', {
          type: 'warning'
        }).then(async () => {
          this.chosenDocument.outline.splice(index, 1)
          this.chosenDocument.contents.splice(index, 1)
          const {
            data: res
          } = await this.$http({
            method: "post",
            url: "/document/edit",
            headers: {
              'Authorization': window.sessionStorage.getItem('token')
            },
            data: {
              document: this.chosenDocument
            }
          })
          if (res.meta.status === 200) {
            this.$message.success(res.meta.msg)
            this.getDocument()
          } else {
            this.$message.error(res.meta.msg)
          }
        }).catch(() => {
          this.$message.info('已取消删除')
        })
      },
      deleteCommentsFile: function(fileName, index) {
        this.$messageBox('确认删除\"' + fileName + '\"', {
          type: 'warning'
        }).then(async () => {
          this.chosenDocument.comments_file_list.splice(index, 1)
          this.editDocument()
        }).catch(() => {
          this.$message.info('已取消')
        })
      },
      uploadCommentsFile: async function() {

      },
      getWordCloud: async function() {

      },
      doClassification: async function() {

      }
    }
  }
</script>

<style lang="less" scoped>
</style>
