Django Blog of Hill1895--刘文图熙1895的博客
===================
该网站为个人的博客网站，用于记录个人的一些技术学习心得及其他东西，网站地址为[hill1895.rocks](http://hill1895.rocks)。
###网站架构
* **服务器**：空间使用AWS一年免费的虚拟机，使用ubuntu14. 04+Nginx1.8+uWSGI来部署Django应用，从Name.com上购买域名。
*  **博客后台**：修改Django自带的Admin系统，主要添加富文本编辑器用于编写博客，富文本编辑器选择百度的UEditor，其[Django的集成版本](https://github.com/zhangfisher/DjangoUeditor)可以在Github上找到。
*  **网站框架**：Django1.8。1.8版较以前版本在Template，staticfiles，数据库同步等方面有一些改动，使用的时候注意参考官方文档。
*  **数据库**：使用MySQL，主要便于同Django集成。
*  **前端**：框架和UI使用Bootstrap3，布局使用Bootstrap的栅格布局，便于做响应式设计，以便支持不同尺寸的设备。使用
SyntaxHighlighter来对pre标签中的代码做代码高亮，目前与Bootstrap似乎还存在一些样式兼容问题。

####目前存在的问题
1. ~~目前小尺寸设备（5S以下）的排版似乎还有问题，iOS Safari的字体似乎没有响应式的放缩，原因还未找到。~~
2. ~~SyntaxHighlighter显示出的代码高亮样式还有问题，尚未找出原因。~~

#####2015.6.12更新
1. 加入Favicon.ico
2. 修改一些网页样式

#####2015.6.22更新
1. 修改响应式设计，更好的支持小型设备
2. 修改一些CSS样式
3. 修改背景及头图

#####2015.6.23更新
1. 增加多说评论插件

#####2015.6.24更新
1. 增加分享功能
2. 文章分类细化

#####2015.6.26更新
1. 编写Profile页
2. 增加友情链接
3. 修改SyntaxHighlighter样式

#####2015.6.27更新
1. 修复Bootstrap网格布局padding超出页面的问题

#####2015.6.28更新
1. 适配iPad

#####2015.6.28更新
1. SEO 优化

#####2015.6.30更新
1. 设计404页面

#####2015.7.5更新
1. 使用Django_compressor合并static文件，使用nginx的gzip压缩静态文件，大幅提高访问速度。
2. robots.txt

#####2015.7.6更新
1. 使用django.contrib.sitemaps自动生成sitemap