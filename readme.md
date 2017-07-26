
# Spider baidubaike
 
该脚本实现爬取百度百科的词条 && 词条类别 && 词条URL，并将爬虫结果写入数据库；

- 数据库`nlp.baidubaike`
- 字段:`id,vocabularyEntry,vocabularyEntryClass,url`

eg：

```
百度百科 文化  https://baike.baidu.com/view/1.htm
词条  https://baike.baidu.com/view/2.htm
馒头  https://baike.baidu.com/view/4.htm
雁荡山 山脉  https://baike.baidu.com/view/6.htm
灵峰 旅游 地理 地点 地形地貌  https://baike.baidu.com/view/7.htm
大龙湫 景观景点 旅游 地理 地形地貌  https://baike.baidu.com/view/8.htm
五大夫松 旅游 地理 地点 历史  https://baike.baidu.com/view/9.htm
红色食品 非科学  https://baike.baidu.com/view/10.htm
饴糖 中药  https://baike.baidu.com/view/11.htm
萝卜腿 疾病  https://baike.baidu.com/view/13.htm
亚健康 科学百科疾病症状分类 文化  https://baike.baidu.com/view/14.htm

```


- 依赖库：MySQLdb，urllib2，BeautifulSoup
- 使用pip安装：

```
pip install MySQLdb
pip install urllib2
pip install BeautifulSoup
```