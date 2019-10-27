# Image Recognition

## Setup

Python Version: `3.7.0`

``` sh
$ pip install web.py==0.40
$ pip install tensorflow==1.13.1
$ pip install opencv-python
$ pip install pillow
$ pip install pymysql
```

## Run

``` sh
$ python src/app.py
```

## Table

``` sql
drop table tbl_image_metadata;

create table tbl_image_metadata (
    id varchar(36) not null primary key,
    original_name varchar(64),
    final_name varchar(64),
    filepath varchar(128),
    probability double(8, 2),
    category int,
    create_date datetime
);
```

## TODO

- TODO: Remove
- `rm -rf static/img`
- `rm src/test.py`
- 304 Not Modified
- RuntimeError('generator raised StopIteration') 
- XML Parsing Error: syntax error
- remove https://unpkg.com
