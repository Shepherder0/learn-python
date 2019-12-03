# Centos7安装Python3.7

### 说明

全部操作在 root 用户下执行

### 1.安装编译相关工具
```
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install libffi-devel -y
```
### 2.下载安装包并解压
````
cd ~/Downloads/
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar -xvJf  Python-3.7.0.tar.xz
````
### 3.编译以及安装
####  Ps:若不是在root用户下执行可能出现权限不足问题
````
mkdir /usr/local/python3  #创建编译安装目录
cd Python-3.7.3
./configure --prefix=/usr/local/python3  #此处应该有很多输出
make  #此处应该有很多输出，若出现很多no，请执行步骤1
make install  #此处应该有很多输出
````
### 4.检测是否安装成功
````
python3 -V # 若成功，应该输出当前python3的版本号Python 3.7.3
Ps:centos7会自带python2，若输入python -V，会出现python2的版本号
```` 
### 5.进入退出python
````
python3  # 出现>>> 表示进入成功
exit()  #推出python
````

