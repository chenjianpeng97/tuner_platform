# 说明
配合Tuner测试框架的平台
# 竞品参考
Cucumber Studio
# 功能
- 项目管理
    - 展示项目的测试情况
- 定义管理
    - 管理feature文件
        - feature文件附件
        - feature子feature
        - feature关联的scenarios文件
        - feature中的rule管理:支持gherkin v6语法特性
        - 管理feature文件目录:feature文件即表现成sceanarios的文件夹
        - feature的background
        - feature修改历史
    - 管理action words
        - 智能提示本项目中已有的action words:以便保持领域语言的一致性
        - 反查used by 哪些scenarios
        - actionwords可以嵌套其他actionword/result/action
        - 编辑actionword时,全局修改这个actionword的调用
    - i18n
        - 当scenarios或actionwords的定义不是用英文定义时;给出推荐的英文名称以映射到自动化时的变量名中
    

- 测试管理
    - 管理测试执行情况
        - 管理测试计划
            - 勾选需要测试的scenario或feature
            - 手动执行测试标记steps的执行情况
            - 管理测试结果

    - 自动化测试
        - 支持behave格式导出feature-scenario的文件目录
# 技术栈
- 前端:vue3
- 后端:python-fastapi
- 数据库:可配置sqlite或postgre
# 测试套件
- 单元测试:pytest
- 集成测试:behave
- UI测试:playwright
# 开发环境
- 前端:vue3-latest
- 后端:django-latest django-restframework bdd框架behave-django
- 数据库:sqlite3
# API风格
- RESTful
# BUILD顺序
- 输出有层次的feature描述
- DDD设计划分分析
- 设计API文档
- 结合Feature文件以BDD的方式完成后端核心功能构建,用behave为框架,在steps/model 下完成implementation,behave --stage=model features/以全部通过这些测试
- 功能函数增加单元测试套件,以TDD方式编写,以pytest驱动运行
- 逐个完成feature的unit实现,并通过测试,循环直至所有feature完成
- 完成feature的集成测试,以behave为框架,在steps/api下完成implementation,behave --stage=api features/以全部通过这些测试
- 逐个完成feature的acceptance实现,并通过测试,循环直至所有feature完成
- 根据api文档和feature完成前端构建
- 完成feature的端到端测试,以behave为框架,在steps/ui下完成implementation,behave --stage=ui features/以全部通过这些测试