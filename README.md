# Badapple-nokia5110_Raspi
使用树莓派在Nokia5110播放badapple

代码修改自[SSD1306_RaspberryPi](https://github.com/Jackadminx/SSD1306_RaspberryPi)只是换成了[Adafruit_Nokia_LCD](https://github.com/adafruit/Adafruit_Nokia_LCD) 这个库，其他基本上没有什么大的变化

```bash
git clone https://github.com/adafruit/Adafruit_Nokia_LCD.git
cd Adafruit_Nokia_LCD
sudo python setup.py install

cd ..
git clone https://github.com/Jackadminx/Badapple-nokia5110_Raspi.git
python video.py

# 如果有依赖问题可以试试这个命令
pip install -r requirements.txt
```

有苹果的地方就有烂屏幕！ 😂