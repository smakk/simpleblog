#一个类的实例代表一篇文章的信息，其中article_context内容代表文章摘要
class mainpage_info_item(object):
    def __init__(self,time,auther,article_type,title,article_context,article_addr,extra_info,type_addr,article_id,read_num,recommand_star):
        self.time = time
        self.auther = auther
        self.article_type = article_type
        self.title = title
        self.article_context = article_context
        self.article_addr = article_addr
        self.extra_info = extra_info
        self.type_addr = type_addr
        self.article_id = article_id
        self.read_num = read_num
        self.recommand_star = recommand_star
