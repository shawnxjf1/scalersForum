##项目运营形式
1.成员自愿参与
2.成员下载代码进行代码修改 （修改方式见 "编写和修改方式” 一节）。
3.成员fork 我的git代码 修改提交后，经审核后合并到主体包中。
4.团队氛围：团队以文字沟通为主，有问题直接提出(写在/doc/...文件夹下)。
5.联系方式：要参加的成员把 S[编号]_微信号_手机号 发给shawn，shawn进行统一整理。


##工程信息
1.github 地址:https://github.com/shawnxjf1/scalersForum.git -(成员fork后请替换成自己的地址)

2.下载代码
git clone  https://github.com/shawnxjf1/scalersForum.git

3.提交代码
git remote add origin https://github.com/shawnxjf1/scalertalk_blog.git
git push -u origin master

##工程结构
1.scalers包为主体包.

2.下面两个包以 称呼命令，如xiangzi 提交了代码或者添加了新的模块就放在"xiangzi"包中
pengyong
xiangzi

3.全局test包 用来测试基本函数


##"代码编写和修改需要注意的地方""
1.文件头 一定要说明python的版本号
2.模块一定要说明该模块的作用 （一个模块只解决某一环节或者某一具体问题）
3.每个函数需要保证测试通过且标明注释，在自己package中保留测试用例 比如在"xiangzi/test.py"中测试
4.在/doc/ 文件夹下以自己文件命名 的文件中写上工作日志，如果内容多建一个文件夹  比如：
/doc/xiangzi/疑问问题.md 
            ./工作日志.md

##技术点及其改进的地方
1. 多线程拉取网页（成员量1000多单线程拉太长了） - 正好学习 协程和多线程
2. 拉取折叠区域的数据
3. 采用第三方数据库存储数据


