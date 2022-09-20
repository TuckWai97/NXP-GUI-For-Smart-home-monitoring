/*
 * Copyright 2022 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#ifndef GUI_GUIDER_H
#define GUI_GUIDER_H
#ifdef __cplusplus
extern "C" {
#endif

#include "lvgl.h"
#include "guider_fonts.h"

typedef struct
{
	lv_obj_t *home_screen;
	bool home_screen_del;
	lv_obj_t *home_screen_cont1;
	lv_obj_t *home_screen_whitebg;
	lv_obj_t *home_screen_cont2;
	lv_obj_t *home_screen_imgbtn_surve;
	lv_obj_t *home_screen_imgbtn_surve_label;
	lv_obj_t *home_screen_imgbtn_humid;
	lv_obj_t *home_screen_imgbtn_humid_label;
	lv_obj_t *home_screen_imgbtn_fanlght;
	lv_obj_t *home_screen_imgbtn_fanlght_label;
	lv_obj_t *home_screen_img_fan;
	lv_obj_t *home_screen_labelhumid;
	lv_obj_t *home_screen_labelfanlight;
	lv_obj_t *home_screen_labelsurvel;
	lv_obj_t *home_screen_imgcopy;
	lv_obj_t *home_screen_imgscan;
	lv_obj_t *home_screen_imglight;
	lv_obj_t *home_screen_imgsurve;
	lv_obj_t *home_screen_temp_but;
	lv_obj_t *home_screen_temp_but_label;
	lv_obj_t *home_screen_label_2;
	lv_obj_t *home_screen_img_1;
	lv_obj_t *home_screen_label_3;
	lv_obj_t *scrTemp;
	bool scrTemp_del;
	lv_obj_t *scrTemp_cont0;
	lv_obj_t *scrTemp_con2;
	lv_obj_t *scrTemp_cont1;
	lv_obj_t *scrTemp_label4;
	lv_obj_t *scrTemp_labelusb;
	lv_obj_t *scrTemp_labelmobile;
	lv_obj_t *scrTemp_imgbtn_1;
	lv_obj_t *scrTemp_imgbtn_1_label;
	lv_obj_t *scrTemp_ddlist_1;
	lv_obj_t *scrTemp_label_1;
	lv_obj_t *scrTemp_label_2;
	lv_obj_t *scrTemp_chart_1;
	lv_obj_t *scrHumid;
	bool scrHumid_del;
	lv_obj_t *scrHumid_cont0;
	lv_obj_t *scrHumid_con2;
	lv_obj_t *scrHumid_cont1;
	lv_obj_t *scrHumid_label4;
	lv_obj_t *scrHumid_labelusb;
	lv_obj_t *scrHumid_labelmobile;
	lv_obj_t *scrHumid_imgbtn_1;
	lv_obj_t *scrHumid_imgbtn_1_label;
	lv_obj_t *scrHumid_ddlist_1;
	lv_obj_t *scrHumid_label_1;
	lv_obj_t *scrHumid_label_2;
	lv_obj_t *scrHumid_chart_1;
	lv_obj_t *scrnFanLightselect;
	bool scrnFanLightselect_del;
	lv_obj_t *scrnFanLightselect_cont1;
	lv_obj_t *scrnFanLightselect_whitebg;
	lv_obj_t *scrnFanLightselect_cont2;
	lv_obj_t *scrnFanLightselect_imgbtn_humid;
	lv_obj_t *scrnFanLightselect_imgbtn_humid_label;
	lv_obj_t *scrnFanLightselect_imgbtn_fanlght;
	lv_obj_t *scrnFanLightselect_imgbtn_fanlght_label;
	lv_obj_t *scrnFanLightselect_img_fan;
	lv_obj_t *scrnFanLightselect_labelhumid;
	lv_obj_t *scrnFanLightselect_labelfanlight;
	lv_obj_t *scrnFanLightselect_imgcopy;
	lv_obj_t *scrnFanLightselect_imglight;
	lv_obj_t *scrnFanLightselect_label_3;
	lv_obj_t *scrFan;
	bool scrFan_del;
	lv_obj_t *scrFan_cont0;
	lv_obj_t *scrFan_con2;
	lv_obj_t *scrFan_cont1;
	lv_obj_t *scrFan_label4;
	lv_obj_t *scrFan_labelusb;
	lv_obj_t *scrFan_labelmobile;
	lv_obj_t *scrFan_imgbtn_1;
	lv_obj_t *scrFan_imgbtn_1_label;
	lv_obj_t *scrFan_ddlist_1;
	lv_obj_t *scrFan_label_1;
	lv_obj_t *scrFan_label_2;
	lv_obj_t *scrFan_chart_1;
	lv_obj_t *scrFan_label_5;
	lv_obj_t *scrnLight;
	bool scrnLight_del;
	lv_obj_t *scrnLight_cont0;
	lv_obj_t *scrnLight_con2;
	lv_obj_t *scrnLight_cont1;
	lv_obj_t *scrnLight_label4;
	lv_obj_t *scrnLight_labelusb;
	lv_obj_t *scrnLight_labelmobile;
	lv_obj_t *scrnLight_imgbtn_1;
	lv_obj_t *scrnLight_imgbtn_1_label;
	lv_obj_t *scrnLight_ddlist_1;
	lv_obj_t *scrnLight_label_4;
	lv_obj_t *scrnLight_chart_1;
	lv_obj_t *scrnLight_label_3;
	lv_obj_t *scrnLight_label_5;
}lv_ui;

void init_scr_del_flag(lv_ui *ui);
void setup_ui(lv_ui *ui);
extern lv_ui guider_ui;
void setup_scr_home_screen(lv_ui *ui);
void setup_scr_scrTemp(lv_ui *ui);
void setup_scr_scrHumid(lv_ui *ui);
void setup_scr_scrnFanLightselect(lv_ui *ui);
void setup_scr_scrFan(lv_ui *ui);
void setup_scr_scrnLight(lv_ui *ui);
LV_IMG_DECLARE(_fan_31x29);
LV_IMG_DECLARE(_copy_29x29);
LV_IMG_DECLARE(_home_alpha_30x26);
LV_IMG_DECLARE(_humidity_29x29);
LV_IMG_DECLARE(_cctv_29x29);
LV_IMG_DECLARE(_btn3_alpha_96x100);
LV_IMG_DECLARE(_btn4_alpha_96x100);
LV_IMG_DECLARE(_light_31x29);
LV_IMG_DECLARE(_btn2_alpha_96x100);
LV_IMG_DECLARE(_temperature_29x29);
LV_IMG_DECLARE(_btn_bg_1_alpha_96x100);

#ifdef __cplusplus
}
#endif
#endif