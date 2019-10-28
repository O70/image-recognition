# Image Recognition

## Run

``` sh
$ python3 src/app.py
```

## Table

``` sql
drop table tbl_image_metadata;

create table tbl_image_metadata (
    id varchar(36) not null primary key,
    filename varchar(64),
    filepath varchar(128),
    predict double(10, 6),
    category int,
    create_date datetime
);
```

## Attentions

`.pb`文件过大, 已被清除.

``` sh
$ git filter-branch --index-filter 'git rm --cached --ignore-unmatch static/yolov3_yanxin1000_1016.pb'
$ rm -rf .git/refs/original
$ git reflog expire --expire=now --all
$ git fsck --full --unreachable
$ git repack -A -d
$ git gc --aggressive --prune=now
$ git push --force origin master
```

## TODO

- `rm src/test.py`
- Loading...
- Image size: x*y
- 304 Not Modified
- RuntimeError('generator raised StopIteration') 
- XML Parsing Error: syntax error
- remove https://unpkg.com
- TypeError: WSGI response header value 469 is not of type str.
- "HTTP/1.1 GET /service-worker.js" - 404 Not Found
- Deploy
