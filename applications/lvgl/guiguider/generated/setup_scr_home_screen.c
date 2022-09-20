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


void setup_scr_home_screen(lv_ui *ui){

	//Write codes home_screen
	ui->home_screen = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->home_screen, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_main_main_default
	static lv_style_t style_home_screen_main_main_default;
	if (style_home_screen_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_main_main_default);
	else
		lv_style_init(&style_home_screen_main_main_default);
	lv_style_set_bg_color(&style_home_screen_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_home_screen_main_main_default, 0);
	lv_obj_add_style(ui->home_screen, &style_home_screen_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_cont1
	ui->home_screen_cont1 = lv_obj_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_cont1, 0, 0);
	lv_obj_set_size(ui->home_screen_cont1, 480, 95);
	lv_obj_set_scrollbar_mode(ui->home_screen_cont1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_cont1_main_main_default
	static lv_style_t style_home_screen_cont1_main_main_default;
	if (style_home_screen_cont1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_cont1_main_main_default);
	else
		lv_style_init(&style_home_screen_cont1_main_main_default);
	lv_style_set_radius(&style_home_screen_cont1_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_cont1_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_color(&style_home_screen_cont1_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_dir(&style_home_screen_cont1_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_cont1_main_main_default, 255);
	lv_style_set_border_color(&style_home_screen_cont1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_home_screen_cont1_main_main_default, 0);
	lv_style_set_border_opa(&style_home_screen_cont1_main_main_default, 255);
	lv_style_set_pad_left(&style_home_screen_cont1_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_cont1_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_cont1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_cont1_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_cont1, &style_home_screen_cont1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_whitebg
	ui->home_screen_whitebg = lv_obj_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_whitebg, 0, 96);
	lv_obj_set_size(ui->home_screen_whitebg, 480, 177);
	lv_obj_set_scrollbar_mode(ui->home_screen_whitebg, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_whitebg_main_main_default
	static lv_style_t style_home_screen_whitebg_main_main_default;
	if (style_home_screen_whitebg_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_whitebg_main_main_default);
	else
		lv_style_init(&style_home_screen_whitebg_main_main_default);
	lv_style_set_radius(&style_home_screen_whitebg_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_whitebg_main_main_default, lv_color_make(0xd6, 0xdc, 0xd6));
	lv_style_set_bg_grad_color(&style_home_screen_whitebg_main_main_default, lv_color_make(0xd9, 0xd9, 0xd9));
	lv_style_set_bg_grad_dir(&style_home_screen_whitebg_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_whitebg_main_main_default, 255);
	lv_style_set_border_color(&style_home_screen_whitebg_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_home_screen_whitebg_main_main_default, 0);
	lv_style_set_border_opa(&style_home_screen_whitebg_main_main_default, 255);
	lv_style_set_pad_left(&style_home_screen_whitebg_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_whitebg_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_whitebg_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_whitebg_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_whitebg, &style_home_screen_whitebg_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_cont2
	ui->home_screen_cont2 = lv_obj_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_cont2, 40, 80);
	lv_obj_set_size(ui->home_screen_cont2, 380, 120);
	lv_obj_set_scrollbar_mode(ui->home_screen_cont2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_cont2_main_main_default
	static lv_style_t style_home_screen_cont2_main_main_default;
	if (style_home_screen_cont2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_cont2_main_main_default);
	else
		lv_style_init(&style_home_screen_cont2_main_main_default);
	lv_style_set_radius(&style_home_screen_cont2_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_cont2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_home_screen_cont2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_home_screen_cont2_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_cont2_main_main_default, 255);
	lv_style_set_border_color(&style_home_screen_cont2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_home_screen_cont2_main_main_default, 0);
	lv_style_set_border_opa(&style_home_screen_cont2_main_main_default, 255);
	lv_style_set_pad_left(&style_home_screen_cont2_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_cont2_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_cont2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_cont2_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_cont2, &style_home_screen_cont2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_imgbtn_surve
	ui->home_screen_imgbtn_surve = lv_imgbtn_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgbtn_surve, 320, 86);
	lv_obj_set_size(ui->home_screen_imgbtn_surve, 96, 100);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgbtn_surve, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgbtn_surve_main_main_default
	static lv_style_t style_home_screen_imgbtn_surve_main_main_default;
	if (style_home_screen_imgbtn_surve_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_surve_main_main_default);
	else
		lv_style_init(&style_home_screen_imgbtn_surve_main_main_default);
	lv_style_set_text_color(&style_home_screen_imgbtn_surve_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_home_screen_imgbtn_surve_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_surve_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_surve_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_surve_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_surve, &style_home_screen_imgbtn_surve_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_home_screen_imgbtn_surve_main_main_pressed
	static lv_style_t style_home_screen_imgbtn_surve_main_main_pressed;
	if (style_home_screen_imgbtn_surve_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_surve_main_main_pressed);
	else
		lv_style_init(&style_home_screen_imgbtn_surve_main_main_pressed);
	lv_style_set_text_color(&style_home_screen_imgbtn_surve_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_surve_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_surve_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_surve_main_main_pressed, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_surve_main_main_pressed, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_surve, &style_home_screen_imgbtn_surve_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_home_screen_imgbtn_surve_main_main_checked
	static lv_style_t style_home_screen_imgbtn_surve_main_main_checked;
	if (style_home_screen_imgbtn_surve_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_surve_main_main_checked);
	else
		lv_style_init(&style_home_screen_imgbtn_surve_main_main_checked);
	lv_style_set_text_color(&style_home_screen_imgbtn_surve_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_surve_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_surve_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_surve_main_main_checked, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_surve_main_main_checked, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_surve, &style_home_screen_imgbtn_surve_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_surve, LV_IMGBTN_STATE_RELEASED, NULL, &_btn4_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_surve, LV_IMGBTN_STATE_PRESSED, NULL, &_btn4_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_surve, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn4_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_surve, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn4_alpha_96x100, NULL);

	//Write codes home_screen_imgbtn_humid
	ui->home_screen_imgbtn_humid = lv_imgbtn_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgbtn_humid, 139, 87);
	lv_obj_set_size(ui->home_screen_imgbtn_humid, 96, 100);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgbtn_humid, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgbtn_humid_main_main_default
	static lv_style_t style_home_screen_imgbtn_humid_main_main_default;
	if (style_home_screen_imgbtn_humid_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_humid_main_main_default);
	else
		lv_style_init(&style_home_screen_imgbtn_humid_main_main_default);
	lv_style_set_text_color(&style_home_screen_imgbtn_humid_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_home_screen_imgbtn_humid_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_humid_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_humid_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_humid_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_humid, &style_home_screen_imgbtn_humid_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_home_screen_imgbtn_humid_main_main_pressed
	static lv_style_t style_home_screen_imgbtn_humid_main_main_pressed;
	if (style_home_screen_imgbtn_humid_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_humid_main_main_pressed);
	else
		lv_style_init(&style_home_screen_imgbtn_humid_main_main_pressed);
	lv_style_set_text_color(&style_home_screen_imgbtn_humid_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_humid_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_humid_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_humid_main_main_pressed, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_humid_main_main_pressed, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_humid, &style_home_screen_imgbtn_humid_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_home_screen_imgbtn_humid_main_main_checked
	static lv_style_t style_home_screen_imgbtn_humid_main_main_checked;
	if (style_home_screen_imgbtn_humid_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_humid_main_main_checked);
	else
		lv_style_init(&style_home_screen_imgbtn_humid_main_main_checked);
	lv_style_set_text_color(&style_home_screen_imgbtn_humid_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_humid_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_humid_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_humid_main_main_checked, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_humid_main_main_checked, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_humid, &style_home_screen_imgbtn_humid_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_humid, LV_IMGBTN_STATE_RELEASED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_humid, LV_IMGBTN_STATE_PRESSED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_humid, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn2_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_humid, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn2_alpha_96x100, NULL);

	//Write codes home_screen_imgbtn_fanlght
	ui->home_screen_imgbtn_fanlght = lv_imgbtn_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgbtn_fanlght, 230, 86);
	lv_obj_set_size(ui->home_screen_imgbtn_fanlght, 96, 100);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgbtn_fanlght, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgbtn_fanlght_main_main_default
	static lv_style_t style_home_screen_imgbtn_fanlght_main_main_default;
	if (style_home_screen_imgbtn_fanlght_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_fanlght_main_main_default);
	else
		lv_style_init(&style_home_screen_imgbtn_fanlght_main_main_default);
	lv_style_set_text_color(&style_home_screen_imgbtn_fanlght_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_home_screen_imgbtn_fanlght_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_fanlght_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_fanlght_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_fanlght_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_fanlght, &style_home_screen_imgbtn_fanlght_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_home_screen_imgbtn_fanlght_main_main_pressed
	static lv_style_t style_home_screen_imgbtn_fanlght_main_main_pressed;
	if (style_home_screen_imgbtn_fanlght_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_fanlght_main_main_pressed);
	else
		lv_style_init(&style_home_screen_imgbtn_fanlght_main_main_pressed);
	lv_style_set_text_color(&style_home_screen_imgbtn_fanlght_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_fanlght_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_fanlght_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_fanlght_main_main_pressed, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_fanlght_main_main_pressed, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_fanlght, &style_home_screen_imgbtn_fanlght_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_home_screen_imgbtn_fanlght_main_main_checked
	static lv_style_t style_home_screen_imgbtn_fanlght_main_main_checked;
	if (style_home_screen_imgbtn_fanlght_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgbtn_fanlght_main_main_checked);
	else
		lv_style_init(&style_home_screen_imgbtn_fanlght_main_main_checked);
	lv_style_set_text_color(&style_home_screen_imgbtn_fanlght_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_imgbtn_fanlght_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_imgbtn_fanlght_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_imgbtn_fanlght_main_main_checked, 0);
	lv_style_set_img_opa(&style_home_screen_imgbtn_fanlght_main_main_checked, 255);
	lv_obj_add_style(ui->home_screen_imgbtn_fanlght, &style_home_screen_imgbtn_fanlght_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_fanlght, LV_IMGBTN_STATE_RELEASED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_fanlght, LV_IMGBTN_STATE_PRESSED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_fanlght, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn3_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_imgbtn_fanlght, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn3_alpha_96x100, NULL);

	//Write codes home_screen_img_fan
	ui->home_screen_img_fan = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_img_fan, 249, 107);
	lv_obj_set_size(ui->home_screen_img_fan, 31, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_img_fan, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_img_fan_main_main_default
	static lv_style_t style_home_screen_img_fan_main_main_default;
	if (style_home_screen_img_fan_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_img_fan_main_main_default);
	else
		lv_style_init(&style_home_screen_img_fan_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_img_fan_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_img_fan_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_img_fan_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_img_fan, &style_home_screen_img_fan_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_img_fan, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_img_fan,&_fan_31x29);
	lv_img_set_pivot(ui->home_screen_img_fan, 0,0);
	lv_img_set_angle(ui->home_screen_img_fan, 0);

	//Write codes home_screen_labelhumid
	ui->home_screen_labelhumid = lv_label_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_labelhumid, 153, 148);
	lv_obj_set_size(ui->home_screen_labelhumid, 67, 20);
	lv_obj_set_scrollbar_mode(ui->home_screen_labelhumid, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->home_screen_labelhumid, "Humidity");
	lv_label_set_long_mode(ui->home_screen_labelhumid, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_labelhumid_main_main_default
	static lv_style_t style_home_screen_labelhumid_main_main_default;
	if (style_home_screen_labelhumid_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_labelhumid_main_main_default);
	else
		lv_style_init(&style_home_screen_labelhumid_main_main_default);
	lv_style_set_radius(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_labelhumid_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_home_screen_labelhumid_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_home_screen_labelhumid_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_text_color(&style_home_screen_labelhumid_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_home_screen_labelhumid_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_home_screen_labelhumid_main_main_default, 1);
	lv_style_set_text_line_space(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_text_align(&style_home_screen_labelhumid_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_labelhumid_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_labelhumid_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_labelhumid, &style_home_screen_labelhumid_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_labelfanlight
	ui->home_screen_labelfanlight = lv_label_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_labelfanlight, 242, 138);
	lv_obj_set_size(ui->home_screen_labelfanlight, 75, 36);
	lv_obj_set_scrollbar_mode(ui->home_screen_labelfanlight, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->home_screen_labelfanlight, "Fan & Light operation time");
	lv_label_set_long_mode(ui->home_screen_labelfanlight, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_labelfanlight_main_main_default
	static lv_style_t style_home_screen_labelfanlight_main_main_default;
	if (style_home_screen_labelfanlight_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_labelfanlight_main_main_default);
	else
		lv_style_init(&style_home_screen_labelfanlight_main_main_default);
	lv_style_set_radius(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_labelfanlight_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_home_screen_labelfanlight_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_home_screen_labelfanlight_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_text_color(&style_home_screen_labelfanlight_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_home_screen_labelfanlight_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_home_screen_labelfanlight_main_main_default, 1);
	lv_style_set_text_line_space(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_text_align(&style_home_screen_labelfanlight_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_labelfanlight_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_labelfanlight, &style_home_screen_labelfanlight_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_labelsurvel
	ui->home_screen_labelsurvel = lv_label_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_labelsurvel, 326, 148);
	lv_obj_set_size(ui->home_screen_labelsurvel, 84, 21);
	lv_obj_set_scrollbar_mode(ui->home_screen_labelsurvel, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->home_screen_labelsurvel, "Surveillance");
	lv_label_set_long_mode(ui->home_screen_labelsurvel, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_labelsurvel_main_main_default
	static lv_style_t style_home_screen_labelsurvel_main_main_default;
	if (style_home_screen_labelsurvel_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_labelsurvel_main_main_default);
	else
		lv_style_init(&style_home_screen_labelsurvel_main_main_default);
	lv_style_set_radius(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_labelsurvel_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_home_screen_labelsurvel_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_home_screen_labelsurvel_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_text_color(&style_home_screen_labelsurvel_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_home_screen_labelsurvel_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_home_screen_labelsurvel_main_main_default, 1);
	lv_style_set_text_line_space(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_text_align(&style_home_screen_labelsurvel_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_labelsurvel_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_labelsurvel, &style_home_screen_labelsurvel_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_imgcopy
	ui->home_screen_imgcopy = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgcopy, 90, 108);
	lv_obj_set_size(ui->home_screen_imgcopy, 29, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgcopy, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgcopy_main_main_default
	static lv_style_t style_home_screen_imgcopy_main_main_default;
	if (style_home_screen_imgcopy_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgcopy_main_main_default);
	else
		lv_style_init(&style_home_screen_imgcopy_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_imgcopy_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgcopy_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgcopy_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgcopy, &style_home_screen_imgcopy_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_imgcopy, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_imgcopy,&_copy_29x29);
	lv_img_set_pivot(ui->home_screen_imgcopy, 0,0);
	lv_img_set_angle(ui->home_screen_imgcopy, 0);

	//Write codes home_screen_imgscan
	ui->home_screen_imgscan = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgscan, 183, 108);
	lv_obj_set_size(ui->home_screen_imgscan, 29, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgscan, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgscan_main_main_default
	static lv_style_t style_home_screen_imgscan_main_main_default;
	if (style_home_screen_imgscan_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgscan_main_main_default);
	else
		lv_style_init(&style_home_screen_imgscan_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_imgscan_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgscan_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgscan_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgscan, &style_home_screen_imgscan_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_imgscan, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_imgscan,&_humidity_29x29);
	lv_img_set_pivot(ui->home_screen_imgscan, 0,0);
	lv_img_set_angle(ui->home_screen_imgscan, -10);

	//Write codes home_screen_imglight
	ui->home_screen_imglight = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imglight, 280, 107);
	lv_obj_set_size(ui->home_screen_imglight, 31, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_imglight, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imglight_main_main_default
	static lv_style_t style_home_screen_imglight_main_main_default;
	if (style_home_screen_imglight_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imglight_main_main_default);
	else
		lv_style_init(&style_home_screen_imglight_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_imglight_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imglight_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imglight_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imglight, &style_home_screen_imglight_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_imglight, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_imglight,&_light_31x29);
	lv_img_set_pivot(ui->home_screen_imglight, 0,0);
	lv_img_set_angle(ui->home_screen_imglight, 0);

	//Write codes home_screen_imgsurve
	ui->home_screen_imgsurve = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_imgsurve, 360, 108);
	lv_obj_set_size(ui->home_screen_imgsurve, 29, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_imgsurve, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_imgsurve_main_main_default
	static lv_style_t style_home_screen_imgsurve_main_main_default;
	if (style_home_screen_imgsurve_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_imgsurve_main_main_default);
	else
		lv_style_init(&style_home_screen_imgsurve_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_imgsurve_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_imgsurve_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_imgsurve_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_imgsurve, &style_home_screen_imgsurve_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_imgsurve, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_imgsurve,&_cctv_29x29);
	lv_img_set_pivot(ui->home_screen_imgsurve, 0,0);
	lv_img_set_angle(ui->home_screen_imgsurve, 0);

	//Write codes home_screen_temp_but
	ui->home_screen_temp_but = lv_imgbtn_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_temp_but, 51, 87);
	lv_obj_set_size(ui->home_screen_temp_but, 96, 100);
	lv_obj_set_scrollbar_mode(ui->home_screen_temp_but, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_temp_but_main_main_default
	static lv_style_t style_home_screen_temp_but_main_main_default;
	if (style_home_screen_temp_but_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_temp_but_main_main_default);
	else
		lv_style_init(&style_home_screen_temp_but_main_main_default);
	lv_style_set_text_color(&style_home_screen_temp_but_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_home_screen_temp_but_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_temp_but_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_temp_but_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_temp_but_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_temp_but, &style_home_screen_temp_but_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_home_screen_temp_but_main_main_pressed
	static lv_style_t style_home_screen_temp_but_main_main_pressed;
	if (style_home_screen_temp_but_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_home_screen_temp_but_main_main_pressed);
	else
		lv_style_init(&style_home_screen_temp_but_main_main_pressed);
	lv_style_set_text_color(&style_home_screen_temp_but_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_temp_but_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_temp_but_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_temp_but_main_main_pressed, 0);
	lv_style_set_img_opa(&style_home_screen_temp_but_main_main_pressed, 255);
	lv_obj_add_style(ui->home_screen_temp_but, &style_home_screen_temp_but_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_home_screen_temp_but_main_main_checked
	static lv_style_t style_home_screen_temp_but_main_main_checked;
	if (style_home_screen_temp_but_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_home_screen_temp_but_main_main_checked);
	else
		lv_style_init(&style_home_screen_temp_but_main_main_checked);
	lv_style_set_text_color(&style_home_screen_temp_but_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_home_screen_temp_but_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_home_screen_temp_but_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_home_screen_temp_but_main_main_checked, 0);
	lv_style_set_img_opa(&style_home_screen_temp_but_main_main_checked, 255);
	lv_obj_add_style(ui->home_screen_temp_but, &style_home_screen_temp_but_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->home_screen_temp_but, LV_IMGBTN_STATE_RELEASED, NULL, &_btn_bg_1_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_temp_but, LV_IMGBTN_STATE_PRESSED, NULL, &_btn_bg_1_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_temp_but, LV_IMGBTN_STATE_CHECKED_RELEASED, NULL, &_btn_bg_1_alpha_96x100, NULL);
	lv_imgbtn_set_src(ui->home_screen_temp_but, LV_IMGBTN_STATE_CHECKED_PRESSED, NULL, &_btn_bg_1_alpha_96x100, NULL);

	//Write codes home_screen_label_2
	ui->home_screen_label_2 = lv_label_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_label_2, 60, 143);
	lv_obj_set_size(ui->home_screen_label_2, 79, 13);
	lv_obj_set_scrollbar_mode(ui->home_screen_label_2, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->home_screen_label_2, "Temperature");
	lv_label_set_long_mode(ui->home_screen_label_2, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_label_2_main_main_default
	static lv_style_t style_home_screen_label_2_main_main_default;
	if (style_home_screen_label_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_label_2_main_main_default);
	else
		lv_style_init(&style_home_screen_label_2_main_main_default);
	lv_style_set_radius(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_home_screen_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_home_screen_label_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_text_color(&style_home_screen_label_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_home_screen_label_2_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_home_screen_label_2_main_main_default, 1);
	lv_style_set_text_line_space(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_text_align(&style_home_screen_label_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_label_2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_label_2_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_label_2, &style_home_screen_label_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes home_screen_img_1
	ui->home_screen_img_1 = lv_img_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_img_1, 97, 103);
	lv_obj_set_size(ui->home_screen_img_1, 29, 29);
	lv_obj_set_scrollbar_mode(ui->home_screen_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_img_1_main_main_default
	static lv_style_t style_home_screen_img_1_main_main_default;
	if (style_home_screen_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_img_1_main_main_default);
	else
		lv_style_init(&style_home_screen_img_1_main_main_default);
	lv_style_set_img_recolor(&style_home_screen_img_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_home_screen_img_1_main_main_default, 0);
	lv_style_set_img_opa(&style_home_screen_img_1_main_main_default, 255);
	lv_obj_add_style(ui->home_screen_img_1, &style_home_screen_img_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->home_screen_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->home_screen_img_1,&_temperature_29x29);
	lv_img_set_pivot(ui->home_screen_img_1, 0,0);
	lv_img_set_angle(ui->home_screen_img_1, 0);

	//Write codes home_screen_label_3
	ui->home_screen_label_3 = lv_label_create(ui->home_screen);
	lv_obj_set_pos(ui->home_screen_label_3, 12, 24);
	lv_obj_set_size(ui->home_screen_label_3, 456, 33);
	lv_obj_set_scrollbar_mode(ui->home_screen_label_3, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->home_screen_label_3, "Hello welcome to smart home monitoring!");
	lv_label_set_long_mode(ui->home_screen_label_3, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_home_screen_label_3_main_main_default
	static lv_style_t style_home_screen_label_3_main_main_default;
	if (style_home_screen_label_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_home_screen_label_3_main_main_default);
	else
		lv_style_init(&style_home_screen_label_3_main_main_default);
	lv_style_set_radius(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_bg_color(&style_home_screen_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_home_screen_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_home_screen_label_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_text_color(&style_home_screen_label_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_home_screen_label_3_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_home_screen_label_3_main_main_default, 2);
	lv_style_set_text_line_space(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_text_align(&style_home_screen_label_3_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_pad_right(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_pad_top(&style_home_screen_label_3_main_main_default, 0);
	lv_style_set_pad_bottom(&style_home_screen_label_3_main_main_default, 0);
	lv_obj_add_style(ui->home_screen_label_3, &style_home_screen_label_3_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Init events for screen
	events_init_home_screen(ui);
}