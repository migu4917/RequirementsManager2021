<template>
  <div id="app">
    <!-- 面包屑区域 -->
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>模板管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/templates/templateList' }">模板列表</el-breadcrumb-item>
        <el-breadcrumb-item>文档管理</el-breadcrumb-item>
        <el-breadcrumb-item>文档名-记得改</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <el-card class="box-card" style="margin-top: 15px;">
      <el-row :gutter="20" style="margin-bottom: 20px;">
        <el-col :span="6">
          <div><span style="color: ghostwhite;">目录</span></div>
        </el-col>
        <el-col :span="18">
          <!-- 添加需求按钮 -->
          <el-dropdown trigger="click" size="medium" @command="handleAddRequirement">
            <el-button type="primary" icon="el-icon-plus" plain round>添加</el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="addBefore">在上方插入</el-dropdown-item>
              <el-dropdown-item command="addAfter">在下方插入</el-dropdown-item>
              <el-dropdown-item command="addInner">添加子需求</el-dropdown-item>
              <el-dropdown-item command="importFile" divided>从文本导入</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-col>
      </el-row>
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

      }
    },
    methods() {

    }
  }
</script>

<style lang="less" scoped>
</style>
