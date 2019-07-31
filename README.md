# epili

#  霹雳诗号

>  收集霹雳人物和诗号

!['搜索']('static/search.png')

###  贡献方法


直接在data目录下按照数据格式新建一个json文本就可以了


数据格式

```
{

"id"  :"",//uuid 字符串  可选
"name":"",//名字 字符串  必填
"title":"",//称号 字符串 可选
"level":"", //境界 字符串 可选
"race":"",// 种族 字符串 可选
"sects":"",//门派 字符串 可选
"poetry":[],//一个人可能有很多个诗号  数组 可选
"desc":"", //介绍  字符串 可选
"img":[] //剧照 数组 可选

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
