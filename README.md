# epili

#  霹雳诗号

>  收集霹雳人物和诗号

###  贡献方法


直接在data目录下按照数据格式新建一个json文本就可以了


数据格式

```
{

"id"  :"",//uuid 字符串
"name":"",//名字 字符串
"title":"",//称号 字符串
"level":"", //境界 字符串
"race":"",// 种族 字符串
"sects":"",//门派 字符串
"poetry":[],//一个人可能有很多个诗号  数组
"desc":"", //介绍  字符串
"img":[] //剧照 数组

}



```

##  说明脚本

```

python  tools/build.py  生成集合的json文件和sqlite文件

python  tools/search.py 名字 搜索诗号

```


本项目仅作为爱好收集
使用时请著名出处
请勿商用
