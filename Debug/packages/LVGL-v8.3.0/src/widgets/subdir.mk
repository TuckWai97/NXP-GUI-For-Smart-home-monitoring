################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../packages/LVGL-v8.3.0/src/widgets/lv_arc.c \
../packages/LVGL-v8.3.0/src/widgets/lv_bar.c \
../packages/LVGL-v8.3.0/src/widgets/lv_btn.c \
../packages/LVGL-v8.3.0/src/widgets/lv_btnmatrix.c \
../packages/LVGL-v8.3.0/src/widgets/lv_canvas.c \
../packages/LVGL-v8.3.0/src/widgets/lv_checkbox.c \
../packages/LVGL-v8.3.0/src/widgets/lv_dropdown.c \
../packages/LVGL-v8.3.0/src/widgets/lv_img.c \
../packages/LVGL-v8.3.0/src/widgets/lv_label.c \
../packages/LVGL-v8.3.0/src/widgets/lv_line.c \
../packages/LVGL-v8.3.0/src/widgets/lv_objx_templ.c \
../packages/LVGL-v8.3.0/src/widgets/lv_roller.c \
../packages/LVGL-v8.3.0/src/widgets/lv_slider.c \
../packages/LVGL-v8.3.0/src/widgets/lv_switch.c \
../packages/LVGL-v8.3.0/src/widgets/lv_table.c \
../packages/LVGL-v8.3.0/src/widgets/lv_textarea.c 

OBJS += \
./packages/LVGL-v8.3.0/src/widgets/lv_arc.o \
./packages/LVGL-v8.3.0/src/widgets/lv_bar.o \
./packages/LVGL-v8.3.0/src/widgets/lv_btn.o \
./packages/LVGL-v8.3.0/src/widgets/lv_btnmatrix.o \
./packages/LVGL-v8.3.0/src/widgets/lv_canvas.o \
./packages/LVGL-v8.3.0/src/widgets/lv_checkbox.o \
./packages/LVGL-v8.3.0/src/widgets/lv_dropdown.o \
./packages/LVGL-v8.3.0/src/widgets/lv_img.o \
./packages/LVGL-v8.3.0/src/widgets/lv_label.o \
./packages/LVGL-v8.3.0/src/widgets/lv_line.o \
./packages/LVGL-v8.3.0/src/widgets/lv_objx_templ.o \
./packages/LVGL-v8.3.0/src/widgets/lv_roller.o \
./packages/LVGL-v8.3.0/src/widgets/lv_slider.o \
./packages/LVGL-v8.3.0/src/widgets/lv_switch.o \
./packages/LVGL-v8.3.0/src/widgets/lv_table.o \
./packages/LVGL-v8.3.0/src/widgets/lv_textarea.o 

C_DEPS += \
./packages/LVGL-v8.3.0/src/widgets/lv_arc.d \
./packages/LVGL-v8.3.0/src/widgets/lv_bar.d \
./packages/LVGL-v8.3.0/src/widgets/lv_btn.d \
./packages/LVGL-v8.3.0/src/widgets/lv_btnmatrix.d \
./packages/LVGL-v8.3.0/src/widgets/lv_canvas.d \
./packages/LVGL-v8.3.0/src/widgets/lv_checkbox.d \
./packages/LVGL-v8.3.0/src/widgets/lv_dropdown.d \
./packages/LVGL-v8.3.0/src/widgets/lv_img.d \
./packages/LVGL-v8.3.0/src/widgets/lv_label.d \
./packages/LVGL-v8.3.0/src/widgets/lv_line.d \
./packages/LVGL-v8.3.0/src/widgets/lv_objx_templ.d \
./packages/LVGL-v8.3.0/src/widgets/lv_roller.d \
./packages/LVGL-v8.3.0/src/widgets/lv_slider.d \
./packages/LVGL-v8.3.0/src/widgets/lv_switch.d \
./packages/LVGL-v8.3.0/src/widgets/lv_table.d \
./packages/LVGL-v8.3.0/src/widgets/lv_textarea.d 


# Each subdirectory must supply rules for building sources it contributes
packages/LVGL-v8.3.0/src/widgets/%.o: ../packages/LVGL-v8.3.0/src/widgets/%.c
	arm-none-eabi-gcc -I"C:\RT-ThreadStudio\workspace2\GUI_contest" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl\guiguider\ui" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications\lvgl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\applications" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\MCUX_Config" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board\ports" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\board" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\CMSIS\Include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\MIMXRT1060\MIMXRT1060" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\libraries\drivers" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\env_support\rt-thread" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\core" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\arm2d" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\nxp\pxp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\nxp\vglite" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\nxp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\sdl" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\stm32_dma2d" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\swm341_dma2d" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw\sw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\draw" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\layouts\flex" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\layouts\grid" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\layouts" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\bmp" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\ffmpeg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\freetype" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\fsdrv" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\gif" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\png" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\qrcode" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\rlottie" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs\sjpg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\libs" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\fragment" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\gridnav" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\ime" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\imgfont" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\monkey" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\msg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others\snapshot" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\others" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\themes\basic" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\themes\default" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\themes\mono" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\themes" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\animimg" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\calendar" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\chart" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\colorwheel" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\imgbtn" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\keyboard" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\led" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\list" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\menu" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\meter" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\msgbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\span" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\spinbox" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\spinner" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\tabview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\tileview" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets\win" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\extra" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\font" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\hal" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\misc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src\widgets" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\LVGL-v8.3.0\src" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\gui_guider_demo-latest\custom" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\gui_guider_demo-latest\generated\guider_fonts" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\gui_guider_demo-latest\generated" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\packages\gui_guider_demo-latest" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\drivers\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\finsh" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\common\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\compilers\newlib" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\poll" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\io\stdio" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\components\libc\posix\ipc" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\include" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\common" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\rt-thread\libcpu\arm\cortex-m7" -I"C:\RT-ThreadStudio\workspace2\GUI_contest\xip" -include"C:\RT-ThreadStudio\workspace2\GUI_contest\rtconfig_preinc.h" -std=gnu11 -mcpu=cortex-m7 -mthumb -mfpu=fpv5-d16 -mfloat-abi=hard -ffunction-sections -fdata-sections -Wall -D__FPU_PRESENT -eentry -g -O0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

