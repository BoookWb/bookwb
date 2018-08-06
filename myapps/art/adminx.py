#from django.contrib import admin
import xadmin
from xadmin import views

from art.models import Category, Art

# 配置主题
class BastSettings:
    enable_themes = False
    use_bootswatch = False
# 全局的配置
class GlobalSettings:
    site_title = '文章管理系统'
    site_footer = '@<span style="font-size:25px;color:blue;">千锋教育.</span><a href = "http://www.baidu.com" class ="btn btn-link">郑州py1802</a>'
    menu_style = 'accordion'# 菜单折叠效果
    # 搜索模型
    global_search_models = [Art,Category]
    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        Art: "glyphicon glyphicon-cloud",
        Category: "glyphicon glyphicon-music"
    }  # 设置models的全局图标
#配置模型的输出
class CategoryAdmin:

    #显示的字段
    list_display = ['name','add_time']
    search_fields = ['name']# 搜索的字段
class ArtAdmin:
    list_display = ['title','author','content','publish_time','category']
    search_fields =['title','category__name']
    list_per_page = 10 #每页显示的记录数
    # 设置字段的样式
    style_fields = {
        'content':'ueditor'
    }

#site位置，register登记
# Register your models here.
xadmin.site.register(views.BaseAdminView,BastSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Art,ArtAdmin)
