################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../rt-thread/src/clock.c \
../rt-thread/src/components.c \
../rt-thread/src/device.c \
../rt-thread/src/idle.c \
../rt-thread/src/ipc.c \
../rt-thread/src/irq.c \
../rt-thread/src/kservice.c \
../rt-thread/src/memheap.c \
../rt-thread/src/mempool.c \
../rt-thread/src/object.c \
../rt-thread/src/scheduler.c \
../rt-thread/src/thread.c \
../rt-thread/src/timer.c 

OBJS += \
./rt-thread/src/clock.o \
./rt-thread/src/components.o \
./rt-thread/src/device.o \
./rt-thread/src/idle.o \
./rt-thread/src/ipc.o \
./rt-thread/src/irq.o \
./rt-thread/src/kservice.o \
./rt-thread/src/memheap.o \
./rt-thread/src/mempool.o \
./rt-thread/src/object.o \
./rt-thread/src/scheduler.o \
./rt-thread/src/thread.o \
./rt-thread/src/timer.o 

C_DEPS += \
./rt-thread/src/clock.d \
./rt-thread/src/components.d \
./rt-thread/src/device.d \
./rt-thread/src/idle.d \
./rt-thread/src/ipc.d \
./rt-thread/src/irq.d \
./rt-thread/src/kservice.d \
./rt-thread/src/memheap.d \
./rt-thread/src/mempool.d \
./rt-thread/src/object.d \
./rt-thread/src/scheduler.d \
./rt-thread/src/thread.d \
./rt-thread/src/timer.d 


# Each subdirectory must supply rules for building sources it contributes
rt-thread/src/%.o: ../rt-thread/src/%.c
	arm-none-eabi-gcc -I"C:\RT-ThreadStudio\workspace2\GUI_contest" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl\guiguider\legacy" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl\guiguider\ui" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\MCUX_Config" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\ports" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\CMSIS\Include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\env_support\rt-thread" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\core" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\nxp_pxp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\nxp_vglite" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\sdl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\stm32_dma2d" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\sw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts\flex" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts\grid" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\bmp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\ffmpeg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\freetype" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\fsdrv" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\gif" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\png" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\qrcode" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\rlottie" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\sjpg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\gridnav" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\monkey" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\snapshot" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\basic" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\default" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\mono" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\animimg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\calendar" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\chart" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\colorwheel" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\imgbtn" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\keyboard" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\led" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\list" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\menu" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\meter" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\msgbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\span" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\spinbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\spinner" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\tabview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\tileview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\win" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\font" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\gpu" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\hal" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\misc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\dfs\filesystems\devfs" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\dfs\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\drivers\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\finsh" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\common\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\newlib" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\poll" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\stdio" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\ipc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\netdev\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\dfs_net" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\socket\sys_socket" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\socket" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\common" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\cortex-m7" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\xip" -include"C:\RT-ThreadStudio\workspace2\GUI_contest\rtconfig_preinc.h" -std=gnu11 -mcpu=cortex-m7 -mthumb -mfpu=fpv5-d16 -mfloat-abi=hard -ffunction-sections -fdata-sections -Wall -D__FPU_PRESENT -eentry -g -O0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

