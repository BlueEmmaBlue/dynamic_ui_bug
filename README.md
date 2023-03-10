# dynamic_ui_bug

## Mahimahi 最佳实践

[参考手册](http://mahimahi.mit.edu/)

**1. 环境搭建**

- 新建虚拟机，安装Ubuntu 20.04 操作系统
- 下载chromium 或者chrome 浏览器，以及对应浏览器版本的webdriver [下载地址](https://chromedriver.chromium.org/downloads)，放到浏览器文件夹下。

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

（可选）录制网站，该命令会调起chromium 浏览器（这里稍微修改了下官网的命令）

- 其中`{result_dir}/{site}`是网站录制文件的保存地址，`https://www.{site}`是想要录制的网站

```shell
mm-webrecord {result_dir}/{site} chromium-browser --test-type --ignore-privacy-errors --ignore-certificate-errors --ignore-ssl-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) https://www.{site}
```

（可选）回放网站，可以设定几个网络参数

- `mm-delay`代表延迟，`mm-loss`代表丢包率，`mm-link`代表链路参数

```
mm-webreplay {result_dir}/{site} mm-delay 50 mm-loss uplink 0.1 mm-link <(echo 1) <(echo 1) -- chromium-browser --ignore-certificate-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) https://www.{site}
```

**3. 遍历录制网站并截屏**

1. 修改`screee_shot.py`中的两个路径参数
```python
DRIVER_PATH = '/home/zhangwei/utils/chromium/chromedriver' # webdriver 路径
SCREEN_SHOT_PATH = '/home/zhangwei/code/result' # 保存录制内容的路径
```

2. 运行`mahimahi.py`

```shell
python mahimahi.py
```

3. 查看保存路径中的内容，看看截屏和保存的网站文件即可知道网站是否成功打开！