<template>
  <div id="app">
    <!-- 面包屑区域 -->
    <div>
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>模板管理</el-breadcrumb-item>
        <!-- <el-breadcrumb-item :to="{ path: '/templates/templateList' }">模板列表</el-breadcrumb-item> -->
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
        </el-col>
        <el-col :span="8">
          <el-tooltip effect="light" content="选择模板创建文档" placement="top-start">
            <!-- when click the button, show the dialog -->
            <el-button type="primary" @click="dialogVisible = true">创建新文档</el-button>
          </el-tooltip>
        </el-col>
      </el-row>
      <el-table v-loading='loadingTag' class="documentList-table" :data="documentList" border>
        <el-table-column type="index" label="#"></el-table-column>
        <!-- todo -->
        <el-table-column prop="document_name" label="文档名" sortable></el-table-column>
        <!-- 按照模板进行筛选 -->
        <el-table-column prop="template_name" label="所属模板"></el-table-column>
        <el-table-column prop="last_time" label="最后修改时间" sortable></el-table-column>
        <el-table-column prop="introduction" label="文档简介"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-tooltip effect="light" content="查看/编辑该文档" placement="top-start">
              <el-button type="info" size="small" icon="el-icon-info"></el-button>
            </el-tooltip>
            <el-tooltip effect="light" content="删除该文档" placement="top-start">
              <el-button type="danger" size="small" icon="el-icon-delete" @click="deleteDocument(scope.row.document_id)"></el-button>
            </el-tooltip>
            <el-tooltip effect="light" content="下载该文档(word格式)" placement="top-start">
              <el-button type="success" size="small" icon="el-icon-download" @click="downloadDocument(scope.row.document_id)"></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
     <!-- 创建新文档对话框 -->
     <el-dialog title="创建新的文档"  width="40%" :visible.sync="dialogVisible">
       <el-form>
         <!-- 选择一个模板 -->
         <el-form-item label="选择一个模板">
           <!-- 下拉选择模板 选择器 -->
           <el-select v-model="chosenTemplateName" clearable filterable placeholder="请选择一个模板">
             <el-option
              v-for="template in templateList"
              :key="template.template_name"
              :label="template.template_name"
              :value="template.template_name">
             </el-option>
           </el-select>
         </el-form-item>
         <!-- 文档名 -->
         <el-form-item label="文档名">
           <el-input v-model="newDocumentTitle"></el-input>
         </el-form-item>
         <!-- 填写简介 -->
         <el-form-item label="文档简介">
           <el-input type="textarea" v-model="newDocumentIntroduction" :rows="5"></el-input>
         </el-form-item>
       </el-form>
       <span slot="footer" class="dialog-footer">
         <el-button @click="dialogVisible = false">取消</el-button>
         <el-button type="primary" @click="createDocument">创建文档</el-button>
       </span>
     </el-dialog>
   </div>
</template>

<script>/* eslint-disable */
// ProjectHomePage.vue
  export default {
    created() {
      this.getDocumentList()
      this.getTemplateList()
    },
    data() {
      return {
        // all template list
        templateList: [],
        // all document list
        documentList: [],
        // loading tag for document table
        loadingTag: false,
        // new document info
        dialogVisible: false,
        newDocumentTitle: "",
        newDocumentIntroduction: "",
        chosenTemplateName: ""
      }
    },
    methods: {
      getTemplateList: async function() {
        const {
          data: res
        } = await this.$http({
          method: 'get',
          url: '/template/list',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          }
        })
        if (res.meta.status === 200) {
          this.templateList = res.data
        } else {
          this.$message.error(res.meta.msg)
        }
      },
      getDocumentList: async function() {
        this.loadingTag = true
        const {
          data: res
        } = await this.$http({
          method: 'get',
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
        if (this.chosenTemplateName.length == 0) {
          return this.$message.error('请填写选择相应模板！')
        }
        if (this.newDocumentTitle.length == 0) {
          return this.$message.error('请填写文档标题！')
        }
        const {
          data: res
        } = await this.$http({
          method: 'post',
          url: '/document/create',
          headers: {
            'Authorization': window.sessionStorage.getItem('token')
          },
          data: {
            template_name: this.chosenTemplateName,
            document_name: this.newDocumentTitle,
            introduction: this.newDocumentIntroduction
          }
        })
        if (res.meta.status === 200) {
          this.$message.success(res.meta.msg)
          this.newDocumentIntroduction = ''
          this.newDocumentTitle = ''
          this.getDocumentList()
        } else {
          this.$message.error(res.meta.msg)
        }
      },
      deleteDocument: async function(document_id) {
        console.log(document_id);
        this.$messageBox('此操作将永久删除该文档, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(
          async () => {
            const {
              data: res
            } = await this.$http({
              method: 'delete',
              url: '/document/delete',
              headers: {
                'Authorization': window.sessionStorage.getItem('token')
              },
              data: {
                'document_id': document_id
              }
            })
            if (res.meta.status === 200) {
              this.$message.success(res.meta.msg)
              this.getDocumentList()
            } else {
              this.$message.error(res.meta.msg)
            }
          }
        ).catch(() => {
          this.$message.info('已取消删除')
        })
      },
      downloadDocument: async function(document_id) {
        // todo
      }
    }
  }
</script>

<style lang="less" scoped>
  .documentList-table {
    margin-top: 15px;
  }
</style>
