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
                <el-input type="textarea" v-model="chosenDocument.introduction"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="最后修改时间">
              <el-col :span="11">
                <el-input v-model="chosenDocument.last_time" :disabled="true"></el-input>
              </el-col>
            </el-form-item>
            <el-form-item label="用户需求数据集列表">
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
              <!-- <template>
              <el-popconfirm title="确定修改吗？(该操作不可逆)"> -->
              <el-button type="primary" @click="editDocument()">提交更改</el-button>
              <!-- </el-popconfirm>
              </template> -->
            </el-form-item>
          </el-form>
          <!-- 左边栏为信息目录 -->
          <!-- <el-row :gutter="20" style="margin-bottom: 20px;">
            <el-col :span="6">
            </el-col>
          </el-row> -->
          <!-- 右边栏为相关信息 -->
        </el-tab-pane>
        <!-- 文档内容编辑 -->
        <el-tab-pane label="文档内容编辑" name="1">
          <!-- test -->
          <el-row :gutter="20" style="margin-bottom: 20px;">
            <el-col :span="6">
              <div><span style="color: ghostwhite;">目录</span></div>
            </el-col>
            <el-col :span="18">
              <!-- 添加需求按钮 -->
              <!-- <el-dropdown trigger="click" size="medium" @command="handleAddRequirement"> -->
                <!-- <el-button type="primary" icon="el-icon-plus" plain round>添加</el-button> -->
                <!-- <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item command="addBefore">在上方插入</el-dropdown-item>
                  <el-dropdown-item command="addAfter">在下方插入</el-dropdown-item>
                  <el-dropdown-item command="addInner">添加子需求</el-dropdown-item>
                  <el-dropdown-item command="importFile" divided>从文本导入</el-dropdown-item>
                </el-dropdown-menu> -->
              <!-- </el-dropdown> -->
            </el-col>
          </el-row>
        </el-tab-pane>
        <!-- 用户需求区域 -->
        <el-tab-pane label="用户反馈管理和分析" name="2">
          <!-- 用户需求文件下拉列表 -->
          <!-- 选择一个用户需求 -->
          <el-row :gutter="20">
            <el-col :span="8">
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
              <el-button type="primary" round>用户需求进行分类</el-button>
            </el-col>
            <!-- 用户需求词云按钮 -->
            <el-col :span="4">
              <el-button type="info" round>生成词云</el-button>
            </el-col>
            <!-- 用户需求分类表格 -->

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
      },
      editDocument: async function() {
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
              document: chosenDocument
            }
          })
          if (res.meta.status === 200) {
            this.$message.success(res.meta.msg)
            this.getDocument()
          } else {
            this.$message.error(res.meta.msg)
          }
        })
        .catch(() => {})
      },
      // 删除表格某一行
      deleteRow: function(index, rows) {
        rows.splice(index, 1);
      }
    }
  }
</script>

<style lang="less" scoped>
</style>
