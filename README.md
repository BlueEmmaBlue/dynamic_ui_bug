# dynamic_ui_bug

## Mahimahi 最佳实践

[参考手册](http://mahimahi.mit.edu/)

**1. 环境搭建**

- 新建虚拟机，安装Ubuntu 20.04 操作系统
- 下载chromium 浏览器

**2. 安装 Mahimahi**

获取Mahimahi

```shell
sudo add-apt-repository ppa:keithw/mahimahi
sudo apt-get update
sudo apt-get install mahimahi
```

构建资源

```shell
git clone https://github.com/ravinet/mahimahi
cd mahimahi
./autogen.sh
./configure
make
sudo make install
```

录制网站，该命令会调起chromium 浏览器（这里稍微修改了下官网的命令）

- 其中`{result_dir}/{site}`是网站录制文件的保存地址，`https://www.{site}`是想要录制的网站

```shell
mm-webrecord {result_dir}/{site} chromium-browser --test-type --ignore-privacy-errors --ignore-certificate-errors --ignore-ssl-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) https://www.{site}
```

回放网站，可以设定几个网络参数

- `mm-delay`代表延迟，`mm-loss`代表丢包率，`mm-link`代表链路参数

```
mm-webreplay {result_dir}/{site} mm-delay 50 mm-loss uplink 0.1 mm-link <(echo 1) <(echo 1) -- chromium-browser --ignore-certificate-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) https://www.{site}
```

**3. 目前的问题**

- 目前通过chrome 命令不能以手机模式打开浏览器，只能指定窗口的尺寸和大小，有的网址如：谷歌，可以针对指定尺寸做移动端自适应，但有的网址如：百度，其自适应是根据UA，故不能根据尺寸自适应
    - 解决办法
        1. 屏幕录制是否要改成pc端而非移动端
        2. 只选取那些做了尺寸自适应移动端的做录屏
        3. 再改进一下数据收集的命令 doing中
