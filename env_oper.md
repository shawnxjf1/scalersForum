## 获取python 当前执行版本
>>> print(sys.path)
['/Applications/PyCharm CE.app/Contents/helpers/pydev', '/Users/shawn/eclipse_workspace_pdev_group/pdev_v1', '/Applications/PyCharm CE.app/Contents/helpers/pydev', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python26.zip', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-dynload', '/Library/Python/2.6/site-packages', '/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/PyObjC', '/Users/shawn/eclipse_workspace_pdev_group/pdev_v1']

## 与其他工程不要混合在一块(不想关的)
比如scalerforum 与LearnPythonCodeExample 等其他工程一块,可能由于其他工程的错误导致 scalerforum 工程运行也失败。
    
```
dir = os.path.join(*paths)
AttributeError: 'module' object has no attribute 'path'
```

```错误的原因
1. 命名py脚本时，不要与python预留字，模块名等相同
2. 删除该库的.pyc文件（因为py脚本每次运行时均会生成.pyc文件；在已经生成.pyc文件的情况下，若代码不更新，运行时依旧会走pyc，所以要删除.pyc文件），重新运行代码；或者找一个可以运行代码的环境，拷贝替换当前机器的.pyc文件即可
```
