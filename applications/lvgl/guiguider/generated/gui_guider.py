# Copyright 2022 NXP
# SPDX-License-Identifier: MIT
# The auto-generated can only be used on NXP devices

import SDL
import utime as time
import usys as sys
import lvgl as lv
import lodepng as png
import ustruct

lv.init()
SDL.init(w=480,h=272)

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 272
disp_drv.register()

# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()

# Below: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

COLOR_SIZE = lv.color_t.__SIZE__
COLOR_IS_SWAPPED = hasattr(lv.color_t().ch,'green_h')

class lodepng_error(RuntimeError):
    def __init__(self, err):
        if type(err) is int:
            super().__init__(png.error_text(err))
        else:
            super().__init__(err)

# Parse PNG file header
# Taken from https://github.com/shibukawa/imagesize_py/blob/ffef30c1a4715c5acf90e8945ceb77f4a2ed2d45/imagesize.py#L63-L85

def get_png_info(decoder, src, header):
    # Only handle variable image types

    if lv.img.src_get_type(src) != lv.img.SRC.VARIABLE:
        return lv.RES.INV

    data = lv.img_dsc_t.__cast__(src).data
    if data == None:
        return lv.RES.INV

    png_header = bytes(data.__dereference__(24))

    if png_header.startswith(b'\211PNG\r\n\032\n'):
        if png_header[12:16] == b'IHDR':
            start = 16
        # Maybe this is for an older PNG version.
        else:
            start = 8
        try:
            width, height = ustruct.unpack(">LL", png_header[start:start+8])
        except ustruct.error:
            return lv.RES.INV
    else:
        return lv.RES.INV

    header.always_zero = 0
    header.w = width
    header.h = height
    header.cf = lv.img.CF.TRUE_COLOR_ALPHA

    return lv.RES.OK

def convert_rgba8888_to_bgra8888(img_view):
    for i in range(0, len(img_view), lv.color_t.__SIZE__):
        ch = lv.color_t.__cast__(img_view[i:i]).ch
        ch.red, ch.blue = ch.blue, ch.red

# Read and parse PNG file

def open_png(decoder, dsc):
    img_dsc = lv.img_dsc_t.__cast__(dsc.src)
    png_data = img_dsc.data
    png_size = img_dsc.data_size
    png_decoded = png.C_Pointer()
    png_width = png.C_Pointer()
    png_height = png.C_Pointer()
    error = png.decode32(png_decoded, png_width, png_height, png_data, png_size)
    if error:
        raise lodepng_error(error)
    img_size = png_width.int_val * png_height.int_val * 4
    img_data = png_decoded.ptr_val
    img_view = img_data.__dereference__(img_size)

    if COLOR_SIZE == 4:
        convert_rgba8888_to_bgra8888(img_view)
    else:
        raise lodepng_error("Error: Color mode not supported yet!")

    dsc.img_data = img_data
    return lv.RES.OK

# Above: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)


home_screen = lv.obj()
home_screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_home_screen_main_main_default
style_home_screen_main_main_default = lv.style_t()
style_home_screen_main_main_default.init()
style_home_screen_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_home_screen_main_main_default.set_bg_opa(0)

# add style for home_screen
home_screen.add_style(style_home_screen_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_cont1 = lv.obj(home_screen)
home_screen_cont1.set_pos(int(0),int(0))
home_screen_cont1.set_size(480,95)
home_screen_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_home_screen_cont1_main_main_default
style_home_screen_cont1_main_main_default = lv.style_t()
style_home_screen_cont1_main_main_default.init()
style_home_screen_cont1_main_main_default.set_radius(0)
style_home_screen_cont1_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_home_screen_cont1_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_home_screen_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_cont1_main_main_default.set_bg_opa(255)
style_home_screen_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_home_screen_cont1_main_main_default.set_border_width(0)
style_home_screen_cont1_main_main_default.set_border_opa(255)
style_home_screen_cont1_main_main_default.set_pad_left(0)
style_home_screen_cont1_main_main_default.set_pad_right(0)
style_home_screen_cont1_main_main_default.set_pad_top(0)
style_home_screen_cont1_main_main_default.set_pad_bottom(0)

# add style for home_screen_cont1
home_screen_cont1.add_style(style_home_screen_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_whitebg = lv.obj(home_screen)
home_screen_whitebg.set_pos(int(0),int(96))
home_screen_whitebg.set_size(480,177)
home_screen_whitebg.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_home_screen_whitebg_main_main_default
style_home_screen_whitebg_main_main_default = lv.style_t()
style_home_screen_whitebg_main_main_default.init()
style_home_screen_whitebg_main_main_default.set_radius(0)
style_home_screen_whitebg_main_main_default.set_bg_color(lv.color_make(0xd6,0xdc,0xd6))
style_home_screen_whitebg_main_main_default.set_bg_grad_color(lv.color_make(0xd9,0xd9,0xd9))
style_home_screen_whitebg_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_whitebg_main_main_default.set_bg_opa(255)
style_home_screen_whitebg_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_home_screen_whitebg_main_main_default.set_border_width(0)
style_home_screen_whitebg_main_main_default.set_border_opa(255)
style_home_screen_whitebg_main_main_default.set_pad_left(0)
style_home_screen_whitebg_main_main_default.set_pad_right(0)
style_home_screen_whitebg_main_main_default.set_pad_top(0)
style_home_screen_whitebg_main_main_default.set_pad_bottom(0)

# add style for home_screen_whitebg
home_screen_whitebg.add_style(style_home_screen_whitebg_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_cont2 = lv.obj(home_screen)
home_screen_cont2.set_pos(int(40),int(80))
home_screen_cont2.set_size(380,120)
home_screen_cont2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_home_screen_cont2_main_main_default
style_home_screen_cont2_main_main_default = lv.style_t()
style_home_screen_cont2_main_main_default.init()
style_home_screen_cont2_main_main_default.set_radius(0)
style_home_screen_cont2_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_home_screen_cont2_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_home_screen_cont2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_cont2_main_main_default.set_bg_opa(255)
style_home_screen_cont2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_home_screen_cont2_main_main_default.set_border_width(0)
style_home_screen_cont2_main_main_default.set_border_opa(255)
style_home_screen_cont2_main_main_default.set_pad_left(0)
style_home_screen_cont2_main_main_default.set_pad_right(0)
style_home_screen_cont2_main_main_default.set_pad_top(0)
style_home_screen_cont2_main_main_default.set_pad_bottom(0)

# add style for home_screen_cont2
home_screen_cont2.add_style(style_home_screen_cont2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_imgbtn_surve = lv.imgbtn(home_screen)
home_screen_imgbtn_surve.set_pos(int(320),int(86))
home_screen_imgbtn_surve.set_size(96,100)
home_screen_imgbtn_surve.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png','rb') as f:
        home_screen_imgbtn_surve_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png')
    sys.exit()

home_screen_imgbtn_surve_imgReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_surve_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_surve_imgReleased_data
})
home_screen_imgbtn_surve.set_src(lv.imgbtn.STATE.RELEASED, home_screen_imgbtn_surve_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png','rb') as f:
        home_screen_imgbtn_surve_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png')
    sys.exit()

home_screen_imgbtn_surve_imgPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_surve_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_surve_imgPressed_data
})
home_screen_imgbtn_surve.set_src(lv.imgbtn.STATE.PRESSED, home_screen_imgbtn_surve_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png','rb') as f:
        home_screen_imgbtn_surve_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png')
    sys.exit()

home_screen_imgbtn_surve_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_surve_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_surve_imgCheckedReleased_data
})
home_screen_imgbtn_surve.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, home_screen_imgbtn_surve_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png','rb') as f:
        home_screen_imgbtn_surve_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp934719295.png')
    sys.exit()

home_screen_imgbtn_surve_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_surve_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_surve_imgCheckedPressed_data
})
home_screen_imgbtn_surve.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, home_screen_imgbtn_surve_imgCheckedPressed, None, None)

# create style style_home_screen_imgbtn_surve_main_main_default
style_home_screen_imgbtn_surve_main_main_default = lv.style_t()
style_home_screen_imgbtn_surve_main_main_default.init()
style_home_screen_imgbtn_surve_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_home_screen_imgbtn_surve_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_imgbtn_surve_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_imgbtn_surve_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_surve_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_surve_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgbtn_surve_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgbtn_surve_main_main_default.set_img_opa(255)

# add style for home_screen_imgbtn_surve
home_screen_imgbtn_surve.add_style(style_home_screen_imgbtn_surve_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_home_screen_imgbtn_surve_main_main_pressed
style_home_screen_imgbtn_surve_main_main_pressed = lv.style_t()
style_home_screen_imgbtn_surve_main_main_pressed.init()
style_home_screen_imgbtn_surve_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_surve_main_main_pressed.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_surve_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_surve_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_surve_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_surve_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_surve_main_main_pressed.set_img_recolor_opa(0)
style_home_screen_imgbtn_surve_main_main_pressed.set_img_opa(255)

# add style for home_screen_imgbtn_surve
home_screen_imgbtn_surve.add_style(style_home_screen_imgbtn_surve_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_home_screen_imgbtn_surve_main_main_checked
style_home_screen_imgbtn_surve_main_main_checked = lv.style_t()
style_home_screen_imgbtn_surve_main_main_checked.init()
style_home_screen_imgbtn_surve_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_surve_main_main_checked.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_surve_main_main_checked.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_surve_main_main_checked.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_surve_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_surve_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_surve_main_main_checked.set_img_recolor_opa(0)
style_home_screen_imgbtn_surve_main_main_checked.set_img_opa(255)

# add style for home_screen_imgbtn_surve
home_screen_imgbtn_surve.add_style(style_home_screen_imgbtn_surve_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

home_screen_imgbtn_humid = lv.imgbtn(home_screen)
home_screen_imgbtn_humid.set_pos(int(139),int(87))
home_screen_imgbtn_humid.set_size(96,100)
home_screen_imgbtn_humid.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        home_screen_imgbtn_humid_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

home_screen_imgbtn_humid_imgReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_humid_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_humid_imgReleased_data
})
home_screen_imgbtn_humid.set_src(lv.imgbtn.STATE.RELEASED, home_screen_imgbtn_humid_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        home_screen_imgbtn_humid_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

home_screen_imgbtn_humid_imgPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_humid_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_humid_imgPressed_data
})
home_screen_imgbtn_humid.set_src(lv.imgbtn.STATE.PRESSED, home_screen_imgbtn_humid_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        home_screen_imgbtn_humid_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

home_screen_imgbtn_humid_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_humid_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_humid_imgCheckedReleased_data
})
home_screen_imgbtn_humid.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, home_screen_imgbtn_humid_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        home_screen_imgbtn_humid_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

home_screen_imgbtn_humid_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_humid_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_humid_imgCheckedPressed_data
})
home_screen_imgbtn_humid.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, home_screen_imgbtn_humid_imgCheckedPressed, None, None)

# create style style_home_screen_imgbtn_humid_main_main_default
style_home_screen_imgbtn_humid_main_main_default = lv.style_t()
style_home_screen_imgbtn_humid_main_main_default.init()
style_home_screen_imgbtn_humid_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_home_screen_imgbtn_humid_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_imgbtn_humid_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_imgbtn_humid_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_humid_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_humid_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgbtn_humid_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgbtn_humid_main_main_default.set_img_opa(255)

# add style for home_screen_imgbtn_humid
home_screen_imgbtn_humid.add_style(style_home_screen_imgbtn_humid_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_home_screen_imgbtn_humid_main_main_pressed
style_home_screen_imgbtn_humid_main_main_pressed = lv.style_t()
style_home_screen_imgbtn_humid_main_main_pressed.init()
style_home_screen_imgbtn_humid_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_humid_main_main_pressed.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_humid_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_humid_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_humid_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_humid_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_humid_main_main_pressed.set_img_recolor_opa(0)
style_home_screen_imgbtn_humid_main_main_pressed.set_img_opa(255)

# add style for home_screen_imgbtn_humid
home_screen_imgbtn_humid.add_style(style_home_screen_imgbtn_humid_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_home_screen_imgbtn_humid_main_main_checked
style_home_screen_imgbtn_humid_main_main_checked = lv.style_t()
style_home_screen_imgbtn_humid_main_main_checked.init()
style_home_screen_imgbtn_humid_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_humid_main_main_checked.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_humid_main_main_checked.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_humid_main_main_checked.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_humid_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_humid_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_humid_main_main_checked.set_img_recolor_opa(0)
style_home_screen_imgbtn_humid_main_main_checked.set_img_opa(255)

# add style for home_screen_imgbtn_humid
home_screen_imgbtn_humid.add_style(style_home_screen_imgbtn_humid_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

home_screen_imgbtn_fanlght = lv.imgbtn(home_screen)
home_screen_imgbtn_fanlght.set_pos(int(230),int(86))
home_screen_imgbtn_fanlght.set_size(96,100)
home_screen_imgbtn_fanlght.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        home_screen_imgbtn_fanlght_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

home_screen_imgbtn_fanlght_imgReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_fanlght_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_fanlght_imgReleased_data
})
home_screen_imgbtn_fanlght.set_src(lv.imgbtn.STATE.RELEASED, home_screen_imgbtn_fanlght_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        home_screen_imgbtn_fanlght_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

home_screen_imgbtn_fanlght_imgPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_fanlght_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_fanlght_imgPressed_data
})
home_screen_imgbtn_fanlght.set_src(lv.imgbtn.STATE.PRESSED, home_screen_imgbtn_fanlght_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        home_screen_imgbtn_fanlght_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

home_screen_imgbtn_fanlght_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_fanlght_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_fanlght_imgCheckedReleased_data
})
home_screen_imgbtn_fanlght.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, home_screen_imgbtn_fanlght_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        home_screen_imgbtn_fanlght_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

home_screen_imgbtn_fanlght_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(home_screen_imgbtn_fanlght_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgbtn_fanlght_imgCheckedPressed_data
})
home_screen_imgbtn_fanlght.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, home_screen_imgbtn_fanlght_imgCheckedPressed, None, None)

# create style style_home_screen_imgbtn_fanlght_main_main_default
style_home_screen_imgbtn_fanlght_main_main_default = lv.style_t()
style_home_screen_imgbtn_fanlght_main_main_default.init()
style_home_screen_imgbtn_fanlght_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_home_screen_imgbtn_fanlght_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_imgbtn_fanlght_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_imgbtn_fanlght_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_fanlght_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_fanlght_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgbtn_fanlght_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgbtn_fanlght_main_main_default.set_img_opa(255)

