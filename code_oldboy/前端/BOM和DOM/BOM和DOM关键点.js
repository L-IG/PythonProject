// 1.BOM
//         下面都是windows的对象,一般可以省略
// 		1. location
// 			1. location.href      --> 获取当前的URL
// 			2. location.href="http://www.luffycity.com" --> 跳转到指定网址
// 			3. location.reload()  --> 重新加载当前页面
//         警告框alert("你看到了吗？");
//         确认框confirm("你确定吗？");
//         提示框prompt("请在下方输入","你的答案");

// 		2. setTimeout和clearTimeout
// 			多少毫秒之后做什么事儿
//         t = setTimeout("js语句",毫秒)
//         t表示函数返回值,可以结合clearTimeout使用,取消函数的调用
//         js语句可以是是一个函数名,不用写成调用形式!!
//
// 		3. setInterval和clearInterval
// 			每隔多少毫秒之后做什么事儿


// 	2.DOM
// 		1. 什么是DOM树
// 		2. DOM都有哪一些内容
// 		3. JS操作DOM
// 			1. 找标签
// 				1. 基本查找
// 					1. 根据ID找标签(有且只能找到一个)
// 						document.getElementById("ID值")
// 					2. 根据class名字找(找到的可以是多个)
// 						document.getElementsByClassName("class值")
// 					3. 根据标签名找(找到的可以是多个)
// 						document.getElementsByTagName("标签名")

// 				2. 间接查找
//                     var Ele = document.getElementById("ID值")
//                     Ele表示一个标签变量节点
//                     1. 找父标签
// 						Ele.parentElement
// 					2. 找子标签(找到的可能是多个)
// 						Ele.children
// 					3. 第一个子标签
//                         Ele.firstElementChild
// 					4. 最后一个子标签
//                         Ele.lastElementChild
// 					5. 前一个兄弟标签
//                         Ele.previousElementSibling
// 					6. 后一个兄弟标签
//                         Ele.nextElementSibling
// 			2. 创建标签  *****
// 				creatElement("标签名")
//                 var divEle = document.createElement("div");

// 			3. 添加标签
// 				1. 在内部的最后添加
// 					appendChild("标签名");
// 				2. 在内部的某个标签的前面插入
// 					insertBefore(要插入的新标签, 哪个标签之前);
//                 somenode.appendChild(newnode);
//                 somenode.insertBefore(newnode,某个节点);
// 			    添加节点的两个方法都是通过父元素往子元素里面添加的!!!
// 			4. 属性(内置属性)
//                 内置属性直接使用下面方法
// 				.属性名="属性值";

// 				自定义的属性只能用:
// 					.setAttribute("s9", "hao")
// 					.getAttribute("s9")
// 					.removeAttribute("s9")

// 			5. 文本操作
// 				1. 设置文本的内容
// 					.innerText=""
// 				2. 设置标签内容
// 					.innerHTML="<p>我是p标签</p>"
// 				3. 获取值的区别
// 					1. .innerHTML  --> 子标签和子标签的内容都取出来
// 					2. .innerText  --> 只取标签之间的文本内容

// 			6. 样式操作
// 				1. 通过class修改
// 					1. classList.remove(cls)  删除指定类
// 					2. classList.add(cls)  添加类
// 					3. classList.contains(cls)  存在返回true，否则返回false
// 					4. classList.toggle(cls)  存在就删除，否则添加
// 					5. className  获取所有样式类名(字符串)
//                     注意:className是所有类在一起的一个字符串,不方便修改,一般用classList
// 				2. 通过.style修改
// 					1. 有中横线的
// 						.style.backgroundColor;
// 					2. 没有中横线的
// 						.style.color;
// 			获取值操作:
//                 语法：
//                     elementNode.value;
//                     适用于以下标签：form表单里 key(name),value(value)需要关注
//                     .input
//                     .select
//                     .textarea

// 			7. 事件(事件实际上是一个属性)
// 				1. 常用事件
// 					1. onclick
// 					2. ondbclick
// 					3. onfocus
// 					4. onblur
// 					5.onchange
// 				2. 绑定事件的方式
// 					1. 在标签里直接写属性(onclick=foo())
// 					2. 通过JS给标签绑定事件
// 				3. this --> 代表的是触发事件的当前标签