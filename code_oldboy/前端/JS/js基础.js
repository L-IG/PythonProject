// 这里内容主要是博客上的!
// 注释

// 这是单行注释
/*
这是
多行注释
*/

// 结束符,一般建议都写上
// javaScript中的语句要以分号（;）为结束符。

// js文件引入方式,以及js文件位置
// Script标签内写代码,一般写在末尾
// <script>
//  在这里写你的JS代码
// </script>
// 引入额外的JS文件
// <script src="js基础.js"></script>

// 变量声明
// JavaScript的变量名可以使用_，数字，字母，$组成，不能以数字开头。
// 声明变量使用 var 变量名; 的格式来进行声明

var name = 'alex';
var age = 18;


// JavaScript数据类型
// js变量是动态的,既可以是数字又可以是字符串
var x1;  // 此时x是undefined
var x2 = 1;  // 此时x是数字
var x3 = "Alex";  // 此时x是字符串

// 数值(Number)
// JavaScript不区分整型和浮点型，就只有一种数字类型。
var a = 12.34;
var b = 20;
var c = 123e5;  // 12300000
var d = 123e-5;  // 0.00123

// 还有一种NaN，表示不是一个数字（Not a Number）
// 举个例子,当使用方法把字符串转化为数字时,该方法做不到,就会返回一个NaN
parseInt("123");  // 返回123
parseInt("ABC");  // 返回NaN,NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。
parseFloat("123.456");  // 返回123.456


// 字符串(String)
var a1 = "Hello";
var b1 = "world";
var c1 = a1 + b1;
console.log(c1);  // 得到Helloworld

// 常用方法：
// .length	返回长度
// .trim()	移除空白
// .trimLeft()	移除左边的空白
// .trimRight()	移除右边的空白
// .charAt(n)	返回第n个字符
// .concat(value, ...)	拼接
// .indexOf(substring, start)	子序列位置
// .substring(from, to)	根据索引获取子序列
// .slice(start, end)	切片
// .toLowerCase()	小写
// .toUpperCase()	大写
// .split(delimiter, limit)	分割

// 拼接字符串一般使用“+”

// slice与substring的区别:
// string.slice(start, stop)和string.substring(start, stop)：
// 两者的相同点：
// 如果start等于end，返回空字符串
// 如果stop参数省略，则取到字符串末
// 如果某个参数超过string的长度，这个参数会被替换为string的长度
// substirng()的特点：
// 如果 start > stop ，start和stop将被交换
// 如果参数是负数或者不是数字，将会被0替换
// silce()的特点：
// 如果 start > stop 不会交换两者
// 如果start小于0，则切割从字符串末尾往前数的第abs(start)个的字符开始(包括该位置的字符)
// 如果stop小于0，则切割在从字符串末尾往前数的第abs(stop)个字符结束(不包含该位置字符)
// 总结:slice更像是切片一点,substirng适合正常的使用


// 布尔值(Boolean)
// 区别于Python，true和false都是小写。

var a3 = true;
var b3 = false;

// 注意:""(空字符串)、0、null、undefined、NaN都是false。

// null和undefined的区别:
// null表示值是空，一般在需要指定或清空一个变量时才会使用，如 name=null;
// undefined表示当声明一个变量但未初始化时，该变量的默认值是undefined。还有就是函数无明确的返回值时，返回的也是undefined。
// null表示变量的值是空，undefined则表示只声明了变量，但还没有赋值。

// 对象(Object)
// JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...此外，JavaScript 允许自定义对象。
// JavaScript 提供多个内建对象，比如 String、Date、Array 等等。
// 对象只是带有属性和方法的特殊数据类型。

// 数组
// 数组对象的作用是：使用单独的变量名来存储一系列的值。类似于Python中的列表。
var a = [123, "ABC"];
console.log(a[1]);  // 输出"ABC"

// 常用方法：

// .length	数组的大小
// .push(ele)	尾部追加元素
// .pop()	获取尾部的元素
// .unshift(ele)	头部插入元素
// .shift()	头部移除元素
// .slice(start, end)	切片
// .reverse()	反转
// .join(seq)	将数组元素连接成字符串
// .concat(val, ...)	连接数组
// .sort()	排序
// .forEach()	将数组的每个元素传递给回调函数
// .splice()	删除元素，并向数组添加新元素。
// .map()	返回一个数组元素调用函数处理后的值的新数组

// 关于sort()需要注意：
// 如果调用该方法时没有使用参数，将按字母顺序对数组中的元素进行排序，说得更精确点，是按照字符编码的顺序进行排序。要实现这一点，首先应把数组的元素都转换成字符串（如有必要），以便进行比较。
// 如果想按照其他标准进行排序，就需要提供比较函数，该函数要比较两个值，然后返回一个用于说明这两个值的相对顺序的数字。比较函数应该具有两个参数 a 和 b，其返回值如下：
// 若 a 小于 b，在排序后的数组中 a 应该出现在 b 之前，则返回一个小于 0 的值。
// 若 a 等于 b，则返回 0。
// 若 a 大于 b，则返回一个大于 0 的值。

// 如果真要使用的话建议用下面的写法,通常数据都是在后端处理好才发过来的
function sortNumber(a, b) {
    return a - b
}

var arr1 = [11, 100, 22, 55, 33, 44];
arr1.sort(sortNumber);
console.log(arr1);   //[11, 22, 33, 44, 55, 100]

// 数组的遍历
var a = [10, 20, 30, 40];
for (var i = 0; i < a.length; i++) {
    console.log(a[i])
}
// 10
// 20
// 30
// 40

// 类型查询
// typeof
typeof "abc"; // "string"
typeof null; // "object"
typeof true; // "boolean"
typeof 123;// "number"

// typeof是一个一元运算符（就像++，--，！，- 等一元运算符），不是一个函数，也不是一个语句。
// 对变量或值调用 typeof 运算符将返回下列值之一：
// undefined - 如果变量是 Undefined 类型的
// boolean - 如果变量是 Boolean 类型的
// number - 如果变量是 Number 类型的
// string - 如果变量是 String 类型的
// object - 如果变量是一种引用类型或 Null 类型的

// 运算符
// 算数运算符
// + - * / % ++ --
// 比较运算符
// > >= < <= != == === !==
// 注意：
// 1 == “1”  // true
// 1 === "1"  // false
// 逻辑运算符
// && || !
// 赋值运算符
// = += -= *= /=

// ==:弱类型运算符,当遇到数字与字符串比较时,会出现相等的情况
// ===:强类型运算符

// 流程控制
// if-else
var a = 10;
if (a > 5) {
    console.log("yes");
} else {
    console.log("no");
}

// if-else if-else
var a = 10;
if (a > 5) {
    console.log("a > 5");
} else if (a < 5) {
    console.log("a < 5");
} else {
    console.log("a = 5");
}

// switch
var day = new Date().getDay();
switch (day) {
    case 0:
        console.log("Sunday");
        break;
    case 1:
        console.log("Monday");
        break;
    default:
        console.log("...")
}

// switch中的case子句通常都会加break语句，否则程序会继续执行后续case中的语句。

// for
for (var i = 0; i < 10; i++) {
    console.log(i);
}
// while
var i = 0;
while (i < 10) {
    console.log(i);
    i++;
}
// 三元运算
var a = 1;
var b = 2;
var c = a > b ? a : b