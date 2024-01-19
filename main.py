import configparser
import serial
from serial.tools import list_ports
import subprocess
import time

# UPS電源設定項目
## 電源からPCへの出力
DCD_OUTPUT_BATTERY_FINE = True
DCD_OUTPUT_BATTERY_LOW = False

# スタートアップ処理
print("### Starting UPS Battery Manager... ###")

# 再設定用リスト表示
print("[LOG] List of serial ports:")
ports = list_ports.comports()
devices = [info.device for info in ports]
for i in range(len(devices)):
  print("[LOG]   input %3d: open %s" % (i, devices[i]))

# 設定ファイル読み込み
print("[LOG] Loading settings.ini...")
inifile = configparser.ConfigParser()
inifile.read("settings.ini")
port = inifile.get("Proto1", "PORT")
timeout = int(inifile.get("Proto1", "TIMEOUT"))
baudrate = int(inifile.get("Proto1", "BAUDRATE"))
mode = inifile.get("Proto1", "MODE") # デバッグモード: debug, 通常:normal
print("[LOG] Success.")

# UPS電源のシリアルポートを確認、接続
print("[LOG] Connecting to UPS power unit...")
ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
print("[LOG] Success.")

# バッテリー監視
print("[LOG] Watching battery status...")
while True:
  # DCDピンがバッテリーの状態を示す
  is_low_battery = ser.cd
  print("[LOG] Battery State(DCD) : {}".format(is_low_battery))
  if is_low_battery == DCD_OUTPUT_BATTERY_LOW:
    # バッテリー残量が少ない事を示す
    print("[LOG] Battery Low. Sending a warning to the front ramp.")
  time.sleep(10)

ser.close()    
