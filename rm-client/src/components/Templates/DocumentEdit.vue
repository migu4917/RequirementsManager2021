<template>
  <div id="app">
    <!-- 面包屑区域 -->
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>模板管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/templateList' }">模板列表</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/documentList' }">文档管理</el-breadcrumb-item>
        <el-breadcrumb-item>{{ document.document_name }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 主体区域 -->
    <!-- v-model="" -->
    <el-tabs tab-position="top" style="overflow: auto;">
      <!-- 文档编辑区域 -->
      <el-tab-pane label="需求文档编辑" name="0">
        <el-row :gutter="20" style="margin-bottom: 20px;">
          <el-col :span="6">
            <div><span style="color: ghostwhite;">目录</span></div>
          </el-col>
          <el-col :span="18">
            <!-- 添加需求按钮 -->
            <!-- <el-dropdown trigger="click" size="medium" @command="handleAddRequirement">
              <el-button type="primary" icon="el-icon-plus" plain round>添加</el-button>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="addBefore">在上方插入</el-dropdown-item>
                <el-dropdown-item command="addAfter">在下方插入</el-dropdown-item>
                <el-dropdown-item command="addInner">添加子需求</el-dropdown-item>
                <el-dropdown-item command="importFile" divided>从文本导入</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown> -->
          </el-col>
        </el-row>
      </el-tab-pane>
      <!-- 用户需求区域 -->
      <el-tab-pane label="用户反馈管理和分析" name="1">
        <!-- 用户需求文件下拉列表 -->
        <!-- 选择一个用户需求 -->
        <el-select v-model="comments_file_name" clearable filterable placeholder="请选择一个用户需求数据集">
          <el-option
           v-for="comments in document.comments_file_list"
           :key="comments"
           :label="comments"
           :value="comments">
          </el-option>
        </el-select>
        <!-- 用户需求分类按钮 -->
        <el-button type="primary" round>用户需求进行分类</el-button>
        <!-- 用户需求词云按钮 -->
        <el-button type="info" round>生成词云</el-button>
        <!-- 用户需求分类表格 -->
      </el-tab-pane>
    </el-tabs>
    <!-- test -->
    <!-- 文档编辑区域 -->
    <el-card class="box-card" style="margin-top: 15px;">
      <!-- 用户需求文件下拉列表 -->

      <!-- 用户需求分析按钮 -->

      <!-- 用户需求词云按钮 -->

      <!-- 用户需求分类表格 -->
    </el-card>
    <!-- 用户需求区域 -->
    <el-card class="box-card" style="margin-top: 15px;">
      <!-- 用户需求文件下拉列表 -->

      <!-- 用户需求分析按钮 -->

      <!-- 用户需求词云按钮 -->

      <!-- 用户需求分类表格 -->

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
        document_id: '',
        document: {
          id: '',
          document_name: '',
          template_name: '',
          introduction: '',
          last_time: [],
          contents: [],
          comments_file_list: []
        },
        comments_file_name: '',
      }
    },
    methods: {
      getDocument: async function() {
        if (this.document_id.length === 0) {
          return this.$message.error('错误！')
        }
        let tempId = this.document_id
        console.log(this.document_id)
        console.log(tempId);
        const {
          data: res
        } = await this.$http({
          method: 'get',
          url: '/document/get_document',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          },
          params: {
            document_id: this.$route.query.document_id
          }
        })
        if (res.meta.status === 200) {
          this.$message.success(res.meta.msg)
          this.document = res.data
          // this.newDocumentIntroduction = ''
          // this.newDocumentTitle = ''
          // this.getDocumentList()
        } else {
          this.$message.error(res.meta.msg)
        }
      }
    }
  }
</script>

<style lang="less" scoped>
</style>
