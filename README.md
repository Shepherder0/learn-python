# Centos7安装Python3.7

### 说明

全部操作在 root 用户下执行

### 1.安装变异相关工具
```
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install libffi-devel -y
```
### 2.下载安装包并解压

