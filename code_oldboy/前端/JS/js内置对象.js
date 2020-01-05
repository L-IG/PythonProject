// js对象与基本数据类型的概念

// 基本数据类型有:Number, String, Boolean
// 组合对象:Array, Math, Date

var s1 = 10;
var s1_ = new Number(10);
var s1__ = Number(10);
console.log(s1, typeof s1);
console.log(s1_, typeof s1_);

var s2 = 'abc';
// 注意两种写法的不一样,不加new的是string,加new的是对象!!!!!
// 注意var s1 = "abc"和var s2 = new String("abc")的区别：typeof s1 --> string而 typeof s2 --> Object
var s2_ = new String("abc");
var s2__ = String("abc");
console.log(s2, typeof s2);
console.log(s2_, typeof s2_);

// 自定义对象
// 本质上就是Python字典形式
var personalObj = {"name": "alex", "age": 18};
var name_var = "name";
// 注意有两个访问对象属性的方法,第一种表示字符串,第二个是变量,当属性名被存在变量里时,只有用第二种才可以
console.log(personalObj.name, personalObj["name"]);
console.log(personalObj.name, personalObj[name_var]);


// 另一种创建对象的方法:
var person = Object();
person.sex = 'Man';
person.age = 20;
console.log(person.sex, person.age);

// 遍历对象的属性
for (var i in person) {
    console.log(i, person[i]);
}

// Date对象
var d1 = new Date();
// var d1 = Date();
console.log(d1, typeof d1);  // Sat Jan 04 2020 13:05:52 GMT+0800 (中国标准时间)
console.log(d1.toLocaleString(), typeof d1.toLocaleString());//2020/1/4 下午1:08:17 string
console.log("~~~~~~");
var d2 = new Date("2020-01-04");
console.log(d2, d2.toLocaleString()); //Sat Jan 04 2020 08:00:00 GMT+0800 (中国标准时间) "2020/1/4 上午8:00:00"
console.log(d2.toUTCString());// 转成字符串格式的UTC时间

console.log(d2.getDate());//具体哪一天
console.log(d2.getDay());//星期几
console.log(d2.getMonth());//月份
console.log(d2.getFullYear());//年
console.log(d2.getHours());//小时
console.log(d2.getMinutes());//分钟
console.log(d2.getSeconds());//秒
console.log(d2.getTime());//时间戳

//Json对象
// 注意json字符串写法,里面的全是双引号,但是最外面用单引号括起来
var s = '{"name":"Ming","age":18}';
// 把字符串转换成JS内部的对象parse
var ret = JSON.parse(s);
console.log(ret, typeof ret);//{name: "Ming", age: 18} "object",其实在代码里面对于key是不加引号的
// 把JS内部的对象转换成字符串stringify
var s_ = JSON.stringify(ret);
console.log(s_, typeof s_);//{"name":"Ming","age":18} string

//Math对象

//RegExp对象
// 把正则表达式存到一个变量里
var reg1 = RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
var regexRet1 = reg1.test("xiaoqiang");
console.log(regexRet1);
//直接写成一行
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test('xiaoming'));

console.log('~~~前端正则表达式的坑~~~');

// 坑1 (正则表达式中间一定不可以有空格)
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("xiaoqiang"));
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5, 11}$/.test("xiaoqiang"));

// 坑2 test()不传值相当于传了一个undefined进去
// 然后test()就把这个undefined当成是"undefined"来判断
console.log("============================================");
console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("undefined"));//true
console.log(/^[0-9]{0,10}$/.test());//false
console.log(/^undefined$/.test(undefined));//true
console.log(/^undefined$/.test("undefined"));//true


//js正则的两种模式
// g表示global全局的
//i表示忽略大小写
var ss = "Alexdashabi";
var ss_ = ss.replace(/a/g, '哈哈哈');
var ss__ = ss.replace(/a/gi, '哈哈哈');
console.log(ss_, ss__);

// 坑3
// 当正则表达式使用了全局模式(g)的时候,并且存在一个变量里,并且你还让它去检测一个字符串,此时会引出来一个lastIndex
// lastIndex会记住上一次匹配成功的位置,并把下一次要开始校验的位置记住
//
console.log("===============================");
var r = /alex/g;
console.log(r.test("alex"));  // true
console.log(r.lastIndex);  // 4
console.log(r.test("alex"));  // false
console.log(r.lastIndex);
console.log(r.test("alex"));  // true
console.log(r.lastIndex);
console.log(r.test("alex"));  // false

// 如果要用全局的,最好只写成下面这样,不要保存在变量里
//lastIndex只对那一行起作用,不影响其他行
console.log(/alex/g.test('alex12345678'));
console.log(/alex/g.test('alexalexalexalex1234'));