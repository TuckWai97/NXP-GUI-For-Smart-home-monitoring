# NXP-GUI-For-Smart-home-monitoring
 
This project uses MIMXRT1060EVKB development board and Rocktech Displays from NXP Semiconductor.This project uses RT-Thread studio as IDE and with LVGL as graphic library with NXP GUI Guider.

I refer to the tutorial for setting up the RT Thread studio and NXP Guider

#Tutorials that helps to setup RT Thread Studio and NXP GUI Guider.

- https://github.com/OUNAVCON/RT-Thread-LVGL.

- https://www.nxp.com/docs/en/application-note/AN13694.pdf
In this link, you can refer to the GUI design for the smart home.

- To use J-link firmware to debug,refer to this link
https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1060-EVKB/ta-p/1452717
Cautions:The board used is **MIMXRT1060EVKB**, but not **MIXMRT1060EVK**, it has different pin layout compared to **MIMXRT1060EVK**.

#Technical difficulty that still not solved:
- Connects NXP MIMXRT1060EVKB via Ethernet(RJ45 port) to PC for internet access for the subscription of sensor data from ESP32 module
- ESP32 module with BME688 sensor how to publish sensor data using RT-Thread Studio via MQTT
- Connects the metrics in real time to the GUI in NXP GUI Guider
- Debugging with using onboard debugging probe needs LP4322 DFS Jumper, need to use external J-Link debug probe.
