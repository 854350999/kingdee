# kingdee
关于金蝶的一个接口调用的封装类

调用方法

```python
import kingdee
kd = kingdee.Kingdee()
cookies = kd.get_cookies(user_id, user_name, password)
post_data = {}
response = kd.save(post_data, cookies)
```
