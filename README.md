# kingdee
关于金蝶的一个接口调用的封装类

win+r打开命令行, 切换到python环境

输入pip install git+https://github.com/854350999/kingdee/kingdee.git@master

调用方法

```python
import kingdee as kd
cookies = kd.get_cookies(user_id, user_name, password)
post_data = {}
response = kd.save(post_data, cookies)
```
