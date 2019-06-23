# Log
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- logging模块提供模块级别的函数记录日志
- 包括四大组件

## 1. 日志相关概念
- 日志
- 日志的级别（level）
    - 不同的用户关注不同程序信息
    - DEBUG
    - INFO
    - 。。。
- IO操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2. Logging模块
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或高于指定级别才被记录
- 使用方式
    - 直接使用logging(封装了其他组件)
    - logging四大组件直接定制
    
#2.1 logging模块的界别日志
- 使用一下几个函数
        - logging.debug(msg, *args, **kwargs)  创建一条严重级别为DEBUG的日志记录
        - logging.info(msg, *args, **kwargs)  创建一条严重级别为INFO的日志记录
        - logging.warning(msg, *args, **kwargs)  创建一条严重级别为WARNING的日志记录
        - logging.error(msg, *args, **kwargs)  创 建一条严重级别为ERROR的日志记录
        - logging.critical(msg, *args, **kwargs)  创建一条严重级别为CRITICAL的日志记录
        - logging.log(level, *args, **kwargs)  创建一条严重级别为level的日志记录 
        - logging.basicConfig(**kwargs)  对root logger进行一次性配置
- logging.basicConfig(**kwargs)  对root logger进行一次性配置     
    - 旨在第一次条用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr
        - 级别：WARNING
        - 格式：level：Log_name:content
- 案例01
- format参数    
        
        https://www.cnblogs.com/yyds/p/6901864.html
        4. logging模块定义的格式字符串字段
        
# 2.1.logging模块处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个接口
    - 处理器（Handler）：把产生的日志发送到相应的目的地
    - 过滤器（Filter）：更精细的控制那些日志输出
    - 格式器（Formatter）：对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
            上面网址
            
    - 如何得到一个logger对象
    - 实例化
    - logging.getLogger()
    
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter
    - 不需要直接使用，Handler是基类
    
            网址自己看
           
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容 
    - 三个参数
        - fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt：指定日期格式字符串，如果不指定该参数默认使用"%Y-%m-%d %H:%M:%S"
        - style:python3.2新增的参数，
- Filter类
    - 可以被Hanler和Logger使用
    - 控制传递过来的信息的具体内容
    - 案例02         
           