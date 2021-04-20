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
    <!-- 主体区域 -->
    <el-tabs v-model="" tab-position="top" style="overflow: auto;">
      <!-- 文档编辑区域 -->
      <el-tab-pane label="需求文档编辑" name="0">
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
      </el-tab-pane>
      <!-- 用户需求区域 -->
      <el-tab-pane label="用户反馈管理和分析" name="1">
      </el-tab-pane>
    </el-tabs>
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
