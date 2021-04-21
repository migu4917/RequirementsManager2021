<template>
  <div id="app">
    <!-- 面包屑区域 -->
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>模板管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/templateList' }">模板列表</el-breadcrumb-item>
        <el-breadcrumb-item>文档管理</el-breadcrumb-item>
        <!-- <el-breadcrumb-item>文档名-记得改</el-breadcrumb-item> -->
      </el-breadcrumb>
    </div>
    <!-- 主体区域 -->
    <el-card class="box-card" style="margin-top: 15px;">
      <!-- 搜索与添加区域 -->
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input placeholder="请输入文档关键字" class="input">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
          <el-tooltip effect="light" content="选择模板创建文档" placement="top-start">
            <!-- todo -->
            <el-button @click="">创建新文档</el-button>
          </el-tooltip>
        </el-col>
      </el-row>
      <!-- todo： data -->
      <el-table v-loading='loadingTag' class="templateList-table" :data="" border>
        <el-table-column type="index" label="#"></el-table-column>
        <!-- todo -->
        <el-table-column prop="" label="文档名"></el-table-column>
        <el-table-column prop="" label="所属模板"></el-table-column>
        <el-table-column prop="" label="最后修改时间"></el-table-column>
        <el-table-column prop="" label="文档简介"></el-table-column>
      </el-table>
    </el-card>
   </div>
</template>

<script>/* eslint-disable */
// ProjectHomePage.vue
  export default {
    created() {

    },
    data() {
      return {
        // all document list
        documentList: [],
        // loading tag for document table
        loadingTag: true,
        // new document info
        newDocumentTitle: "",
        newDocumentIntroduction: "",
      }
    },
    methods() {
      getDocumentList: async function() {
        this.loadingTag = true
        const {
          data: res
        } = await this.$http({
          methods: 'get',
          url: '/document/list',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          }
        })
        if (res.meta.status === 200) {
          this.documentList = res.data
        } else {
          this.$message.error(res.meta.msg)
        }
        this.loadingTag = false
      },
      createDocument: async function() {
        const {
          data: res
        } = await this.$http({
          methods: 'post',
          url: '/document/create',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          }
        })
        if (res.meta.status === 200) {
          // this.tempList = res.data
        } else {
          this.$message.error(res.meta.msg)
        }
      },
      deleteDocument: async function() {
        // todo
      },
      downloadDocument: async function() {
        // todo
      }
    }
  }
</script>

<style lang="less" scoped>
</style>
