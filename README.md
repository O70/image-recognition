# Image Recognition

## Database

``` sql
create database if not exists irdb default charset utf8 collate utf8_general_ci;

drop table if exists tbl_image_metadata;
create table tbl_image_metadata (
    id varchar(36) not null primary key,
    filename varchar(64),
    filepath varchar(128),
    predict double(10, 8),
    category int,
    create_date datetime
);
```

数据库连接配置在`src/config.py`中.

## About Model

模型需要被存放至`src/core/`中, 详情请参考`src/core/model_deploy.py`中等`recognition`方法.

## Run

``` sh
$ pip install web.py==0.40
$ pip install pillow
$ pip install pymysql

$ pip install numpy opencv-python torch pandas tqdm albumentations torchvision
```

``` sh
$ python3 src/app.py 80
```

## Attentions

- `.pb`文件过大, 已被清除.

``` sh
$ git filter-branch --index-filter 'git rm --cached --ignore-unmatch static/yolov3_yanxin1000_1016.pb'
$ rm -rf .git/refs/original
$ git reflog expire --expire=now --all
$ git fsck --full --unreachable
$ git repack -A -d
$ git gc --aggressive --prune=now
$ git push --force origin master
```

- Deprecated: `Browse`

## Bugs

- `el-select`'s `describe` style
- RuntimeError('generator raised StopIteration') 
- TypeError: WSGI response header value 469 is not of type str.
- 'WSGI response header value %r is not of type str.' % v,
- TypeError: super(type, obj): obj must be an instance or subtype of type
- Deploy
