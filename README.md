# Demo
后端Django，前端目前基于easyui，自己尝试制作的一些组件Demo，例如【登录/注册】组合功能，争取做到能复用并提供参考。

# 2017/10/11
1）添加了简单的Login页面；  
2）完成后端基本搭建（admin，user数据表等），增加了LoginView，提供了get/set接口。目前功能性未测试；  

# 2017/10/12
1）修改了Login页面，增加了index页面方便调试；  
2）增加了退出功能，完善了登录功能，通过重载authenticate方法并结合使用Q方法，登录支持用户名和邮箱校验。  

# 2017/10/15
1）增加了app:relation用来测试一些model关系（one2one,one2many,many2many）；  
2）解决了一个admin.py下，list_display[]中不能包含ManytoManyField的问题，该问题在SO上有解答https://stackoverflow.com/questions/18108521/many-to-many-in-list-display-django ，即声明一个方法去获取字段。  

# 2017/10/17
1)调整了blog.model里的对象关系，增加了article用来描述具体文章；  
2）使用markdown显示文章详情；  
3）增加了首页跳转文章详情功能；  

