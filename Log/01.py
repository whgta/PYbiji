import logging
LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"

# level改变等级从最低等级DEBUG开始输出
#filename设置日志输出格式在wh.log中
logging.basicConfig(filename= "wh.log",level= logging.DEBUG,format= LOG_FORMAT)#
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


# 另一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