# add style for home_screen_imgbtn_fanlght
home_screen_imgbtn_fanlght.add_style(style_home_screen_imgbtn_fanlght_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_home_screen_imgbtn_fanlght_main_main_pressed
style_home_screen_imgbtn_fanlght_main_main_pressed = lv.style_t()
style_home_screen_imgbtn_fanlght_main_main_pressed.init()
style_home_screen_imgbtn_fanlght_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_fanlght_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_fanlght_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_fanlght_main_main_pressed.set_img_recolor_opa(0)
style_home_screen_imgbtn_fanlght_main_main_pressed.set_img_opa(255)

# add style for home_screen_imgbtn_fanlght
home_screen_imgbtn_fanlght.add_style(style_home_screen_imgbtn_fanlght_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_home_screen_imgbtn_fanlght_main_main_checked
style_home_screen_imgbtn_fanlght_main_main_checked = lv.style_t()
style_home_screen_imgbtn_fanlght_main_main_checked.init()
style_home_screen_imgbtn_fanlght_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_home_screen_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_home_screen_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_montserrat_16)
style_home_screen_imgbtn_fanlght_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_imgbtn_fanlght_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_imgbtn_fanlght_main_main_checked.set_img_recolor_opa(0)
style_home_screen_imgbtn_fanlght_main_main_checked.set_img_opa(255)

# add style for home_screen_imgbtn_fanlght
home_screen_imgbtn_fanlght.add_style(style_home_screen_imgbtn_fanlght_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

home_screen_img_fan = lv.img(home_screen)
home_screen_img_fan.set_pos(int(249),int(107))
home_screen_img_fan.set_size(31,29)
home_screen_img_fan.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_img_fan.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1980422287.png','rb') as f:
        home_screen_img_fan_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1980422287.png')
    sys.exit()

home_screen_img_fan_img = lv.img_dsc_t({
  'data_size': len(home_screen_img_fan_img_data),
  'header': {'always_zero': 0, 'w': 31, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_img_fan_img_data
})

home_screen_img_fan.set_src(home_screen_img_fan_img)
home_screen_img_fan.set_pivot(0,0)
home_screen_img_fan.set_angle(0)
# create style style_home_screen_img_fan_main_main_default
style_home_screen_img_fan_main_main_default = lv.style_t()
style_home_screen_img_fan_main_main_default.init()
style_home_screen_img_fan_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_img_fan_main_main_default.set_img_recolor_opa(0)
style_home_screen_img_fan_main_main_default.set_img_opa(255)

# add style for home_screen_img_fan
home_screen_img_fan.add_style(style_home_screen_img_fan_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_labelhumid = lv.label(home_screen)
home_screen_labelhumid.set_pos(int(153),int(148))
home_screen_labelhumid.set_size(67,20)
home_screen_labelhumid.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_labelhumid.set_text("Humidity")
home_screen_labelhumid.set_long_mode(lv.label.LONG.WRAP)
# create style style_home_screen_labelhumid_main_main_default
style_home_screen_labelhumid_main_main_default = lv.style_t()
style_home_screen_labelhumid_main_main_default.init()
style_home_screen_labelhumid_main_main_default.set_radius(0)
style_home_screen_labelhumid_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelhumid_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelhumid_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_labelhumid_main_main_default.set_bg_opa(0)
style_home_screen_labelhumid_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_home_screen_labelhumid_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_labelhumid_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_labelhumid_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_labelhumid_main_main_default.set_text_letter_space(1)
style_home_screen_labelhumid_main_main_default.set_text_line_space(0)
style_home_screen_labelhumid_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_labelhumid_main_main_default.set_pad_left(0)
style_home_screen_labelhumid_main_main_default.set_pad_right(0)
style_home_screen_labelhumid_main_main_default.set_pad_top(0)
style_home_screen_labelhumid_main_main_default.set_pad_bottom(0)

# add style for home_screen_labelhumid
home_screen_labelhumid.add_style(style_home_screen_labelhumid_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_labelfanlight = lv.label(home_screen)
home_screen_labelfanlight.set_pos(int(242),int(138))
home_screen_labelfanlight.set_size(75,36)
home_screen_labelfanlight.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_labelfanlight.set_text("Fan & Light operation time")
home_screen_labelfanlight.set_long_mode(lv.label.LONG.WRAP)
# create style style_home_screen_labelfanlight_main_main_default
style_home_screen_labelfanlight_main_main_default = lv.style_t()
style_home_screen_labelfanlight_main_main_default.init()
style_home_screen_labelfanlight_main_main_default.set_radius(0)
style_home_screen_labelfanlight_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelfanlight_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelfanlight_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_labelfanlight_main_main_default.set_bg_opa(0)
style_home_screen_labelfanlight_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_home_screen_labelfanlight_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_labelfanlight_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_labelfanlight_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_labelfanlight_main_main_default.set_text_letter_space(1)
style_home_screen_labelfanlight_main_main_default.set_text_line_space(0)
style_home_screen_labelfanlight_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_labelfanlight_main_main_default.set_pad_left(0)
style_home_screen_labelfanlight_main_main_default.set_pad_right(0)
style_home_screen_labelfanlight_main_main_default.set_pad_top(0)
style_home_screen_labelfanlight_main_main_default.set_pad_bottom(0)

# add style for home_screen_labelfanlight
home_screen_labelfanlight.add_style(style_home_screen_labelfanlight_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_labelsurvel = lv.label(home_screen)
home_screen_labelsurvel.set_pos(int(326),int(148))
home_screen_labelsurvel.set_size(84,21)
home_screen_labelsurvel.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_labelsurvel.set_text("Surveillance")
home_screen_labelsurvel.set_long_mode(lv.label.LONG.WRAP)
# create style style_home_screen_labelsurvel_main_main_default
style_home_screen_labelsurvel_main_main_default = lv.style_t()
style_home_screen_labelsurvel_main_main_default.init()
style_home_screen_labelsurvel_main_main_default.set_radius(0)
style_home_screen_labelsurvel_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelsurvel_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_home_screen_labelsurvel_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_home_screen_labelsurvel_main_main_default.set_bg_opa(0)
style_home_screen_labelsurvel_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_home_screen_labelsurvel_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_labelsurvel_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_labelsurvel_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_labelsurvel_main_main_default.set_text_letter_space(1)
style_home_screen_labelsurvel_main_main_default.set_text_line_space(0)
style_home_screen_labelsurvel_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_labelsurvel_main_main_default.set_pad_left(0)
style_home_screen_labelsurvel_main_main_default.set_pad_right(0)
style_home_screen_labelsurvel_main_main_default.set_pad_top(0)
style_home_screen_labelsurvel_main_main_default.set_pad_bottom(0)

# add style for home_screen_labelsurvel
home_screen_labelsurvel.add_style(style_home_screen_labelsurvel_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_imgcopy = lv.img(home_screen)
home_screen_imgcopy.set_pos(int(90),int(108))
home_screen_imgcopy.set_size(29,29)
home_screen_imgcopy.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_imgcopy.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1651069706.png','rb') as f:
        home_screen_imgcopy_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1651069706.png')
    sys.exit()

home_screen_imgcopy_img = lv.img_dsc_t({
  'data_size': len(home_screen_imgcopy_img_data),
  'header': {'always_zero': 0, 'w': 29, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgcopy_img_data
})

home_screen_imgcopy.set_src(home_screen_imgcopy_img)
home_screen_imgcopy.set_pivot(0,0)
home_screen_imgcopy.set_angle(0)
# create style style_home_screen_imgcopy_main_main_default
style_home_screen_imgcopy_main_main_default = lv.style_t()
style_home_screen_imgcopy_main_main_default.init()
style_home_screen_imgcopy_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgcopy_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgcopy_main_main_default.set_img_opa(255)

# add style for home_screen_imgcopy
home_screen_imgcopy.add_style(style_home_screen_imgcopy_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_imgscan = lv.img(home_screen)
home_screen_imgscan.set_pos(int(183),int(108))
home_screen_imgscan.set_size(29,29)
home_screen_imgscan.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_imgscan.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp751764168.png','rb') as f:
        home_screen_imgscan_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp751764168.png')
    sys.exit()

home_screen_imgscan_img = lv.img_dsc_t({
  'data_size': len(home_screen_imgscan_img_data),
  'header': {'always_zero': 0, 'w': 29, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgscan_img_data
})

home_screen_imgscan.set_src(home_screen_imgscan_img)
home_screen_imgscan.set_pivot(0,0)
home_screen_imgscan.set_angle(-10)
# create style style_home_screen_imgscan_main_main_default
style_home_screen_imgscan_main_main_default = lv.style_t()
style_home_screen_imgscan_main_main_default.init()
style_home_screen_imgscan_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgscan_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgscan_main_main_default.set_img_opa(255)

# add style for home_screen_imgscan
home_screen_imgscan.add_style(style_home_screen_imgscan_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_imglight = lv.img(home_screen)
home_screen_imglight.set_pos(int(280),int(107))
home_screen_imglight.set_size(31,29)
home_screen_imglight.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_imglight.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1521194444.png','rb') as f:
        home_screen_imglight_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1521194444.png')
    sys.exit()

home_screen_imglight_img = lv.img_dsc_t({
  'data_size': len(home_screen_imglight_img_data),
  'header': {'always_zero': 0, 'w': 31, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imglight_img_data
})

home_screen_imglight.set_src(home_screen_imglight_img)
home_screen_imglight.set_pivot(0,0)
home_screen_imglight.set_angle(0)
# create style style_home_screen_imglight_main_main_default
style_home_screen_imglight_main_main_default = lv.style_t()
style_home_screen_imglight_main_main_default.init()
style_home_screen_imglight_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imglight_main_main_default.set_img_recolor_opa(0)
style_home_screen_imglight_main_main_default.set_img_opa(255)

# add style for home_screen_imglight
home_screen_imglight.add_style(style_home_screen_imglight_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_imgsurve = lv.img(home_screen)
home_screen_imgsurve.set_pos(int(360),int(108))
home_screen_imgsurve.set_size(29,29)
home_screen_imgsurve.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_imgsurve.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp762376055.png','rb') as f:
        home_screen_imgsurve_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp762376055.png')
    sys.exit()

home_screen_imgsurve_img = lv.img_dsc_t({
  'data_size': len(home_screen_imgsurve_img_data),
  'header': {'always_zero': 0, 'w': 29, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_imgsurve_img_data
})

home_screen_imgsurve.set_src(home_screen_imgsurve_img)
home_screen_imgsurve.set_pivot(0,0)
home_screen_imgsurve.set_angle(0)
# create style style_home_screen_imgsurve_main_main_default
style_home_screen_imgsurve_main_main_default = lv.style_t()
style_home_screen_imgsurve_main_main_default.init()
style_home_screen_imgsurve_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_imgsurve_main_main_default.set_img_recolor_opa(0)
style_home_screen_imgsurve_main_main_default.set_img_opa(255)

# add style for home_screen_imgsurve
home_screen_imgsurve.add_style(style_home_screen_imgsurve_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_temp_but = lv.imgbtn(home_screen)
home_screen_temp_but.set_pos(int(51),int(87))
home_screen_temp_but.set_size(96,100)
home_screen_temp_but.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png','rb') as f:
        home_screen_temp_but_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png')
    sys.exit()

home_screen_temp_but_imgReleased = lv.img_dsc_t({
  'data_size': len(home_screen_temp_but_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_temp_but_imgReleased_data
})
home_screen_temp_but.set_src(lv.imgbtn.STATE.RELEASED, home_screen_temp_but_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png','rb') as f:
        home_screen_temp_but_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png')
    sys.exit()

home_screen_temp_but_imgPressed = lv.img_dsc_t({
  'data_size': len(home_screen_temp_but_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_temp_but_imgPressed_data
})
home_screen_temp_but.set_src(lv.imgbtn.STATE.PRESSED, home_screen_temp_but_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png','rb') as f:
        home_screen_temp_but_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png')
    sys.exit()

home_screen_temp_but_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(home_screen_temp_but_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_temp_but_imgCheckedReleased_data
})
home_screen_temp_but.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, home_screen_temp_but_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png','rb') as f:
        home_screen_temp_but_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1197151133.png')
    sys.exit()

home_screen_temp_but_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(home_screen_temp_but_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_temp_but_imgCheckedPressed_data
})
home_screen_temp_but.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, home_screen_temp_but_imgCheckedPressed, None, None)

# create style style_home_screen_temp_but_main_main_default
style_home_screen_temp_but_main_main_default = lv.style_t()
style_home_screen_temp_but_main_main_default.init()
style_home_screen_temp_but_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_home_screen_temp_but_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_temp_but_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_temp_but_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_temp_but_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_temp_but_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_temp_but_main_main_default.set_img_recolor_opa(0)
style_home_screen_temp_but_main_main_default.set_img_opa(255)

# add style for home_screen_temp_but
home_screen_temp_but.add_style(style_home_screen_temp_but_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_home_screen_temp_but_main_main_pressed
style_home_screen_temp_but_main_main_pressed = lv.style_t()
style_home_screen_temp_but_main_main_pressed.init()
style_home_screen_temp_but_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_temp_but_main_main_pressed.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_home_screen_temp_but_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_temp_but_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_home_screen_temp_but_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_temp_but_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_temp_but_main_main_pressed.set_img_recolor_opa(0)
style_home_screen_temp_but_main_main_pressed.set_img_opa(255)

# add style for home_screen_temp_but
home_screen_temp_but.add_style(style_home_screen_temp_but_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_home_screen_temp_but_main_main_checked
style_home_screen_temp_but_main_main_checked = lv.style_t()
style_home_screen_temp_but_main_main_checked.init()
style_home_screen_temp_but_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_home_screen_temp_but_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_home_screen_temp_but_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_temp_but_main_main_checked.set_text_font(lv.font_montserrat_16)
style_home_screen_temp_but_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_temp_but_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_home_screen_temp_but_main_main_checked.set_img_recolor_opa(0)
style_home_screen_temp_but_main_main_checked.set_img_opa(255)

# add style for home_screen_temp_but
home_screen_temp_but.add_style(style_home_screen_temp_but_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

home_screen_label_2 = lv.label(home_screen)
home_screen_label_2.set_pos(int(60),int(143))
home_screen_label_2.set_size(79,13)
home_screen_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_label_2.set_text("Temperature")
home_screen_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_home_screen_label_2_main_main_default
style_home_screen_label_2_main_main_default = lv.style_t()
style_home_screen_label_2_main_main_default.init()
style_home_screen_label_2_main_main_default.set_radius(0)
style_home_screen_label_2_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_home_screen_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_home_screen_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_home_screen_label_2_main_main_default.set_bg_opa(0)
style_home_screen_label_2_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_home_screen_label_2_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_label_2_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_label_2_main_main_default.set_text_letter_space(1)
style_home_screen_label_2_main_main_default.set_text_line_space(0)
style_home_screen_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_label_2_main_main_default.set_pad_left(0)
style_home_screen_label_2_main_main_default.set_pad_right(0)
style_home_screen_label_2_main_main_default.set_pad_top(0)
style_home_screen_label_2_main_main_default.set_pad_bottom(0)

# add style for home_screen_label_2
home_screen_label_2.add_style(style_home_screen_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_img_1 = lv.img(home_screen)
home_screen_img_1.set_pos(int(97),int(103))
home_screen_img_1.set_size(29,29)
home_screen_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-2083852933.png','rb') as f:
        home_screen_img_1_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-2083852933.png')
    sys.exit()

home_screen_img_1_img = lv.img_dsc_t({
  'data_size': len(home_screen_img_1_img_data),
  'header': {'always_zero': 0, 'w': 29, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': home_screen_img_1_img_data
})

home_screen_img_1.set_src(home_screen_img_1_img)
home_screen_img_1.set_pivot(0,0)
home_screen_img_1.set_angle(0)
# create style style_home_screen_img_1_main_main_default
style_home_screen_img_1_main_main_default = lv.style_t()
style_home_screen_img_1_main_main_default.init()
style_home_screen_img_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_home_screen_img_1_main_main_default.set_img_recolor_opa(0)
style_home_screen_img_1_main_main_default.set_img_opa(255)

# add style for home_screen_img_1
home_screen_img_1.add_style(style_home_screen_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

home_screen_label_3 = lv.label(home_screen)
home_screen_label_3.set_pos(int(12),int(24))
home_screen_label_3.set_size(456,33)
home_screen_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
home_screen_label_3.set_text("Hello welcome to smart home monitoring!")
home_screen_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_home_screen_label_3_main_main_default
style_home_screen_label_3_main_main_default = lv.style_t()
style_home_screen_label_3_main_main_default.init()
style_home_screen_label_3_main_main_default.set_radius(0)
style_home_screen_label_3_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_home_screen_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_home_screen_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_home_screen_label_3_main_main_default.set_bg_opa(0)
style_home_screen_label_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_home_screen_label_3_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_home_screen_label_3_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_home_screen_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_home_screen_label_3_main_main_default.set_text_letter_space(2)
style_home_screen_label_3_main_main_default.set_text_line_space(0)
style_home_screen_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_home_screen_label_3_main_main_default.set_pad_left(0)
style_home_screen_label_3_main_main_default.set_pad_right(0)
style_home_screen_label_3_main_main_default.set_pad_top(0)
style_home_screen_label_3_main_main_default.set_pad_bottom(0)

# add style for home_screen_label_3
home_screen_label_3.add_style(style_home_screen_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp = lv.obj()
scrTemp.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrtemp_main_main_default
style_scrtemp_main_main_default = lv.style_t()
style_scrtemp_main_main_default.init()
style_scrtemp_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_main_main_default.set_bg_opa(0)

# add style for scrTemp
scrTemp.add_style(style_scrtemp_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_cont0 = lv.obj(scrTemp)
scrTemp_cont0.set_pos(int(0),int(0))
scrTemp_cont0.set_size(480,33)
scrTemp_cont0.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrtemp_cont0_main_main_default
style_scrtemp_cont0_main_main_default = lv.style_t()
style_scrtemp_cont0_main_main_default.init()
style_scrtemp_cont0_main_main_default.set_radius(0)
style_scrtemp_cont0_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_scrtemp_cont0_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_scrtemp_cont0_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_cont0_main_main_default.set_bg_opa(255)
style_scrtemp_cont0_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrtemp_cont0_main_main_default.set_border_width(0)
style_scrtemp_cont0_main_main_default.set_border_opa(255)
style_scrtemp_cont0_main_main_default.set_pad_left(0)
style_scrtemp_cont0_main_main_default.set_pad_right(0)
style_scrtemp_cont0_main_main_default.set_pad_top(0)
style_scrtemp_cont0_main_main_default.set_pad_bottom(0)

# add style for scrTemp_cont0
scrTemp_cont0.add_style(style_scrtemp_cont0_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_con2 = lv.obj(scrTemp)
scrTemp_con2.set_pos(int(0),int(15))
scrTemp_con2.set_size(480,252)
scrTemp_con2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrtemp_con2_main_main_default
style_scrtemp_con2_main_main_default = lv.style_t()
style_scrtemp_con2_main_main_default.init()
style_scrtemp_con2_main_main_default.set_radius(0)
style_scrtemp_con2_main_main_default.set_bg_color(lv.color_make(0xde,0xde,0xde))
style_scrtemp_con2_main_main_default.set_bg_grad_color(lv.color_make(0xde,0xde,0xde))
style_scrtemp_con2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_con2_main_main_default.set_bg_opa(255)
style_scrtemp_con2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrtemp_con2_main_main_default.set_border_width(0)
style_scrtemp_con2_main_main_default.set_border_opa(255)
style_scrtemp_con2_main_main_default.set_pad_left(0)
style_scrtemp_con2_main_main_default.set_pad_right(0)
style_scrtemp_con2_main_main_default.set_pad_top(0)
style_scrtemp_con2_main_main_default.set_pad_bottom(0)

# add style for scrTemp_con2
scrTemp_con2.add_style(style_scrtemp_con2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_cont1 = lv.obj(scrTemp)
scrTemp_cont1.set_pos(int(40),int(60))
scrTemp_cont1.set_size(400,140)
scrTemp_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrtemp_cont1_main_main_default
style_scrtemp_cont1_main_main_default = lv.style_t()
style_scrtemp_cont1_main_main_default.init()
style_scrtemp_cont1_main_main_default.set_radius(0)
style_scrtemp_cont1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_cont1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_cont1_main_main_default.set_bg_opa(255)
style_scrtemp_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrtemp_cont1_main_main_default.set_border_width(0)
style_scrtemp_cont1_main_main_default.set_border_opa(255)
style_scrtemp_cont1_main_main_default.set_pad_left(0)
style_scrtemp_cont1_main_main_default.set_pad_right(0)
style_scrtemp_cont1_main_main_default.set_pad_top(0)
style_scrtemp_cont1_main_main_default.set_pad_bottom(0)

# add style for scrTemp_cont1
scrTemp_cont1.add_style(style_scrtemp_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_label4 = lv.label(scrTemp)
scrTemp_label4.set_pos(int(100),int(13))
scrTemp_label4.set_size(281,30)
scrTemp_label4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_label4.set_text("Temperature Page")
scrTemp_label4.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrtemp_label4_main_main_default
style_scrtemp_label4_main_main_default = lv.style_t()
style_scrtemp_label4_main_main_default.init()
style_scrtemp_label4_main_main_default.set_radius(0)
style_scrtemp_label4_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_label4_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_label4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_label4_main_main_default.set_bg_opa(0)
style_scrtemp_label4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrtemp_label4_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrtemp_label4_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrtemp_label4_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_label4_main_main_default.set_text_letter_space(2)
style_scrtemp_label4_main_main_default.set_text_line_space(0)
style_scrtemp_label4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_label4_main_main_default.set_pad_left(0)
style_scrtemp_label4_main_main_default.set_pad_right(0)
style_scrtemp_label4_main_main_default.set_pad_top(0)
style_scrtemp_label4_main_main_default.set_pad_bottom(0)

# add style for scrTemp_label4
scrTemp_label4.add_style(style_scrtemp_label4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_labelusb = lv.label(scrTemp)
scrTemp_labelusb.set_pos(int(115),int(160))
scrTemp_labelusb.set_size(74,20)
scrTemp_labelusb.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_labelusb.set_text("Room 1")
scrTemp_labelusb.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrtemp_labelusb_main_main_default
style_scrtemp_labelusb_main_main_default = lv.style_t()
style_scrtemp_labelusb_main_main_default.init()
style_scrtemp_labelusb_main_main_default.set_radius(0)
style_scrtemp_labelusb_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_labelusb_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_labelusb_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_labelusb_main_main_default.set_bg_opa(0)
style_scrtemp_labelusb_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrtemp_labelusb_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrtemp_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrtemp_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_labelusb_main_main_default.set_text_letter_space(2)
style_scrtemp_labelusb_main_main_default.set_text_line_space(0)
style_scrtemp_labelusb_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_labelusb_main_main_default.set_pad_left(0)
style_scrtemp_labelusb_main_main_default.set_pad_right(0)
style_scrtemp_labelusb_main_main_default.set_pad_top(0)
style_scrtemp_labelusb_main_main_default.set_pad_bottom(0)

# add style for scrTemp_labelusb
scrTemp_labelusb.add_style(style_scrtemp_labelusb_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_labelmobile = lv.label(scrTemp)
scrTemp_labelmobile.set_pos(int(288),int(160))
scrTemp_labelmobile.set_size(74,20)
scrTemp_labelmobile.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_labelmobile.set_text("Room 2")
scrTemp_labelmobile.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrtemp_labelmobile_main_main_default
style_scrtemp_labelmobile_main_main_default = lv.style_t()
style_scrtemp_labelmobile_main_main_default.init()
style_scrtemp_labelmobile_main_main_default.set_radius(0)
style_scrtemp_labelmobile_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_labelmobile_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrtemp_labelmobile_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrtemp_labelmobile_main_main_default.set_bg_opa(0)
style_scrtemp_labelmobile_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrtemp_labelmobile_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrtemp_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrtemp_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_labelmobile_main_main_default.set_text_letter_space(2)
style_scrtemp_labelmobile_main_main_default.set_text_line_space(0)
style_scrtemp_labelmobile_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_labelmobile_main_main_default.set_pad_left(0)
style_scrtemp_labelmobile_main_main_default.set_pad_right(0)
style_scrtemp_labelmobile_main_main_default.set_pad_top(0)
style_scrtemp_labelmobile_main_main_default.set_pad_bottom(0)

# add style for scrTemp_labelmobile
scrTemp_labelmobile.add_style(style_scrtemp_labelmobile_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_imgbtn_1 = lv.imgbtn(scrTemp)
scrTemp_imgbtn_1.set_pos(int(34),int(0))
scrTemp_imgbtn_1.set_size(30,26)
scrTemp_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrTemp_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrTemp_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(scrTemp_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrTemp_imgbtn_1_imgReleased_data
})
scrTemp_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, scrTemp_imgbtn_1_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrTemp_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrTemp_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(scrTemp_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrTemp_imgbtn_1_imgPressed_data
})
scrTemp_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, scrTemp_imgbtn_1_imgPressed, None, None)




scrTemp_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
# create style style_scrtemp_imgbtn_1_main_main_default
style_scrtemp_imgbtn_1_main_main_default = lv.style_t()
style_scrtemp_imgbtn_1_main_main_default.init()
style_scrtemp_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrtemp_imgbtn_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrtemp_imgbtn_1_main_main_default.set_img_recolor_opa(0)
style_scrtemp_imgbtn_1_main_main_default.set_img_opa(255)

# add style for scrTemp_imgbtn_1
scrTemp_imgbtn_1.add_style(style_scrtemp_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrtemp_imgbtn_1_main_main_pressed
style_scrtemp_imgbtn_1_main_main_pressed = lv.style_t()
style_scrtemp_imgbtn_1_main_main_pressed.init()
style_scrtemp_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrtemp_imgbtn_1_main_main_pressed.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrtemp_imgbtn_1_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrtemp_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_scrtemp_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for scrTemp_imgbtn_1
scrTemp_imgbtn_1.add_style(style_scrtemp_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrtemp_imgbtn_1_main_main_checked
style_scrtemp_imgbtn_1_main_main_checked = lv.style_t()
style_scrtemp_imgbtn_1_main_main_checked.init()
style_scrtemp_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrtemp_imgbtn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrtemp_imgbtn_1_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrtemp_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_scrtemp_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for scrTemp_imgbtn_1
scrTemp_imgbtn_1.add_style(style_scrtemp_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrTemp_ddlist_1 = lv.dropdown(scrTemp)
scrTemp_ddlist_1.set_pos(int(175),int(29))
scrTemp_ddlist_1.set_size(130,30)
scrTemp_ddlist_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_ddlist_1.set_options("Room 1\nRoom 2")

scrTemp_ddlist_1_list = scrTemp_ddlist_1.get_list()
# create style style_scrtemp_ddlist_1_extra_list_selected_checked
style_scrtemp_ddlist_1_extra_list_selected_checked = lv.style_t()
style_scrtemp_ddlist_1_extra_list_selected_checked.init()
style_scrtemp_ddlist_1_extra_list_selected_checked.set_radius(3)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_bg_color(lv.color_make(0x00,0xa1,0xb5))
style_scrtemp_ddlist_1_extra_list_selected_checked.set_bg_grad_color(lv.color_make(0x00,0xa1,0xb5))
style_scrtemp_ddlist_1_extra_list_selected_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_bg_opa(255)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrtemp_ddlist_1_extra_list_selected_checked.set_border_width(1)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_border_opa(255)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrtemp_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_16)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_pad_left(6)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_pad_right(6)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_pad_top(6)
style_scrtemp_ddlist_1_extra_list_selected_checked.set_pad_bottom(6)

# add style for scrTemp_ddlist_1_list
scrTemp_ddlist_1_list.add_style(style_scrtemp_ddlist_1_extra_list_selected_checked, lv.PART.SELECTED|lv.STATE.CHECKED)

# create style style_scrtemp_ddlist_1_extra_list_main_default
style_scrtemp_ddlist_1_extra_list_main_default = lv.style_t()
style_scrtemp_ddlist_1_extra_list_main_default.init()
style_scrtemp_ddlist_1_extra_list_main_default.set_radius(3)
style_scrtemp_ddlist_1_extra_list_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_ddlist_1_extra_list_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_ddlist_1_extra_list_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_ddlist_1_extra_list_main_default.set_bg_opa(255)
style_scrtemp_ddlist_1_extra_list_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrtemp_ddlist_1_extra_list_main_default.set_border_width(1)
style_scrtemp_ddlist_1_extra_list_main_default.set_border_opa(255)
style_scrtemp_ddlist_1_extra_list_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrtemp_ddlist_1_extra_list_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_ddlist_1_extra_list_main_default.set_pad_left(6)
style_scrtemp_ddlist_1_extra_list_main_default.set_pad_right(6)
style_scrtemp_ddlist_1_extra_list_main_default.set_pad_top(6)
style_scrtemp_ddlist_1_extra_list_main_default.set_pad_bottom(6)
style_scrtemp_ddlist_1_extra_list_main_default.set_max_height(90)

# add style for scrTemp_ddlist_1_list
scrTemp_ddlist_1_list.add_style(style_scrtemp_ddlist_1_extra_list_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrtemp_ddlist_1_extra_list_scrollbar_default
style_scrtemp_ddlist_1_extra_list_scrollbar_default = lv.style_t()
style_scrtemp_ddlist_1_extra_list_scrollbar_default.init()
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_radius(3)
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_bg_color(lv.color_make(0x00,0xff,0x00))
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_bg_opa(255)
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_pad_left(6)
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_pad_right(6)
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_pad_top(6)
style_scrtemp_ddlist_1_extra_list_scrollbar_default.set_pad_bottom(6)

# add style for scrTemp_ddlist_1_list
scrTemp_ddlist_1_list.add_style(style_scrtemp_ddlist_1_extra_list_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)

# create style style_scrtemp_ddlist_1_main_main_default
style_scrtemp_ddlist_1_main_main_default = lv.style_t()
style_scrtemp_ddlist_1_main_main_default.init()
style_scrtemp_ddlist_1_main_main_default.set_radius(3)
style_scrtemp_ddlist_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_ddlist_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_ddlist_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_ddlist_1_main_main_default.set_bg_opa(255)
style_scrtemp_ddlist_1_main_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrtemp_ddlist_1_main_main_default.set_border_width(1)
style_scrtemp_ddlist_1_main_main_default.set_border_opa(255)
style_scrtemp_ddlist_1_main_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrtemp_ddlist_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrtemp_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_ddlist_1_main_main_default.set_pad_left(6)
style_scrtemp_ddlist_1_main_main_default.set_pad_right(6)
style_scrtemp_ddlist_1_main_main_default.set_pad_top(8)

# add style for scrTemp_ddlist_1
scrTemp_ddlist_1.add_style(style_scrtemp_ddlist_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_label_1 = lv.label(scrTemp)
scrTemp_label_1.set_pos(int(311),int(105))
scrTemp_label_1.set_size(88,55)
scrTemp_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_label_1.set_text("35")
scrTemp_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrtemp_label_1_main_main_default
style_scrtemp_label_1_main_main_default = lv.style_t()
style_scrtemp_label_1_main_main_default.init()
style_scrtemp_label_1_main_main_default.set_radius(0)
style_scrtemp_label_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrtemp_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrtemp_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_label_1_main_main_default.set_bg_opa(0)
style_scrtemp_label_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrtemp_label_1_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrtemp_label_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_label_1_main_main_default.set_text_letter_space(2)
style_scrtemp_label_1_main_main_default.set_text_line_space(0)
style_scrtemp_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_label_1_main_main_default.set_pad_left(0)
style_scrtemp_label_1_main_main_default.set_pad_right(0)
style_scrtemp_label_1_main_main_default.set_pad_top(20)
style_scrtemp_label_1_main_main_default.set_pad_bottom(0)

# add style for scrTemp_label_1
scrTemp_label_1.add_style(style_scrtemp_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_label_2 = lv.label(scrTemp)
scrTemp_label_2.set_pos(int(299),int(73))
scrTemp_label_2.set_size(117,34)
scrTemp_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_label_2.set_text("Current temperature:")
scrTemp_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrtemp_label_2_main_main_default
style_scrtemp_label_2_main_main_default = lv.style_t()
style_scrtemp_label_2_main_main_default.init()
style_scrtemp_label_2_main_main_default.set_radius(0)
style_scrtemp_label_2_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrtemp_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrtemp_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_label_2_main_main_default.set_bg_opa(0)
style_scrtemp_label_2_main_main_default.set_text_color(lv.color_make(0x7e,0x07,0x07))
try:
    style_scrtemp_label_2_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrtemp_label_2_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrtemp_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrtemp_label_2_main_main_default.set_text_letter_space(2)
style_scrtemp_label_2_main_main_default.set_text_line_space(0)
style_scrtemp_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrtemp_label_2_main_main_default.set_pad_left(0)
style_scrtemp_label_2_main_main_default.set_pad_right(0)
style_scrtemp_label_2_main_main_default.set_pad_top(0)
style_scrtemp_label_2_main_main_default.set_pad_bottom(0)

# add style for scrTemp_label_2
scrTemp_label_2.add_style(style_scrtemp_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrTemp_chart_1 = lv.chart(scrTemp)
scrTemp_chart_1.set_pos(int(64),int(73))
scrTemp_chart_1.set_size(190,99)
scrTemp_chart_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrTemp_chart_1.set_type(lv.chart.TYPE.LINE)
scrTemp_chart_1.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 50)
scrTemp_chart_1.set_div_line_count(5, 5)
scrTemp_chart_1.set_point_count(5)
chart_series_0 = lv.chart.add_series(scrTemp_chart_1, lv.color_make(0x00,0x00,0x00), lv.chart.AXIS.PRIMARY_Y);
scrTemp_chart_1.set_next_value(chart_series_0, 1)
scrTemp_chart_1.set_next_value(chart_series_0, 20)
scrTemp_chart_1.set_next_value(chart_series_0, 30)
scrTemp_chart_1.set_next_value(chart_series_0, 40)
scrTemp_chart_1.set_next_value(chart_series_0, 5)
# create style style_scrtemp_chart_1_main_main_default
style_scrtemp_chart_1_main_main_default = lv.style_t()
style_scrtemp_chart_1_main_main_default.init()
style_scrtemp_chart_1_main_main_default.set_radius(0)
style_scrtemp_chart_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_chart_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrtemp_chart_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrtemp_chart_1_main_main_default.set_bg_opa(255)
style_scrtemp_chart_1_main_main_default.set_border_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrtemp_chart_1_main_main_default.set_border_width(1)
style_scrtemp_chart_1_main_main_default.set_border_opa(255)
style_scrtemp_chart_1_main_main_default.set_line_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrtemp_chart_1_main_main_default.set_line_width(2)
style_scrtemp_chart_1_main_main_default.set_line_opa(255)

# add style for scrTemp_chart_1
scrTemp_chart_1.add_style(style_scrtemp_chart_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid = lv.obj()
scrHumid.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrhumid_main_main_default
style_scrhumid_main_main_default = lv.style_t()
style_scrhumid_main_main_default.init()
style_scrhumid_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_main_main_default.set_bg_opa(0)

# add style for scrHumid
scrHumid.add_style(style_scrhumid_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_cont0 = lv.obj(scrHumid)
scrHumid_cont0.set_pos(int(0),int(0))
scrHumid_cont0.set_size(480,33)
scrHumid_cont0.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrhumid_cont0_main_main_default
style_scrhumid_cont0_main_main_default = lv.style_t()
style_scrhumid_cont0_main_main_default.init()
style_scrhumid_cont0_main_main_default.set_radius(0)
style_scrhumid_cont0_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_scrhumid_cont0_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_scrhumid_cont0_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_cont0_main_main_default.set_bg_opa(255)
style_scrhumid_cont0_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrhumid_cont0_main_main_default.set_border_width(0)
style_scrhumid_cont0_main_main_default.set_border_opa(255)
style_scrhumid_cont0_main_main_default.set_pad_left(0)
style_scrhumid_cont0_main_main_default.set_pad_right(0)
style_scrhumid_cont0_main_main_default.set_pad_top(0)
style_scrhumid_cont0_main_main_default.set_pad_bottom(0)

# add style for scrHumid_cont0
scrHumid_cont0.add_style(style_scrhumid_cont0_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_con2 = lv.obj(scrHumid)
scrHumid_con2.set_pos(int(0),int(15))
scrHumid_con2.set_size(480,252)
scrHumid_con2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrhumid_con2_main_main_default
style_scrhumid_con2_main_main_default = lv.style_t()
style_scrhumid_con2_main_main_default.init()
style_scrhumid_con2_main_main_default.set_radius(0)
style_scrhumid_con2_main_main_default.set_bg_color(lv.color_make(0xde,0xde,0xde))
style_scrhumid_con2_main_main_default.set_bg_grad_color(lv.color_make(0xde,0xde,0xde))
style_scrhumid_con2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_con2_main_main_default.set_bg_opa(255)
style_scrhumid_con2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrhumid_con2_main_main_default.set_border_width(0)
style_scrhumid_con2_main_main_default.set_border_opa(255)
style_scrhumid_con2_main_main_default.set_pad_left(0)
style_scrhumid_con2_main_main_default.set_pad_right(0)
style_scrhumid_con2_main_main_default.set_pad_top(0)
style_scrhumid_con2_main_main_default.set_pad_bottom(0)

# add style for scrHumid_con2
scrHumid_con2.add_style(style_scrhumid_con2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_cont1 = lv.obj(scrHumid)
scrHumid_cont1.set_pos(int(40),int(60))
scrHumid_cont1.set_size(400,140)
scrHumid_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrhumid_cont1_main_main_default
style_scrhumid_cont1_main_main_default = lv.style_t()
style_scrhumid_cont1_main_main_default.init()
style_scrhumid_cont1_main_main_default.set_radius(0)
style_scrhumid_cont1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_cont1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_cont1_main_main_default.set_bg_opa(255)
style_scrhumid_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrhumid_cont1_main_main_default.set_border_width(0)
style_scrhumid_cont1_main_main_default.set_border_opa(255)
style_scrhumid_cont1_main_main_default.set_pad_left(0)
style_scrhumid_cont1_main_main_default.set_pad_right(0)
style_scrhumid_cont1_main_main_default.set_pad_top(0)
style_scrhumid_cont1_main_main_default.set_pad_bottom(0)

# add style for scrHumid_cont1
scrHumid_cont1.add_style(style_scrhumid_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_label4 = lv.label(scrHumid)
scrHumid_label4.set_pos(int(100),int(13))
scrHumid_label4.set_size(281,30)
scrHumid_label4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_label4.set_text("Humidity Page")
scrHumid_label4.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrhumid_label4_main_main_default
style_scrhumid_label4_main_main_default = lv.style_t()
style_scrhumid_label4_main_main_default.init()
style_scrhumid_label4_main_main_default.set_radius(0)
style_scrhumid_label4_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_label4_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_label4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_label4_main_main_default.set_bg_opa(0)
style_scrhumid_label4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrhumid_label4_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrhumid_label4_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrhumid_label4_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_label4_main_main_default.set_text_letter_space(2)
style_scrhumid_label4_main_main_default.set_text_line_space(0)
style_scrhumid_label4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_label4_main_main_default.set_pad_left(0)
style_scrhumid_label4_main_main_default.set_pad_right(0)
style_scrhumid_label4_main_main_default.set_pad_top(0)
style_scrhumid_label4_main_main_default.set_pad_bottom(0)

# add style for scrHumid_label4
scrHumid_label4.add_style(style_scrhumid_label4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_labelusb = lv.label(scrHumid)
scrHumid_labelusb.set_pos(int(115),int(160))
scrHumid_labelusb.set_size(74,20)
scrHumid_labelusb.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_labelusb.set_text("Room 1")
scrHumid_labelusb.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrhumid_labelusb_main_main_default
style_scrhumid_labelusb_main_main_default = lv.style_t()
style_scrhumid_labelusb_main_main_default.init()
style_scrhumid_labelusb_main_main_default.set_radius(0)
style_scrhumid_labelusb_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_labelusb_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_labelusb_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_labelusb_main_main_default.set_bg_opa(0)
style_scrhumid_labelusb_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrhumid_labelusb_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrhumid_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrhumid_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_labelusb_main_main_default.set_text_letter_space(2)
style_scrhumid_labelusb_main_main_default.set_text_line_space(0)
style_scrhumid_labelusb_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_labelusb_main_main_default.set_pad_left(0)
style_scrhumid_labelusb_main_main_default.set_pad_right(0)
style_scrhumid_labelusb_main_main_default.set_pad_top(0)
style_scrhumid_labelusb_main_main_default.set_pad_bottom(0)

# add style for scrHumid_labelusb
scrHumid_labelusb.add_style(style_scrhumid_labelusb_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_labelmobile = lv.label(scrHumid)
scrHumid_labelmobile.set_pos(int(288),int(160))
scrHumid_labelmobile.set_size(74,20)
scrHumid_labelmobile.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_labelmobile.set_text("Room 2")
scrHumid_labelmobile.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrhumid_labelmobile_main_main_default
style_scrhumid_labelmobile_main_main_default = lv.style_t()
style_scrhumid_labelmobile_main_main_default.init()
style_scrhumid_labelmobile_main_main_default.set_radius(0)
style_scrhumid_labelmobile_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_labelmobile_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrhumid_labelmobile_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrhumid_labelmobile_main_main_default.set_bg_opa(0)
style_scrhumid_labelmobile_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrhumid_labelmobile_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrhumid_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrhumid_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_labelmobile_main_main_default.set_text_letter_space(2)
style_scrhumid_labelmobile_main_main_default.set_text_line_space(0)
style_scrhumid_labelmobile_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_labelmobile_main_main_default.set_pad_left(0)
style_scrhumid_labelmobile_main_main_default.set_pad_right(0)
style_scrhumid_labelmobile_main_main_default.set_pad_top(0)
style_scrhumid_labelmobile_main_main_default.set_pad_bottom(0)

# add style for scrHumid_labelmobile
scrHumid_labelmobile.add_style(style_scrhumid_labelmobile_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_imgbtn_1 = lv.imgbtn(scrHumid)
scrHumid_imgbtn_1.set_pos(int(34),int(0))
scrHumid_imgbtn_1.set_size(30,26)
scrHumid_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrHumid_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrHumid_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(scrHumid_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrHumid_imgbtn_1_imgReleased_data
})
scrHumid_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, scrHumid_imgbtn_1_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrHumid_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrHumid_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(scrHumid_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrHumid_imgbtn_1_imgPressed_data
})
scrHumid_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, scrHumid_imgbtn_1_imgPressed, None, None)




scrHumid_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
# create style style_scrhumid_imgbtn_1_main_main_default
style_scrhumid_imgbtn_1_main_main_default = lv.style_t()
style_scrhumid_imgbtn_1_main_main_default.init()
style_scrhumid_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrhumid_imgbtn_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrhumid_imgbtn_1_main_main_default.set_img_recolor_opa(0)
style_scrhumid_imgbtn_1_main_main_default.set_img_opa(255)

# add style for scrHumid_imgbtn_1
scrHumid_imgbtn_1.add_style(style_scrhumid_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrhumid_imgbtn_1_main_main_pressed
style_scrhumid_imgbtn_1_main_main_pressed = lv.style_t()
style_scrhumid_imgbtn_1_main_main_pressed.init()
style_scrhumid_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrhumid_imgbtn_1_main_main_pressed.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrhumid_imgbtn_1_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrhumid_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_scrhumid_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for scrHumid_imgbtn_1
scrHumid_imgbtn_1.add_style(style_scrhumid_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrhumid_imgbtn_1_main_main_checked
style_scrhumid_imgbtn_1_main_main_checked = lv.style_t()
style_scrhumid_imgbtn_1_main_main_checked.init()
style_scrhumid_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrhumid_imgbtn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrhumid_imgbtn_1_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrhumid_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_scrhumid_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for scrHumid_imgbtn_1
scrHumid_imgbtn_1.add_style(style_scrhumid_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrHumid_ddlist_1 = lv.dropdown(scrHumid)
scrHumid_ddlist_1.set_pos(int(175),int(29))
scrHumid_ddlist_1.set_size(130,30)
scrHumid_ddlist_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_ddlist_1.set_options("Room 1\nRoom 2")

scrHumid_ddlist_1_list = scrHumid_ddlist_1.get_list()
# create style style_scrhumid_ddlist_1_extra_list_selected_checked
style_scrhumid_ddlist_1_extra_list_selected_checked = lv.style_t()
style_scrhumid_ddlist_1_extra_list_selected_checked.init()
style_scrhumid_ddlist_1_extra_list_selected_checked.set_radius(3)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_bg_color(lv.color_make(0x00,0xa1,0xb5))
style_scrhumid_ddlist_1_extra_list_selected_checked.set_bg_grad_color(lv.color_make(0x00,0xa1,0xb5))
style_scrhumid_ddlist_1_extra_list_selected_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_bg_opa(255)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrhumid_ddlist_1_extra_list_selected_checked.set_border_width(1)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_border_opa(255)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrhumid_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_16)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_pad_left(6)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_pad_right(6)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_pad_top(6)
style_scrhumid_ddlist_1_extra_list_selected_checked.set_pad_bottom(6)

# add style for scrHumid_ddlist_1_list
scrHumid_ddlist_1_list.add_style(style_scrhumid_ddlist_1_extra_list_selected_checked, lv.PART.SELECTED|lv.STATE.CHECKED)

# create style style_scrhumid_ddlist_1_extra_list_main_default
style_scrhumid_ddlist_1_extra_list_main_default = lv.style_t()
style_scrhumid_ddlist_1_extra_list_main_default.init()
style_scrhumid_ddlist_1_extra_list_main_default.set_radius(3)
style_scrhumid_ddlist_1_extra_list_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_ddlist_1_extra_list_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_ddlist_1_extra_list_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_ddlist_1_extra_list_main_default.set_bg_opa(255)
style_scrhumid_ddlist_1_extra_list_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrhumid_ddlist_1_extra_list_main_default.set_border_width(1)
style_scrhumid_ddlist_1_extra_list_main_default.set_border_opa(255)
style_scrhumid_ddlist_1_extra_list_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrhumid_ddlist_1_extra_list_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_ddlist_1_extra_list_main_default.set_pad_left(6)
style_scrhumid_ddlist_1_extra_list_main_default.set_pad_right(6)
style_scrhumid_ddlist_1_extra_list_main_default.set_pad_top(6)
style_scrhumid_ddlist_1_extra_list_main_default.set_pad_bottom(6)
style_scrhumid_ddlist_1_extra_list_main_default.set_max_height(90)

# add style for scrHumid_ddlist_1_list
scrHumid_ddlist_1_list.add_style(style_scrhumid_ddlist_1_extra_list_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrhumid_ddlist_1_extra_list_scrollbar_default
style_scrhumid_ddlist_1_extra_list_scrollbar_default = lv.style_t()
style_scrhumid_ddlist_1_extra_list_scrollbar_default.init()
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_radius(3)
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_bg_color(lv.color_make(0x00,0xff,0x00))
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_bg_opa(255)
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_pad_left(6)
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_pad_right(6)
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_pad_top(6)
style_scrhumid_ddlist_1_extra_list_scrollbar_default.set_pad_bottom(6)

# add style for scrHumid_ddlist_1_list
scrHumid_ddlist_1_list.add_style(style_scrhumid_ddlist_1_extra_list_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)

# create style style_scrhumid_ddlist_1_main_main_default
style_scrhumid_ddlist_1_main_main_default = lv.style_t()
style_scrhumid_ddlist_1_main_main_default.init()
style_scrhumid_ddlist_1_main_main_default.set_radius(3)
style_scrhumid_ddlist_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_ddlist_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_ddlist_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_ddlist_1_main_main_default.set_bg_opa(255)
style_scrhumid_ddlist_1_main_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrhumid_ddlist_1_main_main_default.set_border_width(1)
style_scrhumid_ddlist_1_main_main_default.set_border_opa(255)
style_scrhumid_ddlist_1_main_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrhumid_ddlist_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrhumid_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_ddlist_1_main_main_default.set_pad_left(6)
style_scrhumid_ddlist_1_main_main_default.set_pad_right(6)
style_scrhumid_ddlist_1_main_main_default.set_pad_top(8)

# add style for scrHumid_ddlist_1
scrHumid_ddlist_1.add_style(style_scrhumid_ddlist_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_label_1 = lv.label(scrHumid)
scrHumid_label_1.set_pos(int(311),int(105))
scrHumid_label_1.set_size(88,55)
scrHumid_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_label_1.set_text("100%")
scrHumid_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrhumid_label_1_main_main_default
style_scrhumid_label_1_main_main_default = lv.style_t()
style_scrhumid_label_1_main_main_default.init()
style_scrhumid_label_1_main_main_default.set_radius(0)
style_scrhumid_label_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrhumid_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrhumid_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_label_1_main_main_default.set_bg_opa(0)
style_scrhumid_label_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrhumid_label_1_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrhumid_label_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_label_1_main_main_default.set_text_letter_space(2)
style_scrhumid_label_1_main_main_default.set_text_line_space(0)
style_scrhumid_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_label_1_main_main_default.set_pad_left(0)
style_scrhumid_label_1_main_main_default.set_pad_right(0)
style_scrhumid_label_1_main_main_default.set_pad_top(20)
style_scrhumid_label_1_main_main_default.set_pad_bottom(0)

# add style for scrHumid_label_1
scrHumid_label_1.add_style(style_scrhumid_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_label_2 = lv.label(scrHumid)
scrHumid_label_2.set_pos(int(299),int(73))
scrHumid_label_2.set_size(117,34)
scrHumid_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_label_2.set_text("Current humidity level:")
scrHumid_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrhumid_label_2_main_main_default
style_scrhumid_label_2_main_main_default = lv.style_t()
style_scrhumid_label_2_main_main_default.init()
style_scrhumid_label_2_main_main_default.set_radius(0)
style_scrhumid_label_2_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrhumid_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrhumid_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_label_2_main_main_default.set_bg_opa(0)
style_scrhumid_label_2_main_main_default.set_text_color(lv.color_make(0x7e,0x07,0x07))
try:
    style_scrhumid_label_2_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrhumid_label_2_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrhumid_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrhumid_label_2_main_main_default.set_text_letter_space(2)
style_scrhumid_label_2_main_main_default.set_text_line_space(0)
style_scrhumid_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrhumid_label_2_main_main_default.set_pad_left(0)
style_scrhumid_label_2_main_main_default.set_pad_right(0)
style_scrhumid_label_2_main_main_default.set_pad_top(0)
style_scrhumid_label_2_main_main_default.set_pad_bottom(0)

# add style for scrHumid_label_2
scrHumid_label_2.add_style(style_scrhumid_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrHumid_chart_1 = lv.chart(scrHumid)
scrHumid_chart_1.set_pos(int(64),int(73))
scrHumid_chart_1.set_size(190,99)
scrHumid_chart_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrHumid_chart_1.set_type(lv.chart.TYPE.LINE)
scrHumid_chart_1.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 50)
scrHumid_chart_1.set_div_line_count(5, 5)
scrHumid_chart_1.set_point_count(5)
chart_series_0 = lv.chart.add_series(scrHumid_chart_1, lv.color_make(0x00,0x00,0x00), lv.chart.AXIS.PRIMARY_Y);
scrHumid_chart_1.set_next_value(chart_series_0, 1)
scrHumid_chart_1.set_next_value(chart_series_0, 20)
scrHumid_chart_1.set_next_value(chart_series_0, 30)
scrHumid_chart_1.set_next_value(chart_series_0, 40)
scrHumid_chart_1.set_next_value(chart_series_0, 5)
# create style style_scrhumid_chart_1_main_main_default
style_scrhumid_chart_1_main_main_default = lv.style_t()
style_scrhumid_chart_1_main_main_default.init()
style_scrhumid_chart_1_main_main_default.set_radius(0)
style_scrhumid_chart_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_chart_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrhumid_chart_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrhumid_chart_1_main_main_default.set_bg_opa(255)
style_scrhumid_chart_1_main_main_default.set_border_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrhumid_chart_1_main_main_default.set_border_width(1)
style_scrhumid_chart_1_main_main_default.set_border_opa(255)
style_scrhumid_chart_1_main_main_default.set_line_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrhumid_chart_1_main_main_default.set_line_width(2)
style_scrhumid_chart_1_main_main_default.set_line_opa(255)

# add style for scrHumid_chart_1
scrHumid_chart_1.add_style(style_scrhumid_chart_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect = lv.obj()
scrnFanLightselect.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnfanlightselect_main_main_default
style_scrnfanlightselect_main_main_default = lv.style_t()
style_scrnfanlightselect_main_main_default.init()
style_scrnfanlightselect_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_main_main_default.set_bg_opa(0)

# add style for scrnFanLightselect
scrnFanLightselect.add_style(style_scrnfanlightselect_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_cont1 = lv.obj(scrnFanLightselect)
scrnFanLightselect_cont1.set_pos(int(0),int(0))
scrnFanLightselect_cont1.set_size(480,95)
scrnFanLightselect_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnfanlightselect_cont1_main_main_default
style_scrnfanlightselect_cont1_main_main_default = lv.style_t()
style_scrnfanlightselect_cont1_main_main_default.init()
style_scrnfanlightselect_cont1_main_main_default.set_radius(0)
style_scrnfanlightselect_cont1_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_scrnfanlightselect_cont1_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_scrnfanlightselect_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnfanlightselect_cont1_main_main_default.set_bg_opa(255)
style_scrnfanlightselect_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_cont1_main_main_default.set_border_width(0)
style_scrnfanlightselect_cont1_main_main_default.set_border_opa(255)
style_scrnfanlightselect_cont1_main_main_default.set_pad_left(0)
style_scrnfanlightselect_cont1_main_main_default.set_pad_right(0)
style_scrnfanlightselect_cont1_main_main_default.set_pad_top(0)
style_scrnfanlightselect_cont1_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_cont1
scrnFanLightselect_cont1.add_style(style_scrnfanlightselect_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_whitebg = lv.obj(scrnFanLightselect)
scrnFanLightselect_whitebg.set_pos(int(0),int(96))
scrnFanLightselect_whitebg.set_size(480,177)
scrnFanLightselect_whitebg.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnfanlightselect_whitebg_main_main_default
style_scrnfanlightselect_whitebg_main_main_default = lv.style_t()
style_scrnfanlightselect_whitebg_main_main_default.init()
style_scrnfanlightselect_whitebg_main_main_default.set_radius(0)
style_scrnfanlightselect_whitebg_main_main_default.set_bg_color(lv.color_make(0xd6,0xdc,0xd6))
style_scrnfanlightselect_whitebg_main_main_default.set_bg_grad_color(lv.color_make(0xd9,0xd9,0xd9))
style_scrnfanlightselect_whitebg_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnfanlightselect_whitebg_main_main_default.set_bg_opa(255)
style_scrnfanlightselect_whitebg_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_whitebg_main_main_default.set_border_width(0)
style_scrnfanlightselect_whitebg_main_main_default.set_border_opa(255)
style_scrnfanlightselect_whitebg_main_main_default.set_pad_left(0)
style_scrnfanlightselect_whitebg_main_main_default.set_pad_right(0)
style_scrnfanlightselect_whitebg_main_main_default.set_pad_top(0)
style_scrnfanlightselect_whitebg_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_whitebg
scrnFanLightselect_whitebg.add_style(style_scrnfanlightselect_whitebg_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_cont2 = lv.obj(scrnFanLightselect)
scrnFanLightselect_cont2.set_pos(int(40),int(80))
scrnFanLightselect_cont2.set_size(380,120)
scrnFanLightselect_cont2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnfanlightselect_cont2_main_main_default
style_scrnfanlightselect_cont2_main_main_default = lv.style_t()
style_scrnfanlightselect_cont2_main_main_default.init()
style_scrnfanlightselect_cont2_main_main_default.set_radius(0)
style_scrnfanlightselect_cont2_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_cont2_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_cont2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnfanlightselect_cont2_main_main_default.set_bg_opa(255)
style_scrnfanlightselect_cont2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_cont2_main_main_default.set_border_width(0)
style_scrnfanlightselect_cont2_main_main_default.set_border_opa(255)
style_scrnfanlightselect_cont2_main_main_default.set_pad_left(0)
style_scrnfanlightselect_cont2_main_main_default.set_pad_right(0)
style_scrnfanlightselect_cont2_main_main_default.set_pad_top(0)
style_scrnfanlightselect_cont2_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_cont2
scrnFanLightselect_cont2.add_style(style_scrnfanlightselect_cont2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_imgbtn_humid = lv.imgbtn(scrnFanLightselect)
scrnFanLightselect_imgbtn_humid.set_pos(int(139),int(87))
scrnFanLightselect_imgbtn_humid.set_size(96,100)
scrnFanLightselect_imgbtn_humid.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        scrnFanLightselect_imgbtn_humid_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

scrnFanLightselect_imgbtn_humid_imgReleased = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_humid_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_humid_imgReleased_data
})
scrnFanLightselect_imgbtn_humid.set_src(lv.imgbtn.STATE.RELEASED, scrnFanLightselect_imgbtn_humid_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        scrnFanLightselect_imgbtn_humid_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

scrnFanLightselect_imgbtn_humid_imgPressed = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_humid_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_humid_imgPressed_data
})
scrnFanLightselect_imgbtn_humid.set_src(lv.imgbtn.STATE.PRESSED, scrnFanLightselect_imgbtn_humid_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        scrnFanLightselect_imgbtn_humid_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

scrnFanLightselect_imgbtn_humid_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_humid_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_humid_imgCheckedReleased_data
})
scrnFanLightselect_imgbtn_humid.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, scrnFanLightselect_imgbtn_humid_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png','rb') as f:
        scrnFanLightselect_imgbtn_humid_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp872679681.png')
    sys.exit()

scrnFanLightselect_imgbtn_humid_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_humid_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_humid_imgCheckedPressed_data
})
scrnFanLightselect_imgbtn_humid.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, scrnFanLightselect_imgbtn_humid_imgCheckedPressed, None, None)

# create style style_scrnfanlightselect_imgbtn_humid_main_main_default
style_scrnfanlightselect_imgbtn_humid_main_main_default = lv.style_t()
style_scrnfanlightselect_imgbtn_humid_main_main_default.init()
style_scrnfanlightselect_imgbtn_humid_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrnfanlightselect_imgbtn_humid_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_humid_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_humid_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_humid_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_humid_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_imgbtn_humid_main_main_default.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_humid_main_main_default.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_humid
scrnFanLightselect_imgbtn_humid.add_style(style_scrnfanlightselect_imgbtn_humid_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrnfanlightselect_imgbtn_humid_main_main_pressed
style_scrnfanlightselect_imgbtn_humid_main_main_pressed = lv.style_t()
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.init()
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_humid_main_main_pressed.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_humid
scrnFanLightselect_imgbtn_humid.add_style(style_scrnfanlightselect_imgbtn_humid_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrnfanlightselect_imgbtn_humid_main_main_checked
style_scrnfanlightselect_imgbtn_humid_main_main_checked = lv.style_t()
style_scrnfanlightselect_imgbtn_humid_main_main_checked.init()
style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_humid_main_main_checked.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_humid
scrnFanLightselect_imgbtn_humid.add_style(style_scrnfanlightselect_imgbtn_humid_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrnFanLightselect_imgbtn_fanlght = lv.imgbtn(scrnFanLightselect)
scrnFanLightselect_imgbtn_fanlght.set_pos(int(230),int(86))
scrnFanLightselect_imgbtn_fanlght.set_size(96,100)
scrnFanLightselect_imgbtn_fanlght.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        scrnFanLightselect_imgbtn_fanlght_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

scrnFanLightselect_imgbtn_fanlght_imgReleased = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_fanlght_imgReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_fanlght_imgReleased_data
})
scrnFanLightselect_imgbtn_fanlght.set_src(lv.imgbtn.STATE.RELEASED, scrnFanLightselect_imgbtn_fanlght_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        scrnFanLightselect_imgbtn_fanlght_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

scrnFanLightselect_imgbtn_fanlght_imgPressed = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_fanlght_imgPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_fanlght_imgPressed_data
})
scrnFanLightselect_imgbtn_fanlght.set_src(lv.imgbtn.STATE.PRESSED, scrnFanLightselect_imgbtn_fanlght_imgPressed, None, None)


try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        scrnFanLightselect_imgbtn_fanlght_imgCheckedReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

scrnFanLightselect_imgbtn_fanlght_imgCheckedReleased = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_fanlght_imgCheckedReleased_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_fanlght_imgCheckedReleased_data
})
scrnFanLightselect_imgbtn_fanlght.set_src(lv.imgbtn.STATE.CHECKED_RELEASED, scrnFanLightselect_imgbtn_fanlght_imgCheckedReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png','rb') as f:
        scrnFanLightselect_imgbtn_fanlght_imgCheckedPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp903699488.png')
    sys.exit()

scrnFanLightselect_imgbtn_fanlght_imgCheckedPressed = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgbtn_fanlght_imgCheckedPressed_data),
  'header': {'always_zero': 0, 'w': 96, 'h': 100, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgbtn_fanlght_imgCheckedPressed_data
})
scrnFanLightselect_imgbtn_fanlght.set_src(lv.imgbtn.STATE.CHECKED_PRESSED, scrnFanLightselect_imgbtn_fanlght_imgCheckedPressed, None, None)

# create style style_scrnfanlightselect_imgbtn_fanlght_main_main_default
style_scrnfanlightselect_imgbtn_fanlght_main_main_default = lv.style_t()
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.init()
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_fanlght_main_main_default.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_fanlght
scrnFanLightselect_imgbtn_fanlght.add_style(style_scrnfanlightselect_imgbtn_fanlght_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed = lv.style_t()
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.init()
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_fanlght
scrnFanLightselect_imgbtn_fanlght.add_style(style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrnfanlightselect_imgbtn_fanlght_main_main_checked
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked = lv.style_t()
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.init()
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_img_recolor_opa(0)
style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.set_img_opa(255)

# add style for scrnFanLightselect_imgbtn_fanlght
scrnFanLightselect_imgbtn_fanlght.add_style(style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrnFanLightselect_img_fan = lv.img(scrnFanLightselect)
scrnFanLightselect_img_fan.set_pos(int(172),int(119))
scrnFanLightselect_img_fan.set_size(31,29)
scrnFanLightselect_img_fan.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_img_fan.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1980422287.png','rb') as f:
        scrnFanLightselect_img_fan_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1980422287.png')
    sys.exit()

scrnFanLightselect_img_fan_img = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_img_fan_img_data),
  'header': {'always_zero': 0, 'w': 31, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_img_fan_img_data
})

scrnFanLightselect_img_fan.set_src(scrnFanLightselect_img_fan_img)
scrnFanLightselect_img_fan.set_pivot(0,0)
scrnFanLightselect_img_fan.set_angle(0)
# create style style_scrnfanlightselect_img_fan_main_main_default
style_scrnfanlightselect_img_fan_main_main_default = lv.style_t()
style_scrnfanlightselect_img_fan_main_main_default.init()
style_scrnfanlightselect_img_fan_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_img_fan_main_main_default.set_img_recolor_opa(0)
style_scrnfanlightselect_img_fan_main_main_default.set_img_opa(255)

# add style for scrnFanLightselect_img_fan
scrnFanLightselect_img_fan.add_style(style_scrnfanlightselect_img_fan_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_labelhumid = lv.label(scrnFanLightselect)
scrnFanLightselect_labelhumid.set_pos(int(154),int(156))
scrnFanLightselect_labelhumid.set_size(67,20)
scrnFanLightselect_labelhumid.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_labelhumid.set_text("Fan")
scrnFanLightselect_labelhumid.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnfanlightselect_labelhumid_main_main_default
style_scrnfanlightselect_labelhumid_main_main_default = lv.style_t()
style_scrnfanlightselect_labelhumid_main_main_default.init()
style_scrnfanlightselect_labelhumid_main_main_default.set_radius(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnfanlightselect_labelhumid_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnfanlightselect_labelhumid_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnfanlightselect_labelhumid_main_main_default.set_bg_opa(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnfanlightselect_labelhumid_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnfanlightselect_labelhumid_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnfanlightselect_labelhumid_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_labelhumid_main_main_default.set_text_letter_space(1)
style_scrnfanlightselect_labelhumid_main_main_default.set_text_line_space(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_labelhumid_main_main_default.set_pad_left(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_pad_right(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_pad_top(0)
style_scrnfanlightselect_labelhumid_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_labelhumid
scrnFanLightselect_labelhumid.add_style(style_scrnfanlightselect_labelhumid_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_labelfanlight = lv.label(scrnFanLightselect)
scrnFanLightselect_labelfanlight.set_pos(int(242),int(156))
scrnFanLightselect_labelfanlight.set_size(75,36)
scrnFanLightselect_labelfanlight.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_labelfanlight.set_text("Light")
scrnFanLightselect_labelfanlight.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnfanlightselect_labelfanlight_main_main_default
style_scrnfanlightselect_labelfanlight_main_main_default = lv.style_t()
style_scrnfanlightselect_labelfanlight_main_main_default.init()
style_scrnfanlightselect_labelfanlight_main_main_default.set_radius(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnfanlightselect_labelfanlight_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnfanlightselect_labelfanlight_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnfanlightselect_labelfanlight_main_main_default.set_bg_opa(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnfanlightselect_labelfanlight_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnfanlightselect_labelfanlight_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnfanlightselect_labelfanlight_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_labelfanlight_main_main_default.set_text_letter_space(1)
style_scrnfanlightselect_labelfanlight_main_main_default.set_text_line_space(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_labelfanlight_main_main_default.set_pad_left(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_pad_right(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_pad_top(0)
style_scrnfanlightselect_labelfanlight_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_labelfanlight
scrnFanLightselect_labelfanlight.add_style(style_scrnfanlightselect_labelfanlight_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_imgcopy = lv.img(scrnFanLightselect)
scrnFanLightselect_imgcopy.set_pos(int(90),int(108))
scrnFanLightselect_imgcopy.set_size(29,29)
scrnFanLightselect_imgcopy.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_imgcopy.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1651069706.png','rb') as f:
        scrnFanLightselect_imgcopy_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp1651069706.png')
    sys.exit()

scrnFanLightselect_imgcopy_img = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imgcopy_img_data),
  'header': {'always_zero': 0, 'w': 29, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imgcopy_img_data
})

scrnFanLightselect_imgcopy.set_src(scrnFanLightselect_imgcopy_img)
scrnFanLightselect_imgcopy.set_pivot(0,0)
scrnFanLightselect_imgcopy.set_angle(0)
# create style style_scrnfanlightselect_imgcopy_main_main_default
style_scrnfanlightselect_imgcopy_main_main_default = lv.style_t()
style_scrnfanlightselect_imgcopy_main_main_default.init()
style_scrnfanlightselect_imgcopy_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_imgcopy_main_main_default.set_img_recolor_opa(0)
style_scrnfanlightselect_imgcopy_main_main_default.set_img_opa(255)

# add style for scrnFanLightselect_imgcopy
scrnFanLightselect_imgcopy.add_style(style_scrnfanlightselect_imgcopy_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_imglight = lv.img(scrnFanLightselect)
scrnFanLightselect_imglight.set_pos(int(264),int(119))
scrnFanLightselect_imglight.set_size(31,29)
scrnFanLightselect_imglight.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_imglight.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1521194444.png','rb') as f:
        scrnFanLightselect_imglight_img_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp-1521194444.png')
    sys.exit()

scrnFanLightselect_imglight_img = lv.img_dsc_t({
  'data_size': len(scrnFanLightselect_imglight_img_data),
  'header': {'always_zero': 0, 'w': 31, 'h': 29, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnFanLightselect_imglight_img_data
})

scrnFanLightselect_imglight.set_src(scrnFanLightselect_imglight_img)
scrnFanLightselect_imglight.set_pivot(0,0)
scrnFanLightselect_imglight.set_angle(0)
# create style style_scrnfanlightselect_imglight_main_main_default
style_scrnfanlightselect_imglight_main_main_default = lv.style_t()
style_scrnfanlightselect_imglight_main_main_default.init()
style_scrnfanlightselect_imglight_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnfanlightselect_imglight_main_main_default.set_img_recolor_opa(0)
style_scrnfanlightselect_imglight_main_main_default.set_img_opa(255)

# add style for scrnFanLightselect_imglight
scrnFanLightselect_imglight.add_style(style_scrnfanlightselect_imglight_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnFanLightselect_label_3 = lv.label(scrnFanLightselect)
scrnFanLightselect_label_3.set_pos(int(12),int(24))
scrnFanLightselect_label_3.set_size(456,33)
scrnFanLightselect_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnFanLightselect_label_3.set_text("Which you would like to monitor?")
scrnFanLightselect_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnfanlightselect_label_3_main_main_default
style_scrnfanlightselect_label_3_main_main_default = lv.style_t()
style_scrnfanlightselect_label_3_main_main_default.init()
style_scrnfanlightselect_label_3_main_main_default.set_radius(0)
style_scrnfanlightselect_label_3_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrnfanlightselect_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrnfanlightselect_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnfanlightselect_label_3_main_main_default.set_bg_opa(0)
style_scrnfanlightselect_label_3_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnfanlightselect_label_3_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnfanlightselect_label_3_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnfanlightselect_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnfanlightselect_label_3_main_main_default.set_text_letter_space(2)
style_scrnfanlightselect_label_3_main_main_default.set_text_line_space(0)
style_scrnfanlightselect_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnfanlightselect_label_3_main_main_default.set_pad_left(0)
style_scrnfanlightselect_label_3_main_main_default.set_pad_right(0)
style_scrnfanlightselect_label_3_main_main_default.set_pad_top(0)
style_scrnfanlightselect_label_3_main_main_default.set_pad_bottom(0)

# add style for scrnFanLightselect_label_3
scrnFanLightselect_label_3.add_style(style_scrnfanlightselect_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan = lv.obj()
scrFan.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrfan_main_main_default
style_scrfan_main_main_default = lv.style_t()
style_scrfan_main_main_default.init()
style_scrfan_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_main_main_default.set_bg_opa(0)

# add style for scrFan
scrFan.add_style(style_scrfan_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_cont0 = lv.obj(scrFan)
scrFan_cont0.set_pos(int(0),int(0))
scrFan_cont0.set_size(480,33)
scrFan_cont0.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrfan_cont0_main_main_default
style_scrfan_cont0_main_main_default = lv.style_t()
style_scrfan_cont0_main_main_default.init()
style_scrfan_cont0_main_main_default.set_radius(0)
style_scrfan_cont0_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_scrfan_cont0_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_scrfan_cont0_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_cont0_main_main_default.set_bg_opa(255)
style_scrfan_cont0_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrfan_cont0_main_main_default.set_border_width(0)
style_scrfan_cont0_main_main_default.set_border_opa(255)
style_scrfan_cont0_main_main_default.set_pad_left(0)
style_scrfan_cont0_main_main_default.set_pad_right(0)
style_scrfan_cont0_main_main_default.set_pad_top(0)
style_scrfan_cont0_main_main_default.set_pad_bottom(0)

# add style for scrFan_cont0
scrFan_cont0.add_style(style_scrfan_cont0_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_con2 = lv.obj(scrFan)
scrFan_con2.set_pos(int(0),int(15))
scrFan_con2.set_size(480,252)
scrFan_con2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrfan_con2_main_main_default
style_scrfan_con2_main_main_default = lv.style_t()
style_scrfan_con2_main_main_default.init()
style_scrfan_con2_main_main_default.set_radius(0)
style_scrfan_con2_main_main_default.set_bg_color(lv.color_make(0xde,0xde,0xde))
style_scrfan_con2_main_main_default.set_bg_grad_color(lv.color_make(0xde,0xde,0xde))
style_scrfan_con2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_con2_main_main_default.set_bg_opa(255)
style_scrfan_con2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrfan_con2_main_main_default.set_border_width(0)
style_scrfan_con2_main_main_default.set_border_opa(255)
style_scrfan_con2_main_main_default.set_pad_left(0)
style_scrfan_con2_main_main_default.set_pad_right(0)
style_scrfan_con2_main_main_default.set_pad_top(0)
style_scrfan_con2_main_main_default.set_pad_bottom(0)

# add style for scrFan_con2
scrFan_con2.add_style(style_scrfan_con2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_cont1 = lv.obj(scrFan)
scrFan_cont1.set_pos(int(40),int(60))
scrFan_cont1.set_size(400,140)
scrFan_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrfan_cont1_main_main_default
style_scrfan_cont1_main_main_default = lv.style_t()
style_scrfan_cont1_main_main_default.init()
style_scrfan_cont1_main_main_default.set_radius(0)
style_scrfan_cont1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_cont1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_cont1_main_main_default.set_bg_opa(255)
style_scrfan_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrfan_cont1_main_main_default.set_border_width(0)
style_scrfan_cont1_main_main_default.set_border_opa(255)
style_scrfan_cont1_main_main_default.set_pad_left(0)
style_scrfan_cont1_main_main_default.set_pad_right(0)
style_scrfan_cont1_main_main_default.set_pad_top(0)
style_scrfan_cont1_main_main_default.set_pad_bottom(0)

# add style for scrFan_cont1
scrFan_cont1.add_style(style_scrfan_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_label4 = lv.label(scrFan)
scrFan_label4.set_pos(int(100),int(13))
scrFan_label4.set_size(281,30)
scrFan_label4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_label4.set_text("Fan condition")
scrFan_label4.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_label4_main_main_default
style_scrfan_label4_main_main_default = lv.style_t()
style_scrfan_label4_main_main_default.init()
style_scrfan_label4_main_main_default.set_radius(0)
style_scrfan_label4_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_label4_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_label4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_label4_main_main_default.set_bg_opa(0)
style_scrfan_label4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrfan_label4_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrfan_label4_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrfan_label4_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_label4_main_main_default.set_text_letter_space(2)
style_scrfan_label4_main_main_default.set_text_line_space(0)
style_scrfan_label4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_label4_main_main_default.set_pad_left(0)
style_scrfan_label4_main_main_default.set_pad_right(0)
style_scrfan_label4_main_main_default.set_pad_top(0)
style_scrfan_label4_main_main_default.set_pad_bottom(0)

# add style for scrFan_label4
scrFan_label4.add_style(style_scrfan_label4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_labelusb = lv.label(scrFan)
scrFan_labelusb.set_pos(int(115),int(160))
scrFan_labelusb.set_size(74,20)
scrFan_labelusb.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_labelusb.set_text("Room 1")
scrFan_labelusb.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_labelusb_main_main_default
style_scrfan_labelusb_main_main_default = lv.style_t()
style_scrfan_labelusb_main_main_default.init()
style_scrfan_labelusb_main_main_default.set_radius(0)
style_scrfan_labelusb_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_labelusb_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_labelusb_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_labelusb_main_main_default.set_bg_opa(0)
style_scrfan_labelusb_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrfan_labelusb_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrfan_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrfan_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_labelusb_main_main_default.set_text_letter_space(2)
style_scrfan_labelusb_main_main_default.set_text_line_space(0)
style_scrfan_labelusb_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_labelusb_main_main_default.set_pad_left(0)
style_scrfan_labelusb_main_main_default.set_pad_right(0)
style_scrfan_labelusb_main_main_default.set_pad_top(0)
style_scrfan_labelusb_main_main_default.set_pad_bottom(0)

# add style for scrFan_labelusb
scrFan_labelusb.add_style(style_scrfan_labelusb_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_labelmobile = lv.label(scrFan)
scrFan_labelmobile.set_pos(int(288),int(160))
scrFan_labelmobile.set_size(74,20)
scrFan_labelmobile.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_labelmobile.set_text("Room 2")
scrFan_labelmobile.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_labelmobile_main_main_default
style_scrfan_labelmobile_main_main_default = lv.style_t()
style_scrfan_labelmobile_main_main_default.init()
style_scrfan_labelmobile_main_main_default.set_radius(0)
style_scrfan_labelmobile_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_labelmobile_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrfan_labelmobile_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrfan_labelmobile_main_main_default.set_bg_opa(0)
style_scrfan_labelmobile_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrfan_labelmobile_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrfan_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrfan_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_labelmobile_main_main_default.set_text_letter_space(2)
style_scrfan_labelmobile_main_main_default.set_text_line_space(0)
style_scrfan_labelmobile_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_labelmobile_main_main_default.set_pad_left(0)
style_scrfan_labelmobile_main_main_default.set_pad_right(0)
style_scrfan_labelmobile_main_main_default.set_pad_top(0)
style_scrfan_labelmobile_main_main_default.set_pad_bottom(0)

# add style for scrFan_labelmobile
scrFan_labelmobile.add_style(style_scrfan_labelmobile_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_imgbtn_1 = lv.imgbtn(scrFan)
scrFan_imgbtn_1.set_pos(int(34),int(0))
scrFan_imgbtn_1.set_size(30,26)
scrFan_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrFan_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrFan_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(scrFan_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrFan_imgbtn_1_imgReleased_data
})
scrFan_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, scrFan_imgbtn_1_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrFan_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrFan_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(scrFan_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrFan_imgbtn_1_imgPressed_data
})
scrFan_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, scrFan_imgbtn_1_imgPressed, None, None)




scrFan_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
# create style style_scrfan_imgbtn_1_main_main_default
style_scrfan_imgbtn_1_main_main_default = lv.style_t()
style_scrfan_imgbtn_1_main_main_default.init()
style_scrfan_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrfan_imgbtn_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrfan_imgbtn_1_main_main_default.set_img_recolor_opa(0)
style_scrfan_imgbtn_1_main_main_default.set_img_opa(255)

# add style for scrFan_imgbtn_1
scrFan_imgbtn_1.add_style(style_scrfan_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrfan_imgbtn_1_main_main_pressed
style_scrfan_imgbtn_1_main_main_pressed = lv.style_t()
style_scrfan_imgbtn_1_main_main_pressed.init()
style_scrfan_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrfan_imgbtn_1_main_main_pressed.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrfan_imgbtn_1_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrfan_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_scrfan_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for scrFan_imgbtn_1
scrFan_imgbtn_1.add_style(style_scrfan_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrfan_imgbtn_1_main_main_checked
style_scrfan_imgbtn_1_main_main_checked = lv.style_t()
style_scrfan_imgbtn_1_main_main_checked.init()
style_scrfan_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrfan_imgbtn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrfan_imgbtn_1_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrfan_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_scrfan_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for scrFan_imgbtn_1
scrFan_imgbtn_1.add_style(style_scrfan_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrFan_ddlist_1 = lv.dropdown(scrFan)
scrFan_ddlist_1.set_pos(int(175),int(29))
scrFan_ddlist_1.set_size(130,30)
scrFan_ddlist_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_ddlist_1.set_options("Room 1\nRoom 2")

scrFan_ddlist_1_list = scrFan_ddlist_1.get_list()
# create style style_scrfan_ddlist_1_extra_list_selected_checked
style_scrfan_ddlist_1_extra_list_selected_checked = lv.style_t()
style_scrfan_ddlist_1_extra_list_selected_checked.init()
style_scrfan_ddlist_1_extra_list_selected_checked.set_radius(3)
style_scrfan_ddlist_1_extra_list_selected_checked.set_bg_color(lv.color_make(0x00,0xa1,0xb5))
style_scrfan_ddlist_1_extra_list_selected_checked.set_bg_grad_color(lv.color_make(0x00,0xa1,0xb5))
style_scrfan_ddlist_1_extra_list_selected_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_ddlist_1_extra_list_selected_checked.set_bg_opa(255)
style_scrfan_ddlist_1_extra_list_selected_checked.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrfan_ddlist_1_extra_list_selected_checked.set_border_width(1)
style_scrfan_ddlist_1_extra_list_selected_checked.set_border_opa(255)
style_scrfan_ddlist_1_extra_list_selected_checked.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrfan_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_16)
style_scrfan_ddlist_1_extra_list_selected_checked.set_pad_left(6)
style_scrfan_ddlist_1_extra_list_selected_checked.set_pad_right(6)
style_scrfan_ddlist_1_extra_list_selected_checked.set_pad_top(6)
style_scrfan_ddlist_1_extra_list_selected_checked.set_pad_bottom(6)

# add style for scrFan_ddlist_1_list
scrFan_ddlist_1_list.add_style(style_scrfan_ddlist_1_extra_list_selected_checked, lv.PART.SELECTED|lv.STATE.CHECKED)

# create style style_scrfan_ddlist_1_extra_list_main_default
style_scrfan_ddlist_1_extra_list_main_default = lv.style_t()
style_scrfan_ddlist_1_extra_list_main_default.init()
style_scrfan_ddlist_1_extra_list_main_default.set_radius(3)
style_scrfan_ddlist_1_extra_list_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_ddlist_1_extra_list_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_ddlist_1_extra_list_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_ddlist_1_extra_list_main_default.set_bg_opa(255)
style_scrfan_ddlist_1_extra_list_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrfan_ddlist_1_extra_list_main_default.set_border_width(1)
style_scrfan_ddlist_1_extra_list_main_default.set_border_opa(255)
style_scrfan_ddlist_1_extra_list_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrfan_ddlist_1_extra_list_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_ddlist_1_extra_list_main_default.set_pad_left(6)
style_scrfan_ddlist_1_extra_list_main_default.set_pad_right(6)
style_scrfan_ddlist_1_extra_list_main_default.set_pad_top(6)
style_scrfan_ddlist_1_extra_list_main_default.set_pad_bottom(6)
style_scrfan_ddlist_1_extra_list_main_default.set_max_height(90)

# add style for scrFan_ddlist_1_list
scrFan_ddlist_1_list.add_style(style_scrfan_ddlist_1_extra_list_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrfan_ddlist_1_extra_list_scrollbar_default
style_scrfan_ddlist_1_extra_list_scrollbar_default = lv.style_t()
style_scrfan_ddlist_1_extra_list_scrollbar_default.init()
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_radius(3)
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_bg_color(lv.color_make(0x00,0xff,0x00))
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_bg_opa(255)
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_pad_left(6)
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_pad_right(6)
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_pad_top(6)
style_scrfan_ddlist_1_extra_list_scrollbar_default.set_pad_bottom(6)

# add style for scrFan_ddlist_1_list
scrFan_ddlist_1_list.add_style(style_scrfan_ddlist_1_extra_list_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)

# create style style_scrfan_ddlist_1_main_main_default
style_scrfan_ddlist_1_main_main_default = lv.style_t()
style_scrfan_ddlist_1_main_main_default.init()
style_scrfan_ddlist_1_main_main_default.set_radius(3)
style_scrfan_ddlist_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_ddlist_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_ddlist_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_ddlist_1_main_main_default.set_bg_opa(255)
style_scrfan_ddlist_1_main_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrfan_ddlist_1_main_main_default.set_border_width(1)
style_scrfan_ddlist_1_main_main_default.set_border_opa(255)
style_scrfan_ddlist_1_main_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrfan_ddlist_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrfan_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_ddlist_1_main_main_default.set_pad_left(6)
style_scrfan_ddlist_1_main_main_default.set_pad_right(6)
style_scrfan_ddlist_1_main_main_default.set_pad_top(8)

# add style for scrFan_ddlist_1
scrFan_ddlist_1.add_style(style_scrfan_ddlist_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_label_1 = lv.label(scrFan)
scrFan_label_1.set_pos(int(313),int(125))
scrFan_label_1.set_size(88,55)
scrFan_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_label_1.set_text("ON")
scrFan_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_label_1_main_main_default
style_scrfan_label_1_main_main_default = lv.style_t()
style_scrfan_label_1_main_main_default.init()
style_scrfan_label_1_main_main_default.set_radius(0)
style_scrfan_label_1_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_label_1_main_main_default.set_bg_opa(0)
style_scrfan_label_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrfan_label_1_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrfan_label_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_label_1_main_main_default.set_text_letter_space(2)
style_scrfan_label_1_main_main_default.set_text_line_space(0)
style_scrfan_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_label_1_main_main_default.set_pad_left(0)
style_scrfan_label_1_main_main_default.set_pad_right(0)
style_scrfan_label_1_main_main_default.set_pad_top(20)
style_scrfan_label_1_main_main_default.set_pad_bottom(0)

# add style for scrFan_label_1
scrFan_label_1.add_style(style_scrfan_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_label_2 = lv.label(scrFan)
scrFan_label_2.set_pos(int(299),int(119))
scrFan_label_2.set_size(117,34)
scrFan_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_label_2.set_text("Fan condition")
scrFan_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_label_2_main_main_default
style_scrfan_label_2_main_main_default = lv.style_t()
style_scrfan_label_2_main_main_default.init()
style_scrfan_label_2_main_main_default.set_radius(0)
style_scrfan_label_2_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_label_2_main_main_default.set_bg_opa(0)
style_scrfan_label_2_main_main_default.set_text_color(lv.color_make(0x7e,0x07,0x07))
try:
    style_scrfan_label_2_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrfan_label_2_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_label_2_main_main_default.set_text_letter_space(2)
style_scrfan_label_2_main_main_default.set_text_line_space(0)
style_scrfan_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_label_2_main_main_default.set_pad_left(0)
style_scrfan_label_2_main_main_default.set_pad_right(0)
style_scrfan_label_2_main_main_default.set_pad_top(0)
style_scrfan_label_2_main_main_default.set_pad_bottom(0)

# add style for scrFan_label_2
scrFan_label_2.add_style(style_scrfan_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_chart_1 = lv.chart(scrFan)
scrFan_chart_1.set_pos(int(73),int(70))
scrFan_chart_1.set_size(158,92)
scrFan_chart_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_chart_1.set_type(lv.chart.TYPE.LINE)
scrFan_chart_1.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)
scrFan_chart_1.set_div_line_count(3, 5)
scrFan_chart_1.set_point_count(5)
chart_series_0 = lv.chart.add_series(scrFan_chart_1, lv.color_make(0x00,0x00,0x00), lv.chart.AXIS.PRIMARY_Y);
scrFan_chart_1.set_next_value(chart_series_0, 1)
scrFan_chart_1.set_next_value(chart_series_0, 20)
scrFan_chart_1.set_next_value(chart_series_0, 30)
scrFan_chart_1.set_next_value(chart_series_0, 40)
scrFan_chart_1.set_next_value(chart_series_0, 5)
# create style style_scrfan_chart_1_main_main_default
style_scrfan_chart_1_main_main_default = lv.style_t()
style_scrfan_chart_1_main_main_default.init()
style_scrfan_chart_1_main_main_default.set_radius(0)
style_scrfan_chart_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_chart_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrfan_chart_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_chart_1_main_main_default.set_bg_opa(255)
style_scrfan_chart_1_main_main_default.set_border_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrfan_chart_1_main_main_default.set_border_width(1)
style_scrfan_chart_1_main_main_default.set_border_opa(255)
style_scrfan_chart_1_main_main_default.set_line_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrfan_chart_1_main_main_default.set_line_width(2)
style_scrfan_chart_1_main_main_default.set_line_opa(255)

# add style for scrFan_chart_1
scrFan_chart_1.add_style(style_scrfan_chart_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrFan_label_5 = lv.label(scrFan)
scrFan_label_5.set_pos(int(68),int(180))
scrFan_label_5.set_size(163,32)
scrFan_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrFan_label_5.set_text("Time ON: 5 hours")
scrFan_label_5.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrfan_label_5_main_main_default
style_scrfan_label_5_main_main_default = lv.style_t()
style_scrfan_label_5_main_main_default.init()
style_scrfan_label_5_main_main_default.set_radius(0)
style_scrfan_label_5_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_5_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrfan_label_5_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrfan_label_5_main_main_default.set_bg_opa(0)
style_scrfan_label_5_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrfan_label_5_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrfan_label_5_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrfan_label_5_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrfan_label_5_main_main_default.set_text_letter_space(2)
style_scrfan_label_5_main_main_default.set_text_line_space(0)
style_scrfan_label_5_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrfan_label_5_main_main_default.set_pad_left(0)
style_scrfan_label_5_main_main_default.set_pad_right(0)
style_scrfan_label_5_main_main_default.set_pad_top(0)
style_scrfan_label_5_main_main_default.set_pad_bottom(0)

# add style for scrFan_label_5
scrFan_label_5.add_style(style_scrfan_label_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight = lv.obj()
scrnLight.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnlight_main_main_default
style_scrnlight_main_main_default = lv.style_t()
style_scrnlight_main_main_default.init()
style_scrnlight_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_main_main_default.set_bg_opa(0)

# add style for scrnLight
scrnLight.add_style(style_scrnlight_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_cont0 = lv.obj(scrnLight)
scrnLight_cont0.set_pos(int(0),int(0))
scrnLight_cont0.set_size(480,33)
scrnLight_cont0.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnlight_cont0_main_main_default
style_scrnlight_cont0_main_main_default = lv.style_t()
style_scrnlight_cont0_main_main_default.init()
style_scrnlight_cont0_main_main_default.set_radius(0)
style_scrnlight_cont0_main_main_default.set_bg_color(lv.color_make(0x2f,0x32,0x43))
style_scrnlight_cont0_main_main_default.set_bg_grad_color(lv.color_make(0x2f,0x32,0x43))
style_scrnlight_cont0_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_cont0_main_main_default.set_bg_opa(255)
style_scrnlight_cont0_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnlight_cont0_main_main_default.set_border_width(0)
style_scrnlight_cont0_main_main_default.set_border_opa(255)
style_scrnlight_cont0_main_main_default.set_pad_left(0)
style_scrnlight_cont0_main_main_default.set_pad_right(0)
style_scrnlight_cont0_main_main_default.set_pad_top(0)
style_scrnlight_cont0_main_main_default.set_pad_bottom(0)

# add style for scrnLight_cont0
scrnLight_cont0.add_style(style_scrnlight_cont0_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_con2 = lv.obj(scrnLight)
scrnLight_con2.set_pos(int(0),int(15))
scrnLight_con2.set_size(480,252)
scrnLight_con2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnlight_con2_main_main_default
style_scrnlight_con2_main_main_default = lv.style_t()
style_scrnlight_con2_main_main_default.init()
style_scrnlight_con2_main_main_default.set_radius(0)
style_scrnlight_con2_main_main_default.set_bg_color(lv.color_make(0xde,0xde,0xde))
style_scrnlight_con2_main_main_default.set_bg_grad_color(lv.color_make(0xde,0xde,0xde))
style_scrnlight_con2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_con2_main_main_default.set_bg_opa(255)
style_scrnlight_con2_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnlight_con2_main_main_default.set_border_width(0)
style_scrnlight_con2_main_main_default.set_border_opa(255)
style_scrnlight_con2_main_main_default.set_pad_left(0)
style_scrnlight_con2_main_main_default.set_pad_right(0)
style_scrnlight_con2_main_main_default.set_pad_top(0)
style_scrnlight_con2_main_main_default.set_pad_bottom(0)

# add style for scrnLight_con2
scrnLight_con2.add_style(style_scrnlight_con2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_cont1 = lv.obj(scrnLight)
scrnLight_cont1.set_pos(int(40),int(60))
scrnLight_cont1.set_size(400,140)
scrnLight_cont1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_scrnlight_cont1_main_main_default
style_scrnlight_cont1_main_main_default = lv.style_t()
style_scrnlight_cont1_main_main_default.init()
style_scrnlight_cont1_main_main_default.set_radius(0)
style_scrnlight_cont1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_cont1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_cont1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_cont1_main_main_default.set_bg_opa(255)
style_scrnlight_cont1_main_main_default.set_border_color(lv.color_make(0x00,0x00,0x00))
style_scrnlight_cont1_main_main_default.set_border_width(0)
style_scrnlight_cont1_main_main_default.set_border_opa(255)
style_scrnlight_cont1_main_main_default.set_pad_left(0)
style_scrnlight_cont1_main_main_default.set_pad_right(0)
style_scrnlight_cont1_main_main_default.set_pad_top(0)
style_scrnlight_cont1_main_main_default.set_pad_bottom(0)

# add style for scrnLight_cont1
scrnLight_cont1.add_style(style_scrnlight_cont1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_label4 = lv.label(scrnLight)
scrnLight_label4.set_pos(int(100),int(13))
scrnLight_label4.set_size(281,30)
scrnLight_label4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_label4.set_text(" Light condition")
scrnLight_label4.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_label4_main_main_default
style_scrnlight_label4_main_main_default = lv.style_t()
style_scrnlight_label4_main_main_default.init()
style_scrnlight_label4_main_main_default.set_radius(0)
style_scrnlight_label4_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_label4_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_label4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_label4_main_main_default.set_bg_opa(0)
style_scrnlight_label4_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnlight_label4_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnlight_label4_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnlight_label4_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_label4_main_main_default.set_text_letter_space(2)
style_scrnlight_label4_main_main_default.set_text_line_space(0)
style_scrnlight_label4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_label4_main_main_default.set_pad_left(0)
style_scrnlight_label4_main_main_default.set_pad_right(0)
style_scrnlight_label4_main_main_default.set_pad_top(0)
style_scrnlight_label4_main_main_default.set_pad_bottom(0)

# add style for scrnLight_label4
scrnLight_label4.add_style(style_scrnlight_label4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_labelusb = lv.label(scrnLight)
scrnLight_labelusb.set_pos(int(115),int(160))
scrnLight_labelusb.set_size(74,20)
scrnLight_labelusb.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_labelusb.set_text("Room 1")
scrnLight_labelusb.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_labelusb_main_main_default
style_scrnlight_labelusb_main_main_default = lv.style_t()
style_scrnlight_labelusb_main_main_default.init()
style_scrnlight_labelusb_main_main_default.set_radius(0)
style_scrnlight_labelusb_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_labelusb_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_labelusb_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_labelusb_main_main_default.set_bg_opa(0)
style_scrnlight_labelusb_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnlight_labelusb_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnlight_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnlight_labelusb_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_labelusb_main_main_default.set_text_letter_space(2)
style_scrnlight_labelusb_main_main_default.set_text_line_space(0)
style_scrnlight_labelusb_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_labelusb_main_main_default.set_pad_left(0)
style_scrnlight_labelusb_main_main_default.set_pad_right(0)
style_scrnlight_labelusb_main_main_default.set_pad_top(0)
style_scrnlight_labelusb_main_main_default.set_pad_bottom(0)

# add style for scrnLight_labelusb
scrnLight_labelusb.add_style(style_scrnlight_labelusb_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_labelmobile = lv.label(scrnLight)
scrnLight_labelmobile.set_pos(int(288),int(160))
scrnLight_labelmobile.set_size(74,20)
scrnLight_labelmobile.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_labelmobile.set_text("Room 2")
scrnLight_labelmobile.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_labelmobile_main_main_default
style_scrnlight_labelmobile_main_main_default = lv.style_t()
style_scrnlight_labelmobile_main_main_default.init()
style_scrnlight_labelmobile_main_main_default.set_radius(0)
style_scrnlight_labelmobile_main_main_default.set_bg_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_labelmobile_main_main_default.set_bg_grad_color(lv.color_make(0x4a,0xb2,0x41))
style_scrnlight_labelmobile_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.VER)
style_scrnlight_labelmobile_main_main_default.set_bg_opa(0)
style_scrnlight_labelmobile_main_main_default.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnlight_labelmobile_main_main_default.set_text_font(lv.font_arial_16)
except AttributeError:
    try:
        style_scrnlight_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_scrnlight_labelmobile_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_labelmobile_main_main_default.set_text_letter_space(2)
style_scrnlight_labelmobile_main_main_default.set_text_line_space(0)
style_scrnlight_labelmobile_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_labelmobile_main_main_default.set_pad_left(0)
style_scrnlight_labelmobile_main_main_default.set_pad_right(0)
style_scrnlight_labelmobile_main_main_default.set_pad_top(0)
style_scrnlight_labelmobile_main_main_default.set_pad_bottom(0)

# add style for scrnLight_labelmobile
scrnLight_labelmobile.add_style(style_scrnlight_labelmobile_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_imgbtn_1 = lv.imgbtn(scrnLight)
scrnLight_imgbtn_1.set_pos(int(34),int(0))
scrnLight_imgbtn_1.set_size(30,26)
scrnLight_imgbtn_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrnLight_imgbtn_1_imgReleased_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrnLight_imgbtn_1_imgReleased = lv.img_dsc_t({
  'data_size': len(scrnLight_imgbtn_1_imgReleased_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnLight_imgbtn_1_imgReleased_data
})
scrnLight_imgbtn_1.set_src(lv.imgbtn.STATE.RELEASED, scrnLight_imgbtn_1_imgReleased, None, None)

try:
    with open('C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png','rb') as f:
        scrnLight_imgbtn_1_imgPressed_data = f.read()
except:
    print('Could not open C:\\NXP\\GUI-Guider-Projects\\monitoring_GUI\\generated\\mPythonImages\\mp2010334983.png')
    sys.exit()

scrnLight_imgbtn_1_imgPressed = lv.img_dsc_t({
  'data_size': len(scrnLight_imgbtn_1_imgPressed_data),
  'header': {'always_zero': 0, 'w': 30, 'h': 26, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': scrnLight_imgbtn_1_imgPressed_data
})
scrnLight_imgbtn_1.set_src(lv.imgbtn.STATE.PRESSED, scrnLight_imgbtn_1_imgPressed, None, None)




scrnLight_imgbtn_1.add_flag(lv.obj.FLAG.CHECKABLE)
# create style style_scrnlight_imgbtn_1_main_main_default
style_scrnlight_imgbtn_1_main_main_default = lv.style_t()
style_scrnlight_imgbtn_1_main_main_default.init()
style_scrnlight_imgbtn_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrnlight_imgbtn_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_imgbtn_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_imgbtn_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_imgbtn_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_scrnlight_imgbtn_1_main_main_default.set_img_recolor_opa(0)
style_scrnlight_imgbtn_1_main_main_default.set_img_opa(255)

# add style for scrnLight_imgbtn_1
scrnLight_imgbtn_1.add_style(style_scrnlight_imgbtn_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrnlight_imgbtn_1_main_main_pressed
style_scrnlight_imgbtn_1_main_main_pressed = lv.style_t()
style_scrnlight_imgbtn_1_main_main_pressed.init()
style_scrnlight_imgbtn_1_main_main_pressed.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnlight_imgbtn_1_main_main_pressed.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_imgbtn_1_main_main_pressed.set_text_font(lv.font_montserrat_16)
style_scrnlight_imgbtn_1_main_main_pressed.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_imgbtn_1_main_main_pressed.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnlight_imgbtn_1_main_main_pressed.set_img_recolor_opa(0)
style_scrnlight_imgbtn_1_main_main_pressed.set_img_opa(255)

# add style for scrnLight_imgbtn_1
scrnLight_imgbtn_1.add_style(style_scrnlight_imgbtn_1_main_main_pressed, lv.PART.MAIN|lv.STATE.PRESSED)

# create style style_scrnlight_imgbtn_1_main_main_checked
style_scrnlight_imgbtn_1_main_main_checked = lv.style_t()
style_scrnlight_imgbtn_1_main_main_checked.init()
style_scrnlight_imgbtn_1_main_main_checked.set_text_color(lv.color_make(0xFF,0x33,0xFF))
try:
    style_scrnlight_imgbtn_1_main_main_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_imgbtn_1_main_main_checked.set_text_font(lv.font_montserrat_16)
style_scrnlight_imgbtn_1_main_main_checked.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_imgbtn_1_main_main_checked.set_img_recolor(lv.color_make(0x00,0x00,0x00))
style_scrnlight_imgbtn_1_main_main_checked.set_img_recolor_opa(0)
style_scrnlight_imgbtn_1_main_main_checked.set_img_opa(255)

# add style for scrnLight_imgbtn_1
scrnLight_imgbtn_1.add_style(style_scrnlight_imgbtn_1_main_main_checked, lv.PART.MAIN|lv.STATE.CHECKED)

scrnLight_ddlist_1 = lv.dropdown(scrnLight)
scrnLight_ddlist_1.set_pos(int(175),int(29))
scrnLight_ddlist_1.set_size(130,30)
scrnLight_ddlist_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_ddlist_1.set_options("Room 1\nRoom 2")

scrnLight_ddlist_1_list = scrnLight_ddlist_1.get_list()
# create style style_scrnlight_ddlist_1_extra_list_selected_checked
style_scrnlight_ddlist_1_extra_list_selected_checked = lv.style_t()
style_scrnlight_ddlist_1_extra_list_selected_checked.init()
style_scrnlight_ddlist_1_extra_list_selected_checked.set_radius(3)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_bg_color(lv.color_make(0x00,0xa1,0xb5))
style_scrnlight_ddlist_1_extra_list_selected_checked.set_bg_grad_color(lv.color_make(0x00,0xa1,0xb5))
style_scrnlight_ddlist_1_extra_list_selected_checked.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_bg_opa(255)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrnlight_ddlist_1_extra_list_selected_checked.set_border_width(1)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_border_opa(255)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_text_color(lv.color_make(0xff,0xff,0xff))
try:
    style_scrnlight_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_ddlist_1_extra_list_selected_checked.set_text_font(lv.font_montserrat_16)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_pad_left(6)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_pad_right(6)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_pad_top(6)
style_scrnlight_ddlist_1_extra_list_selected_checked.set_pad_bottom(6)

# add style for scrnLight_ddlist_1_list
scrnLight_ddlist_1_list.add_style(style_scrnlight_ddlist_1_extra_list_selected_checked, lv.PART.SELECTED|lv.STATE.CHECKED)

# create style style_scrnlight_ddlist_1_extra_list_main_default
style_scrnlight_ddlist_1_extra_list_main_default = lv.style_t()
style_scrnlight_ddlist_1_extra_list_main_default.init()
style_scrnlight_ddlist_1_extra_list_main_default.set_radius(3)
style_scrnlight_ddlist_1_extra_list_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_ddlist_1_extra_list_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_ddlist_1_extra_list_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_ddlist_1_extra_list_main_default.set_bg_opa(255)
style_scrnlight_ddlist_1_extra_list_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrnlight_ddlist_1_extra_list_main_default.set_border_width(1)
style_scrnlight_ddlist_1_extra_list_main_default.set_border_opa(255)
style_scrnlight_ddlist_1_extra_list_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrnlight_ddlist_1_extra_list_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_ddlist_1_extra_list_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_ddlist_1_extra_list_main_default.set_pad_left(6)
style_scrnlight_ddlist_1_extra_list_main_default.set_pad_right(6)
style_scrnlight_ddlist_1_extra_list_main_default.set_pad_top(6)
style_scrnlight_ddlist_1_extra_list_main_default.set_pad_bottom(6)
style_scrnlight_ddlist_1_extra_list_main_default.set_max_height(90)

# add style for scrnLight_ddlist_1_list
scrnLight_ddlist_1_list.add_style(style_scrnlight_ddlist_1_extra_list_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_scrnlight_ddlist_1_extra_list_scrollbar_default
style_scrnlight_ddlist_1_extra_list_scrollbar_default = lv.style_t()
style_scrnlight_ddlist_1_extra_list_scrollbar_default.init()
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_radius(3)
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_bg_color(lv.color_make(0x00,0xff,0x00))
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_bg_opa(255)
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_pad_left(6)
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_pad_right(6)
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_pad_top(6)
style_scrnlight_ddlist_1_extra_list_scrollbar_default.set_pad_bottom(6)

# add style for scrnLight_ddlist_1_list
scrnLight_ddlist_1_list.add_style(style_scrnlight_ddlist_1_extra_list_scrollbar_default, lv.PART.SCROLLBAR|lv.STATE.DEFAULT)

# create style style_scrnlight_ddlist_1_main_main_default
style_scrnlight_ddlist_1_main_main_default = lv.style_t()
style_scrnlight_ddlist_1_main_main_default.init()
style_scrnlight_ddlist_1_main_main_default.set_radius(3)
style_scrnlight_ddlist_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_ddlist_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_ddlist_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_ddlist_1_main_main_default.set_bg_opa(255)
style_scrnlight_ddlist_1_main_main_default.set_border_color(lv.color_make(0xe1,0xe6,0xee))
style_scrnlight_ddlist_1_main_main_default.set_border_width(1)
style_scrnlight_ddlist_1_main_main_default.set_border_opa(255)
style_scrnlight_ddlist_1_main_main_default.set_text_color(lv.color_make(0x0D,0x30,0x55))
try:
    style_scrnlight_ddlist_1_main_main_default.set_text_font(lv.font_simsun_12)
except AttributeError:
    try:
        style_scrnlight_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_ddlist_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_ddlist_1_main_main_default.set_pad_left(6)
style_scrnlight_ddlist_1_main_main_default.set_pad_right(6)
style_scrnlight_ddlist_1_main_main_default.set_pad_top(8)

# add style for scrnLight_ddlist_1
scrnLight_ddlist_1.add_style(style_scrnlight_ddlist_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_label_4 = lv.label(scrnLight)
scrnLight_label_4.set_pos(int(307),int(136))
scrnLight_label_4.set_size(100,32)
scrnLight_label_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_label_4.set_text("ON")
scrnLight_label_4.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_label_4_main_main_default
style_scrnlight_label_4_main_main_default = lv.style_t()
style_scrnlight_label_4_main_main_default.init()
style_scrnlight_label_4_main_main_default.set_radius(0)
style_scrnlight_label_4_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_4_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_label_4_main_main_default.set_bg_opa(0)
style_scrnlight_label_4_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrnlight_label_4_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnlight_label_4_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_label_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_label_4_main_main_default.set_text_letter_space(2)
style_scrnlight_label_4_main_main_default.set_text_line_space(0)
style_scrnlight_label_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_label_4_main_main_default.set_pad_left(0)
style_scrnlight_label_4_main_main_default.set_pad_right(0)
style_scrnlight_label_4_main_main_default.set_pad_top(0)
style_scrnlight_label_4_main_main_default.set_pad_bottom(0)

# add style for scrnLight_label_4
scrnLight_label_4.add_style(style_scrnlight_label_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_chart_1 = lv.chart(scrnLight)
scrnLight_chart_1.set_pos(int(73),int(70))
scrnLight_chart_1.set_size(158,92)
scrnLight_chart_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_chart_1.set_type(lv.chart.TYPE.LINE)
scrnLight_chart_1.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)
scrnLight_chart_1.set_div_line_count(3, 5)
scrnLight_chart_1.set_point_count(5)
chart_series_0 = lv.chart.add_series(scrnLight_chart_1, lv.color_make(0x00,0x00,0x00), lv.chart.AXIS.PRIMARY_Y);
scrnLight_chart_1.set_next_value(chart_series_0, 1)
scrnLight_chart_1.set_next_value(chart_series_0, 20)
scrnLight_chart_1.set_next_value(chart_series_0, 30)
scrnLight_chart_1.set_next_value(chart_series_0, 40)
scrnLight_chart_1.set_next_value(chart_series_0, 5)
# create style style_scrnlight_chart_1_main_main_default
style_scrnlight_chart_1_main_main_default = lv.style_t()
style_scrnlight_chart_1_main_main_default.init()
style_scrnlight_chart_1_main_main_default.set_radius(0)
style_scrnlight_chart_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_chart_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_scrnlight_chart_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_chart_1_main_main_default.set_bg_opa(255)
style_scrnlight_chart_1_main_main_default.set_border_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrnlight_chart_1_main_main_default.set_border_width(1)
style_scrnlight_chart_1_main_main_default.set_border_opa(255)
style_scrnlight_chart_1_main_main_default.set_line_color(lv.color_make(0xe8,0xe8,0xe8))
style_scrnlight_chart_1_main_main_default.set_line_width(2)
style_scrnlight_chart_1_main_main_default.set_line_opa(255)

# add style for scrnLight_chart_1
scrnLight_chart_1.add_style(style_scrnlight_chart_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_label_3 = lv.label(scrnLight)
scrnLight_label_3.set_pos(int(299),int(105))
scrnLight_label_3.set_size(117,63)
scrnLight_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_label_3.set_text("Light condition")
scrnLight_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_label_3_main_main_default
style_scrnlight_label_3_main_main_default = lv.style_t()
style_scrnlight_label_3_main_main_default.init()
style_scrnlight_label_3_main_main_default.set_radius(0)
style_scrnlight_label_3_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_label_3_main_main_default.set_bg_opa(0)
style_scrnlight_label_3_main_main_default.set_text_color(lv.color_make(0x7e,0x07,0x07))
try:
    style_scrnlight_label_3_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnlight_label_3_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_label_3_main_main_default.set_text_letter_space(2)
style_scrnlight_label_3_main_main_default.set_text_line_space(0)
style_scrnlight_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_label_3_main_main_default.set_pad_left(0)
style_scrnlight_label_3_main_main_default.set_pad_right(0)
style_scrnlight_label_3_main_main_default.set_pad_top(0)
style_scrnlight_label_3_main_main_default.set_pad_bottom(0)

# add style for scrnLight_label_3
scrnLight_label_3.add_style(style_scrnlight_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

scrnLight_label_5 = lv.label(scrnLight)
scrnLight_label_5.set_pos(int(68),int(168))
scrnLight_label_5.set_size(163,32)
scrnLight_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scrnLight_label_5.set_text("Time ON: 5 hours")
scrnLight_label_5.set_long_mode(lv.label.LONG.WRAP)
# create style style_scrnlight_label_5_main_main_default
style_scrnlight_label_5_main_main_default = lv.style_t()
style_scrnlight_label_5_main_main_default.init()
style_scrnlight_label_5_main_main_default.set_radius(0)
style_scrnlight_label_5_main_main_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_5_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_scrnlight_label_5_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_scrnlight_label_5_main_main_default.set_bg_opa(0)
style_scrnlight_label_5_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_scrnlight_label_5_main_main_default.set_text_font(lv.font_arial_12)
except AttributeError:
    try:
        style_scrnlight_label_5_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_scrnlight_label_5_main_main_default.set_text_font(lv.font_montserrat_16)
style_scrnlight_label_5_main_main_default.set_text_letter_space(2)
style_scrnlight_label_5_main_main_default.set_text_line_space(0)
style_scrnlight_label_5_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_scrnlight_label_5_main_main_default.set_pad_left(0)
style_scrnlight_label_5_main_main_default.set_pad_right(0)
style_scrnlight_label_5_main_main_default.set_pad_top(0)
style_scrnlight_label_5_main_main_default.set_pad_bottom(0)

# add style for scrnLight_label_5
scrnLight_label_5.add_style(style_scrnlight_label_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)




def home_screen_temp_but_pressed_1_event_cb(e,scrTemp):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(scrTemp, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
home_screen_temp_but.add_event_cb(lambda e: home_screen_temp_but_pressed_1_event_cb(e,scrTemp), lv.EVENT.PRESSED, None)




def scrHumid_imgbtn_1_pressed_1_event_cb(e,home_screen):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(home_screen, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrHumid_imgbtn_1.add_event_cb(lambda e: scrHumid_imgbtn_1_pressed_1_event_cb(e,home_screen), lv.EVENT.PRESSED, None)


def scrFan_imgbtn_1_pressed_1_event_cb(e,home_screen):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(home_screen, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrFan_imgbtn_1.add_event_cb(lambda e: scrFan_imgbtn_1_pressed_1_event_cb(e,home_screen), lv.EVENT.PRESSED, None)



def home_screen_imgbtn_fanlght_pressed_1_event_cb(e,scrnFanLightselect):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(scrnFanLightselect, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
home_screen_imgbtn_fanlght.add_event_cb(lambda e: home_screen_imgbtn_fanlght_pressed_1_event_cb(e,scrnFanLightselect), lv.EVENT.PRESSED, None)


def home_screen_imgbtn_humid_pressed_1_event_cb(e,scrHumid):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(scrHumid, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
home_screen_imgbtn_humid.add_event_cb(lambda e: home_screen_imgbtn_humid_pressed_1_event_cb(e,scrHumid), lv.EVENT.PRESSED, None)


def scrTemp_imgbtn_1_pressed_1_event_cb(e,home_screen):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(home_screen, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrTemp_imgbtn_1.add_event_cb(lambda e: scrTemp_imgbtn_1_pressed_1_event_cb(e,home_screen), lv.EVENT.PRESSED, None)


def scrnFanLightselect_imgbtn_humid_pressed_1_event_cb(e,scrFan):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(scrFan, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrnFanLightselect_imgbtn_humid.add_event_cb(lambda e: scrnFanLightselect_imgbtn_humid_pressed_1_event_cb(e,scrFan), lv.EVENT.PRESSED, None)



def scrnFanLightselect_imgbtn_fanlght_pressed_1_event_cb(e,scrnLight):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(scrnLight, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrnFanLightselect_imgbtn_fanlght.add_event_cb(lambda e: scrnFanLightselect_imgbtn_fanlght_pressed_1_event_cb(e,scrnLight), lv.EVENT.PRESSED, None)



def home_screen_imgbtn_surve_pressed_2_event_cb(e):
    src = e.get_target()
    code = e.get_code()
    guider_load_screen(ScreenEnum.SCR_SETUP)
    lv_demo_printer_anim_in_all(setup, 200)

home_screen_imgbtn_surve.add_event_cb(lambda e: home_screen_imgbtn_surve_pressed_2_event_cb(e), lv.EVENT.PRESSED, None)


def scrnLight_imgbtn_1_pressed_1_event_cb(e,home_screen):
    src = e.get_target()
    code = e.get_code()
    lv.scr_load_anim(home_screen, lv.SCR_LOAD_ANIM.OVER_TOP, 0, 0, False)
scrnLight_imgbtn_1.add_event_cb(lambda e: scrnLight_imgbtn_1_pressed_1_event_cb(e,home_screen), lv.EVENT.PRESSED, None)



# content from custom.py
class ScreenEnum:
    SCR_HOME = 0
    SCR_COPY_HOME = 1
    SCR_COPY_NEXT = 2
    SCR_SCAN_HOME = 3
    SCR_PRT_HOME = 4
    SCR_PRT_USB = 5
    SCR_PRT_MB = 6
    SCR_PRT_IT = 7
    SCR_SETUP = 8
    SCR_LOADER = 9
    SCR_SAVED = 10

LV_DEMO_PRINTER_ANIM_DELAY=40
LV_DEMO_PRINTER_ANIM_TIME=150
LV_DEMO_PRINTER_ANIM_TIME_BG=300
LOAD_ANIM_TIME=1000
lightness_act = 0
hue_act = 180
cur_scr = ScreenEnum.SCR_HOME
copy_counter = 1
prtusb_counter = 1
save_src = 0


def get_scr_by_id(scr_id):
    if(scr_id == ScreenEnum.SCR_HOME):
        return home
    elif(scr_id == ScreenEnum.SCR_COPY_HOME):
        return copyhome
    elif(scr_id == ScreenEnum.SCR_COPY_NEXT):
        return copynext
    elif(scr_id == ScreenEnum.SCR_SCAN_HOME):
        return scanhome
    elif(scr_id == ScreenEnum.SCR_PRT_HOME):
        return prthome
    elif(scr_id == ScreenEnum.SCR_PRT_USB):
        return prtusb
    elif(scr_id == ScreenEnum.SCR_PRT_MB):
        return prtmb
    elif(scr_id == ScreenEnum.SCR_PRT_IT):
        return printit
    elif(scr_id == ScreenEnum.SCR_SETUP):
        return setup
    elif(scr_id == ScreenEnum.SCR_LOADER):
        return loader
    elif(scr_id == ScreenEnum.SCR_SAVED):
        return saved

def load_disbtn_home_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        guider_load_screen(ScreenEnum.SCR_HOME)
        lv_demo_printer_anim_in_all(home, 100)

def load_copy_next_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
         guider_load_screen(ScreenEnum.SCR_COPY_NEXT)
         lv_demo_printer_anim_in_all(copynext, 200)

def hue_slider_event_cb(e, obj):
    src = e.get_target()
    code = e.get_code()
    if(code == lv.EVENT.VALUE_CHANGED):
        global hue_act
        hue_act = src.get_value()
        scan_img_color_refr(obj)


def lightness_slider_event_cb(e, obj):
    src = e.get_target()
    code = e.get_code()
    if(code == lv.EVENT.VALUE_CHANGED):
        global lightness_act
        lightness_act = src.get_value()
        scan_img_color_refr(obj)

def loader_anim_cb(arc, v):
    if(v > 100):
        v = 100
    arc.set_angles(270, int(v * 360 / 100 + 270))
    loader_loadlabel.set_text(str(v))

def copy_counter_event_cb(e, obj):
    code = e.get_code()
    print(code)
    if(code == lv.EVENT.PRESSED):
        global copy_counter
        if (obj == copynext_up):
            if(copy_counter < 200):
                copy_counter += 1
        else:
            if (copy_counter > 1):
                copy_counter -= 1
        print(copy_counter, obj)
        copynext_labelcnt.set_text(str(copy_counter))

def prtusb_counter_event_cb(e, obj):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        global prtusb_counter
        if (obj == prtusb_up):
            if(prtusb_counter < 200):
                prtusb_counter += 1
        else:
            if (prtusb_counter > 1):
                prtusb_counter -= 1
        print(prtusb_counter, obj)
        prtusb_labelcnt.set_text(str(prtusb_counter))

def load_print_finish_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        global save_src
        save_src = 2
        guider_load_screen(ScreenEnum.SCR_LOADER)
        add_loader(load_save)

def load_save_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        guider_load_screen(ScreenEnum.SCR_LOADER)
        global save_src
        save_src = 1
        add_loader(load_save)

def load_print_usb_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        guider_load_screen(ScreenEnum.SCR_PRT_USB)
        lv_demo_printer_anim_in_all(prtusb, 200)

def load_print_mobile_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        guider_load_screen(ScreenEnum.SCR_PRT_MB)
        lv_demo_printer_anim_in_all(prtmb, 200)

def load_print_it_cb(e):
    code = e.get_code()
    if(code == lv.EVENT.PRESSED):
        guider_load_screen(ScreenEnum.SCR_PRT_IT)
        lv_demo_printer_anim_in_all(printit, 200)

def copy_home_event_init():
    copyhome_btncopyback.add_event_cb(lambda e: load_disbtn_home_cb(e), lv.EVENT.CLICKED, None)

def scan_img_color_refr(obj):
    if lightness_act > 0:
        s = 100 - lightness_act
        v = 100
    else:
        s = 100
        v = 100 + lightness_act
    c = lv.color_hsv_to_rgb(hue_act,s,v)
    obj.set_style_img_recolor_opa(v, 0)
    obj.set_style_img_recolor(c, 0)

def anim_y_cb(obj, v):
    obj.set_y(v)

def lv_demo_printer_anim_in_all(obj, delay):
    child_cnts = lv.obj.get_child_cnt(obj)
    for i in range(child_cnts):
        child = lv.obj.get_child(obj, i)
        child.update_layout()
        # a = lv.anim_t()
        # a.init()
        # a.set_var(child)
        # a.set_time(LV_DEMO_PRINTER_ANIM_TIME)
        # a.set_delay(delay)
        # a.set_custom_exec_cb(lambda a, val: anim_y_cb(child,val))
        # a.set_values(child.get_y() - int(lv.scr_act().get_disp().driver.ver_res / 20), child.get_y())
        # lv.anim_t.start(a)
        child.fade_in(LV_DEMO_PRINTER_ANIM_TIME - 100, delay)


def load_copy(a):
    guider_load_screen(ScreenEnum.SCR_COPY_HOME)
    lv_demo_printer_anim_in_all(copyhome, 200)

def load_save(a):
    guider_load_screen(ScreenEnum.SCR_SAVED)
    if(save_src == 1):
        saved_label2.set_x(157)
        saved_label2.set_text("File saved")
    elif(save_src == 2):
        saved_label2.set_x(157)
        saved_label2.set_text("Printing finished")
    else:
        saved_label2.set_x(157)
        saved_label2.set_text("File saved")
    lv_demo_printer_anim_in_all(saved, 200)

def load_home(a):
    guider_load_screen(ScreenEnum.SCR_HOME)


def load_scan(a):
    guider_load_screen(ScreenEnum.SCR_SCAN_HOME)
    lv_demo_printer_anim_in_all(scanhome, 200)

def load_setup(a):
    guider_load_screen(ScreenEnum.SCR_SETUP)
    lv_demo_printer_anim_in_all(setup, 200)

def load_print(a):
    guider_load_screen(ScreenEnum.SCR_PRT_HOME)
    lv_demo_printer_anim_in_all(prthome, 200)

# loading event function support.
def add_loader(end_cb):
    loader_loadarc.set_angles(270, 270)
    a = lv.anim_t()
    a.init()
    a.set_time(LOAD_ANIM_TIME)
    a.set_values(0, 110)
    a.set_var(loader_loadarc)
    a.set_custom_exec_cb(lambda a,val: loader_anim_cb(loader_loadarc,val))
    a.set_ready_cb(end_cb)
    lv.anim_t.start(a)


def guider_load_screen(scr_id):
    scr = None
    if(scr_id == ScreenEnum.SCR_HOME):
        scr = home
    elif(scr_id == ScreenEnum.SCR_COPY_HOME):
        scr = copyhome
        copyhome_img3.set_style_radius(8, lv.STATE.DEFAULT)
        copyhome_img3.set_style_clip_corner(True, lv.STATE.DEFAULT)
        copyhome_img3.set_style_bg_img_recolor_opa(180, lv.STATE.DEFAULT)

    elif(scr_id == ScreenEnum.SCR_COPY_NEXT):
        scr = copynext
        global copy_counter
        copy_counter = 1
        copynext_labelcnt.set_text(str(copy_counter))
        copynext_print.clear_flag(False)
    elif(scr_id == ScreenEnum.SCR_SCAN_HOME):
        scr = scanhome
        scanhome_img3.set_style_radius(8, lv.STATE.DEFAULT)
        scanhome_img3.set_style_clip_corner(True, lv.STATE.DEFAULT)
        scanhome_img3.set_style_bg_img_recolor_opa(180, lv.STATE.DEFAULT)
    elif(scr_id == ScreenEnum.SCR_PRT_HOME):
        scr = prthome
        global prtusb_counter
        prtusb_counter = 1
        prtusb_labelcnt.set_text(str(prtusb_counter))
    elif(scr_id == ScreenEnum.SCR_PRT_USB):
        scr = prtusb
    elif(scr_id == ScreenEnum.SCR_PRT_MB):
        scr = prtmb
    elif(scr_id == ScreenEnum.SCR_PRT_IT):
        scr = printit
    elif(scr_id == ScreenEnum.SCR_SETUP):
        scr = setup
    elif(scr_id == ScreenEnum.SCR_LOADER):
        scr = loader
        # loader_loadarc.add_style(lv.STATE.DEFAULT)
    elif(scr_id == ScreenEnum.SCR_SAVED):
        scr = saved
        saved_btnsavecontinue_label.set_style_text_font(lv.font_montserrat_14, lv.STATE.DEFAULT)
    else:
        scr = None
    
    lv.scr_load(scr)

copyhome_btncopyback.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
copyhome_btncopynext.add_event_cb(load_copy_next_cb, lv.EVENT.ALL, None)
copyhome_sliderhue.add_event_cb(lambda e: hue_slider_event_cb(e, copyhome_img3), lv.EVENT.ALL, None)
copyhome_sliderbright.add_event_cb(lambda e: lightness_slider_event_cb(e, copyhome_img3), lv.EVENT.ALL, None)
copynext_up.add_event_cb(lambda e: copy_counter_event_cb(e, copynext_up),lv.EVENT.ALL, None)
copynext_down.add_event_cb(lambda e: copy_counter_event_cb(e, copynext_down),lv.EVENT.ALL, None)
copynext_print.add_event_cb(lambda e: load_print_finish_cb(e), lv.EVENT.ALL, None)
scanhome_btnscanback.add_event_cb(lambda e: load_disbtn_home_cb(e), lv.EVENT.ALL, None)
scanhome_btnscansave.add_event_cb(lambda e: load_save_cb(e), lv.EVENT.ALL, None)
scanhome_sliderhue.add_event_cb(lambda e: hue_slider_event_cb(e, scanhome_img3), lv.EVENT.ALL, None)
scanhome_sliderbright.add_event_cb(lambda e: lightness_slider_event_cb(e, scanhome_img3), lv.EVENT.ALL, None)
prthome_imgbtnusb.add_event_cb(load_print_usb_cb, lv.EVENT.ALL, None)
prthome_imgbtnmobile.add_event_cb(load_print_mobile_cb, lv.EVENT.ALL, None)
prthome_imgbtnit.add_event_cb(load_print_it_cb, lv.EVENT.ALL, None)
prthome_btnprintback.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
prtusb_back.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
prtusb_btnprint.add_event_cb(load_print_finish_cb, lv.EVENT.ALL, None)
prtusb_up.add_event_cb(lambda e: prtusb_counter_event_cb(e, prtusb_up),lv.EVENT.ALL, None)
prtusb_down.add_event_cb(lambda e: prtusb_counter_event_cb(e, prtusb_down),lv.EVENT.ALL, None)
prtmb_btnback.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
printit_btnprtitback.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
setup_btnsetback.add_event_cb(load_disbtn_home_cb, lv.EVENT.ALL, None)
saved_btnsavecontinue.add_event_cb(lambda e: load_disbtn_home_cb(e), lv.EVENT.ALL, None)

# Load the default screen
lv.scr_load(home_screen)

while SDL.check():
    time.sleep_ms(5)
