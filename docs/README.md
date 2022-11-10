# 《编写整洁的Python代码（第2版）》阅读笔记{docsify-ignore-all}

&emsp;&emsp;本书通过10章的内容，介绍了如何编写整洁的Python代码，并引用了著名的Python禅语，通过大量的案例讲解Python代码的优化方法，包括装饰器、描述符、生成器、迭代器、异步编程和单元测试相关的编程技巧和方法。特别喜欢书中讲述Python在设计模式中的适用性，很一般讲设计模式的书不一样，主要结合实用性介绍，并结合了很多Python内置库的设计模式应用，比如os库使用了门面模式等。

## 在线阅读地址
在线阅读地址：https://relph1119.github.io/clean-code-in-python-note

## 环境安装
### Python版本
Python 3.8.10 Windows环境

### 运行环境配置
安装相关的依赖包
```shell
pip install -r requirements.txt
```

## Python禅语

```
Beautiful is better than ugly.
优美胜过丑陋。

Explicit is better than implicit.
显示胜过隐式。

Simple is better than complex.
简单胜过复杂。

Complex is better than complicated.
复杂胜过繁复。

Flat is better than nested.
串行胜过嵌套。

Sparse is better than dense.
稀疏胜过稠密。

Readability counts.
可读性很重要。

Special cases aren't special enough to break the rules. Although practicality beats purity.
虽然理想很丰满，现实很骨感，但是所谓特例并不足以打破上面的这些规则。

Errors should never pass silently. Unless explicitly silenced.
所有错误都不应该被直接忽略，除非能够被精确的捕获之后。(其中一个典型的例子就是，不建议用Exception:pass来直接忽略所有异常。)

In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch.
当面对不明确的情况时，要拒绝去猜测的诱惑。应该有一种，最好是唯一一种，显而易见的解决方案。尽管起初，那种解决方案可能并不是那么显而易见，因为你不是Python 之父(这里的Dutch是指Python之父Guido Van Rossum，他是荷兰人。)

Now is better than never. Although never is often better than right now.
现在行动胜过永不开始。尽管，永不开始经常好过冲动的开始。

If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.
如果你的实现难于向别人解释，这往往不是个好主意。如果你的实现很容易向别人解释，这可能是个好主意。

Namespaces are one honking great idea -- let's do more of those!
命名空间是一个令人激动的伟大想法，让我们将它发扬光大。
```
