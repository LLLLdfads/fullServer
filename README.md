# fullServer
## 这是一个用于使用django并完成了基本配置的、可快速实现web服务的项目（项目名fullServer，默认应用app1）
## 通过该项目你可以快速实现api测试，资源文件访问，网站构建等
## 使用步骤：
### 1.下载项目
```shell
git clone https://github.com/LLLLdfads/fullServer.git
```
### 2.安装依赖(本项目使用python3.9.7)
```shell
pip install -r requirements.txt
```
### 3.运行项目
```shell
python manage.py runserver 0.0.0.0:8000
```
## 添加接口：请在app1/views.py中添加函数，并在app1/urls.py中添加路由
## 添加资源文件：请在static文件夹中添加资源文件