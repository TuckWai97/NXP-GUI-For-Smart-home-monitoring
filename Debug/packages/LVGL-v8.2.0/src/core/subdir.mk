################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../packages/LVGL-v8.2.0/src/core/lv_disp.c \
../packages/LVGL-v8.2.0/src/core/lv_event.c \
../packages/LVGL-v8.2.0/src/core/lv_group.c \
../packages/LVGL-v8.2.0/src/core/lv_indev.c \
../packages/LVGL-v8.2.0/src/core/lv_indev_scroll.c \
../packages/LVGL-v8.2.0/src/core/lv_obj.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_class.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_draw.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_pos.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_scroll.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_style.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_style_gen.c \
../packages/LVGL-v8.2.0/src/core/lv_obj_tree.c \
../packages/LVGL-v8.2.0/src/core/lv_refr.c \
../packages/LVGL-v8.2.0/src/core/lv_theme.c 

OBJS += \
./packages/LVGL-v8.2.0/src/core/lv_disp.o \
./packages/LVGL-v8.2.0/src/core/lv_event.o \
./packages/LVGL-v8.2.0/src/core/lv_group.o \
./packages/LVGL-v8.2.0/src/core/lv_indev.o \
./packages/LVGL-v8.2.0/src/core/lv_indev_scroll.o \
./packages/LVGL-v8.2.0/src/core/lv_obj.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_class.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_draw.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_pos.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_scroll.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_style.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_style_gen.o \
./packages/LVGL-v8.2.0/src/core/lv_obj_tree.o \
./packages/LVGL-v8.2.0/src/core/lv_refr.o \
./packages/LVGL-v8.2.0/src/core/lv_theme.o 

C_DEPS += \
./packages/LVGL-v8.2.0/src/core/lv_disp.d \
./packages/LVGL-v8.2.0/src/core/lv_event.d \
./packages/LVGL-v8.2.0/src/core/lv_group.d \
./packages/LVGL-v8.2.0/src/core/lv_indev.d \
./packages/LVGL-v8.2.0/src/core/lv_indev_scroll.d \
./packages/LVGL-v8.2.0/src/core/lv_obj.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_class.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_draw.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_pos.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_scroll.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_style.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_style_gen.d \
./packages/LVGL-v8.2.0/src/core/lv_obj_tree.d \
./packages/LVGL-v8.2.0/src/core/lv_refr.d \
./packages/LVGL-v8.2.0/src/core/lv_theme.d 


# Each subdirectory must supply rules for building sources it contributes
packages/LVGL-v8.2.0/src/core/%.o: ../packages/LVGL-v8.2.0/src/core/%.c
	arm-none-eabi-gcc -I"C:\RT-ThreadStudio\workspace2\GUI_contest" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl\guiguider\legacy" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl\guiguider\ui" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\MCUX_Config" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\ports" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\CMSIS\Include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\env_support\rt-thread" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\core" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\nxp_pxp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\nxp_vglite" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\sdl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\stm32_dma2d" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw\sw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\draw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts\flex" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts\grid" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\layouts" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\bmp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\ffmpeg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\freetype" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\fsdrv" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\gif" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\png" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\qrcode" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\rlottie" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs\sjpg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\libs" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\gridnav" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\monkey" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others\snapshot" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\others" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\basic" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\default" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes\mono" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\themes" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\animimg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\calendar" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\chart" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\colorwheel" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\imgbtn" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\keyboard" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\led" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\list" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\menu" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\meter" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\msgbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\span" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\spinbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\spinner" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\tabview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\tileview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets\win" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\extra" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\font" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\gpu" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\hal" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\misc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.2.0\src" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\dfs\filesystems\devfs" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\dfs\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\drivers\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\finsh" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\common\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\newlib" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\poll" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\stdio" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\ipc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\netdev\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\dfs_net" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\socket\sys_socket" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include\socket" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\net\sal\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\common" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\cortex-m7" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\xip" -include"C:\RT-ThreadStudio\workspace2\GUI_contest\rtconfig_preinc.h" -std=gnu11 -mcpu=cortex-m7 -mthumb -mfpu=fpv5-d16 -mfloat-abi=hard -ffunction-sections -fdata-sections -Wall -D__FPU_PRESENT -eentry -g -O0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

