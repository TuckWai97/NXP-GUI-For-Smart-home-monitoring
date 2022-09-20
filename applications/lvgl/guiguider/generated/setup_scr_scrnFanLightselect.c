/*
 * Copyright 2022 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"
#include "events_init.h"
#include "custom.h"


void setup_scr_scrnFanLightselect(lv_ui *ui){

	//Write codes scrnFanLightselect
	ui->scrnFanLightselect = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_main_main_default
	static lv_style_t style_scrnfanlightselect_main_main_default;
	if (style_scrnfanlightselect_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_main_main_default);
	lv_style_set_bg_color(&style_scrnfanlightselect_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_scrnfanlightselect_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect, &style_scrnfanlightselect_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_cont1
	ui->scrnFanLightselect_cont1 = lv_obj_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_cont1, 0, 0);
	lv_obj_set_size(ui->scrnFanLightselect_cont1, 480, 95);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_cont1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_cont1_main_main_default
	static lv_style_t style_scrnfanlightselect_cont1_main_main_default;
	if (style_scrnfanlightselect_cont1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_cont1_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_cont1_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_cont1_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_cont1_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_cont1_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrnfanlightselect_cont1_main_main_default, 255);
	lv_style_set_border_color(&style_scrnfanlightselect_cont1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_style_set_border_opa(&style_scrnfanlightselect_cont1_main_main_default, 255);
	lv_style_set_pad_left(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_cont1_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_cont1, &style_scrnfanlightselect_cont1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_whitebg
	ui->scrnFanLightselect_whitebg = lv_obj_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_whitebg, 0, 96);
	lv_obj_set_size(ui->scrnFanLightselect_whitebg, 480, 177);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_whitebg, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_whitebg_main_main_default
	static lv_style_t style_scrnfanlightselect_whitebg_main_main_default;
	if (style_scrnfanlightselect_whitebg_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_whitebg_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_whitebg_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_whitebg_main_main_default, lv_color_make(0xd6, 0xdc, 0xd6));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_whitebg_main_main_default, lv_color_make(0xd9, 0xd9, 0xd9));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_whitebg_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrnfanlightselect_whitebg_main_main_default, 255);
	lv_style_set_border_color(&style_scrnfanlightselect_whitebg_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_style_set_border_opa(&style_scrnfanlightselect_whitebg_main_main_default, 255);
	lv_style_set_pad_left(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_whitebg_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_whitebg, &style_scrnfanlightselect_whitebg_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_cont2
	ui->scrnFanLightselect_cont2 = lv_obj_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_cont2, 40, 80);
	lv_obj_set_size(ui->scrnFanLightselect_cont2, 380, 120);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_cont2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_cont2_main_main_default
	static lv_style_t style_scrnfanlightselect_cont2_main_main_default;
	if (style_scrnfanlightselect_cont2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_cont2_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_cont2_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_cont2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_cont2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_cont2_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrnfanlightselect_cont2_main_main_default, 255);
	lv_style_set_border_color(&style_scrnfanlightselect_cont2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_style_set_border_opa(&style_scrnfanlightselect_cont2_main_main_default, 255);
	lv_style_set_pad_left(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_cont2_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_cont2, &style_scrnfanlightselect_cont2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_imgbtn_humid
	ui->scrnFanLightselect_imgbtn_humid = lv_imgbtn_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_imgbtn_humid, 139, 87);
	lv_obj_set_size(ui->scrnFanLightselect_imgbtn_humid, 96, 100);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_imgbtn_humid, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_imgbtn_humid_main_main_default
	static lv_style_t style_scrnfanlightselect_imgbtn_humid_main_main_default;
	if (style_scrnfanlightselect_imgbtn_humid_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_humid_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_humid_main_main_default);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_humid_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_humid_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_humid_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_default, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_default, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_humid, &style_scrnfanlightselect_imgbtn_humid_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_scrnfanlightselect_imgbtn_humid_main_main_pressed
	static lv_style_t style_scrnfanlightselect_imgbtn_humid_main_main_pressed;
	if (style_scrnfanlightselect_imgbtn_humid_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_pressed, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_humid, &style_scrnfanlightselect_imgbtn_humid_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_scrnfanlightselect_imgbtn_humid_main_main_checked
	static lv_style_t style_scrnfanlightselect_imgbtn_humid_main_main_checked;
	if (style_scrnfanlightselect_imgbtn_humid_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_humid_main_main_checked);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_humid_main_main_checked);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_humid_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_humid_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_humid_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_checked, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_humid_main_main_checked, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_humid, &style_scrnfanlightselect_imgbtn_humid_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_humid, LV_IMGBTN_STATE_RELEASED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_humid, LV_IMGBTN_STATE_PRESSED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_humid, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_humid, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn2_alpha_96x100, NULL);

	//Write codes scrnFanLightselect_imgbtn_fanlght
	ui->scrnFanLightselect_imgbtn_fanlght = lv_imgbtn_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_imgbtn_fanlght, 230, 86);
	lv_obj_set_size(ui->scrnFanLightselect_imgbtn_fanlght, 96, 100);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_imgbtn_fanlght, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_imgbtn_fanlght_main_main_default
	static lv_style_t style_scrnfanlightselect_imgbtn_fanlght_main_main_default;
	if (style_scrnfanlightselect_imgbtn_fanlght_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_default, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_fanlght, &style_scrnfanlightselect_imgbtn_fanlght_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed
	static lv_style_t style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed;
	if (style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_fanlght, &style_scrnfanlightselect_imgbtn_fanlght_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_scrnfanlightselect_imgbtn_fanlght_main_main_checked
	static lv_style_t style_scrnfanlightselect_imgbtn_fanlght_main_main_checked;
	if (style_scrnfanlightselect_imgbtn_fanlght_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked);
	else
		lv_style_init(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked);
	lv_style_set_text_color(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgbtn_fanlght, &style_scrnfanlightselect_imgbtn_fanlght_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_fanlght, LV_IMGBTN_STATE_RELEASED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_fanlght, LV_IMGBTN_STATE_PRESSED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_fanlght, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->scrnFanLightselect_imgbtn_fanlght, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn3_alpha_96x100, NULL);

	//Write codes scrnFanLightselect_img_fan
	ui->scrnFanLightselect_img_fan = lv_img_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_img_fan, 172, 119);
	lv_obj_set_size(ui->scrnFanLightselect_img_fan, 31, 29);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_img_fan, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_img_fan_main_main_default
	static lv_style_t style_scrnfanlightselect_img_fan_main_main_default;
	if (style_scrnfanlightselect_img_fan_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_img_fan_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_img_fan_main_main_default);
	lv_style_set_img_recolor(&style_scrnfanlightselect_img_fan_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_img_fan_main_main_default, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_img_fan_main_main_default, 255);
	lv_obj_add_style(ui->scrnFanLightselect_img_fan, &style_scrnfanlightselect_img_fan_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->scrnFanLightselect_img_fan, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->scrnFanLightselect_img_fan,&_fan_31x29);
	lv_img_set_pivot(ui->scrnFanLightselect_img_fan, 0,0);
	lv_img_set_angle(ui->scrnFanLightselect_img_fan, 0);

	//Write codes scrnFanLightselect_labelhumid
	ui->scrnFanLightselect_labelhumid = lv_label_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_labelhumid, 154, 156);
	lv_obj_set_size(ui->scrnFanLightselect_labelhumid, 67, 20);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_labelhumid, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrnFanLightselect_labelhumid, "Fan");
	lv_label_set_long_mode(ui->scrnFanLightselect_labelhumid, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_labelhumid_main_main_default
	static lv_style_t style_scrnfanlightselect_labelhumid_main_main_default;
	if (style_scrnfanlightselect_labelhumid_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_labelhumid_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_labelhumid_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_labelhumid_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_labelhumid_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_labelhumid_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_text_color(&style_scrnfanlightselect_labelhumid_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrnfanlightselect_labelhumid_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrnfanlightselect_labelhumid_main_main_default, 1);
	lv_style_set_text_line_space(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_text_align(&style_scrnfanlightselect_labelhumid_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_labelhumid_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_labelhumid, &style_scrnfanlightselect_labelhumid_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_labelfanlight
	ui->scrnFanLightselect_labelfanlight = lv_label_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_labelfanlight, 242, 156);
	lv_obj_set_size(ui->scrnFanLightselect_labelfanlight, 75, 36);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_labelfanlight, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrnFanLightselect_labelfanlight, "Light");
	lv_label_set_long_mode(ui->scrnFanLightselect_labelfanlight, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_labelfanlight_main_main_default
	static lv_style_t style_scrnfanlightselect_labelfanlight_main_main_default;
	if (style_scrnfanlightselect_labelfanlight_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_labelfanlight_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_labelfanlight_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_labelfanlight_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_labelfanlight_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_labelfanlight_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_text_color(&style_scrnfanlightselect_labelfanlight_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrnfanlightselect_labelfanlight_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrnfanlightselect_labelfanlight_main_main_default, 1);
	lv_style_set_text_line_space(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_text_align(&style_scrnfanlightselect_labelfanlight_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_labelfanlight_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_labelfanlight, &style_scrnfanlightselect_labelfanlight_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrnFanLightselect_imgcopy
	ui->scrnFanLightselect_imgcopy = lv_img_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_imgcopy, 90, 108);
	lv_obj_set_size(ui->scrnFanLightselect_imgcopy, 29, 29);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_imgcopy, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_imgcopy_main_main_default
	static lv_style_t style_scrnfanlightselect_imgcopy_main_main_default;
	if (style_scrnfanlightselect_imgcopy_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imgcopy_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_imgcopy_main_main_default);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imgcopy_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imgcopy_main_main_default, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imgcopy_main_main_default, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imgcopy, &style_scrnfanlightselect_imgcopy_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->scrnFanLightselect_imgcopy, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->scrnFanLightselect_imgcopy,&_copy_29x29);
	lv_img_set_pivot(ui->scrnFanLightselect_imgcopy, 0,0);
	lv_img_set_angle(ui->scrnFanLightselect_imgcopy, 0);

	//Write codes scrnFanLightselect_imglight
	ui->scrnFanLightselect_imglight = lv_img_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_imglight, 264, 119);
	lv_obj_set_size(ui->scrnFanLightselect_imglight, 31, 29);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_imglight, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_imglight_main_main_default
	static lv_style_t style_scrnfanlightselect_imglight_main_main_default;
	if (style_scrnfanlightselect_imglight_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_imglight_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_imglight_main_main_default);
	lv_style_set_img_recolor(&style_scrnfanlightselect_imglight_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrnfanlightselect_imglight_main_main_default, 0);
	lv_style_set_img_opa(&style_scrnfanlightselect_imglight_main_main_default, 255);
	lv_obj_add_style(ui->scrnFanLightselect_imglight, &style_scrnfanlightselect_imglight_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->scrnFanLightselect_imglight, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->scrnFanLightselect_imglight,&_light_31x29);
	lv_img_set_pivot(ui->scrnFanLightselect_imglight, 0,0);
	lv_img_set_angle(ui->scrnFanLightselect_imglight, 0);

	//Write codes scrnFanLightselect_label_3
	ui->scrnFanLightselect_label_3 = lv_label_create(ui->scrnFanLightselect);
	lv_obj_set_pos(ui->scrnFanLightselect_label_3, 12, 24);
	lv_obj_set_size(ui->scrnFanLightselect_label_3, 456, 33);
	lv_obj_set_scrollbar_mode(ui->scrnFanLightselect_label_3, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrnFanLightselect_label_3, "Which you would like to monitor?");
	lv_label_set_long_mode(ui->scrnFanLightselect_label_3, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrnfanlightselect_label_3_main_main_default
	static lv_style_t style_scrnfanlightselect_label_3_main_main_default;
	if (style_scrnfanlightselect_label_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrnfanlightselect_label_3_main_main_default);
	else
		lv_style_init(&style_scrnfanlightselect_label_3_main_main_default);
	lv_style_set_radius(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_bg_color(&style_scrnfanlightselect_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_scrnfanlightselect_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_scrnfanlightselect_label_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_text_color(&style_scrnfanlightselect_label_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrnfanlightselect_label_3_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrnfanlightselect_label_3_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_text_align(&style_scrnfanlightselect_label_3_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_pad_right(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_pad_top(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrnfanlightselect_label_3_main_main_default, 0);
	lv_obj_add_style(ui->scrnFanLightselect_label_3, &style_scrnfanlightselect_label_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Init events for screen
	events_init_scrnFanLightselect(ui);
}