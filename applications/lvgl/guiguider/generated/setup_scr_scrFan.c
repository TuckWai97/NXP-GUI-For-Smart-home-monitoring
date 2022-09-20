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


void setup_scr_scrFan(lv_ui *ui){

	//Write codes scrFan
	ui->scrFan = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->scrFan, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_main_main_default
	static lv_style_t style_scrfan_main_main_default;
	if (style_scrfan_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_main_main_default);
	else
		lv_style_init(&style_scrfan_main_main_default);
	lv_style_set_bg_color(&style_scrfan_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_opa(&style_scrfan_main_main_default, 0);
	lv_obj_add_style(ui->scrFan, &style_scrfan_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_cont0
	ui->scrFan_cont0 = lv_obj_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_cont0, 0, 0);
	lv_obj_set_size(ui->scrFan_cont0, 480, 33);
	lv_obj_set_scrollbar_mode(ui->scrFan_cont0, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_cont0_main_main_default
	static lv_style_t style_scrfan_cont0_main_main_default;
	if (style_scrfan_cont0_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_cont0_main_main_default);
	else
		lv_style_init(&style_scrfan_cont0_main_main_default);
	lv_style_set_radius(&style_scrfan_cont0_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_cont0_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_color(&style_scrfan_cont0_main_main_default, lv_color_make(0x2f, 0x32, 0x43));
	lv_style_set_bg_grad_dir(&style_scrfan_cont0_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_cont0_main_main_default, 255);
	lv_style_set_border_color(&style_scrfan_cont0_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrfan_cont0_main_main_default, 0);
	lv_style_set_border_opa(&style_scrfan_cont0_main_main_default, 255);
	lv_style_set_pad_left(&style_scrfan_cont0_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_cont0_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_cont0_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_cont0_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_cont0, &style_scrfan_cont0_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_con2
	ui->scrFan_con2 = lv_obj_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_con2, 0, 15);
	lv_obj_set_size(ui->scrFan_con2, 480, 252);
	lv_obj_set_scrollbar_mode(ui->scrFan_con2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_con2_main_main_default
	static lv_style_t style_scrfan_con2_main_main_default;
	if (style_scrfan_con2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_con2_main_main_default);
	else
		lv_style_init(&style_scrfan_con2_main_main_default);
	lv_style_set_radius(&style_scrfan_con2_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_con2_main_main_default, lv_color_make(0xde, 0xde, 0xde));
	lv_style_set_bg_grad_color(&style_scrfan_con2_main_main_default, lv_color_make(0xde, 0xde, 0xde));
	lv_style_set_bg_grad_dir(&style_scrfan_con2_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_con2_main_main_default, 255);
	lv_style_set_border_color(&style_scrfan_con2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrfan_con2_main_main_default, 0);
	lv_style_set_border_opa(&style_scrfan_con2_main_main_default, 255);
	lv_style_set_pad_left(&style_scrfan_con2_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_con2_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_con2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_con2_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_con2, &style_scrfan_con2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_cont1
	ui->scrFan_cont1 = lv_obj_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_cont1, 40, 60);
	lv_obj_set_size(ui->scrFan_cont1, 400, 140);
	lv_obj_set_scrollbar_mode(ui->scrFan_cont1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_cont1_main_main_default
	static lv_style_t style_scrfan_cont1_main_main_default;
	if (style_scrfan_cont1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_cont1_main_main_default);
	else
		lv_style_init(&style_scrfan_cont1_main_main_default);
	lv_style_set_radius(&style_scrfan_cont1_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_cont1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_scrfan_cont1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_scrfan_cont1_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_cont1_main_main_default, 255);
	lv_style_set_border_color(&style_scrfan_cont1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_border_width(&style_scrfan_cont1_main_main_default, 0);
	lv_style_set_border_opa(&style_scrfan_cont1_main_main_default, 255);
	lv_style_set_pad_left(&style_scrfan_cont1_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_cont1_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_cont1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_cont1_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_cont1, &style_scrfan_cont1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_label4
	ui->scrFan_label4 = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_label4, 100, 13);
	lv_obj_set_size(ui->scrFan_label4, 281, 30);
	lv_obj_set_scrollbar_mode(ui->scrFan_label4, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_label4, "Fan condition");
	lv_label_set_long_mode(ui->scrFan_label4, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_label4_main_main_default
	static lv_style_t style_scrfan_label4_main_main_default;
	if (style_scrfan_label4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_label4_main_main_default);
	else
		lv_style_init(&style_scrfan_label4_main_main_default);
	lv_style_set_radius(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_label4_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_scrfan_label4_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_scrfan_label4_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_label4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrfan_label4_main_main_default, &lv_font_arial_16);
	lv_style_set_text_letter_space(&style_scrfan_label4_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_label4_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_label4_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_label4_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_label4, &style_scrfan_label4_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_labelusb
	ui->scrFan_labelusb = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_labelusb, 115, 160);
	lv_obj_set_size(ui->scrFan_labelusb, 74, 20);
	lv_obj_set_scrollbar_mode(ui->scrFan_labelusb, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_labelusb, "Room 1");
	lv_label_set_long_mode(ui->scrFan_labelusb, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_labelusb_main_main_default
	static lv_style_t style_scrfan_labelusb_main_main_default;
	if (style_scrfan_labelusb_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_labelusb_main_main_default);
	else
		lv_style_init(&style_scrfan_labelusb_main_main_default);
	lv_style_set_radius(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_labelusb_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_scrfan_labelusb_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_scrfan_labelusb_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_labelusb_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrfan_labelusb_main_main_default, &lv_font_arial_16);
	lv_style_set_text_letter_space(&style_scrfan_labelusb_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_labelusb_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_labelusb_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_labelusb_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_labelusb, &style_scrfan_labelusb_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_labelmobile
	ui->scrFan_labelmobile = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_labelmobile, 288, 160);
	lv_obj_set_size(ui->scrFan_labelmobile, 74, 20);
	lv_obj_set_scrollbar_mode(ui->scrFan_labelmobile, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_labelmobile, "Room 2");
	lv_label_set_long_mode(ui->scrFan_labelmobile, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_labelmobile_main_main_default
	static lv_style_t style_scrfan_labelmobile_main_main_default;
	if (style_scrfan_labelmobile_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_labelmobile_main_main_default);
	else
		lv_style_init(&style_scrfan_labelmobile_main_main_default);
	lv_style_set_radius(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_labelmobile_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_color(&style_scrfan_labelmobile_main_main_default, lv_color_make(0x4a, 0xb2, 0x41));
	lv_style_set_bg_grad_dir(&style_scrfan_labelmobile_main_main_default, LV_GRAD_DIR_VER);
	lv_style_set_bg_opa(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_labelmobile_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrfan_labelmobile_main_main_default, &lv_font_arial_16);
	lv_style_set_text_letter_space(&style_scrfan_labelmobile_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_labelmobile_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_labelmobile_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_labelmobile_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_labelmobile, &style_scrfan_labelmobile_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_imgbtn_1
	ui->scrFan_imgbtn_1 = lv_imgbtn_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_imgbtn_1, 34, 0);
	lv_obj_set_size(ui->scrFan_imgbtn_1, 30, 26);
	lv_obj_set_scrollbar_mode(ui->scrFan_imgbtn_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_imgbtn_1_main_main_default
	static lv_style_t style_scrfan_imgbtn_1_main_main_default;
	if (style_scrfan_imgbtn_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_imgbtn_1_main_main_default);
	else
		lv_style_init(&style_scrfan_imgbtn_1_main_main_default);
	lv_style_set_text_color(&style_scrfan_imgbtn_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_align(&style_scrfan_imgbtn_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrfan_imgbtn_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_scrfan_imgbtn_1_main_main_default, 0);
	lv_style_set_img_opa(&style_scrfan_imgbtn_1_main_main_default, 255);
	lv_obj_add_style(ui->scrFan_imgbtn_1, &style_scrfan_imgbtn_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_PRESSED for style_scrfan_imgbtn_1_main_main_pressed
	static lv_style_t style_scrfan_imgbtn_1_main_main_pressed;
	if (style_scrfan_imgbtn_1_main_main_pressed.prop_cnt > 1)
		lv_style_reset(&style_scrfan_imgbtn_1_main_main_pressed);
	else
		lv_style_init(&style_scrfan_imgbtn_1_main_main_pressed);
	lv_style_set_text_color(&style_scrfan_imgbtn_1_main_main_pressed, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrfan_imgbtn_1_main_main_pressed, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrfan_imgbtn_1_main_main_pressed, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrfan_imgbtn_1_main_main_pressed, 0);
	lv_style_set_img_opa(&style_scrfan_imgbtn_1_main_main_pressed, 255);
	lv_obj_add_style(ui->scrFan_imgbtn_1, &style_scrfan_imgbtn_1_main_main_pressed, LV_PART_MAIN|LV_STATE_PRESSED);

	//Write style state: LV_STATE_CHECKED for style_scrfan_imgbtn_1_main_main_checked
	static lv_style_t style_scrfan_imgbtn_1_main_main_checked;
	if (style_scrfan_imgbtn_1_main_main_checked.prop_cnt > 1)
		lv_style_reset(&style_scrfan_imgbtn_1_main_main_checked);
	else
		lv_style_init(&style_scrfan_imgbtn_1_main_main_checked);
	lv_style_set_text_color(&style_scrfan_imgbtn_1_main_main_checked, lv_color_make(0xFF, 0x33, 0xFF));
	lv_style_set_text_align(&style_scrfan_imgbtn_1_main_main_checked, LV_TEXT_ALIGN_CENTER);
	lv_style_set_img_recolor(&style_scrfan_imgbtn_1_main_main_checked, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_img_recolor_opa(&style_scrfan_imgbtn_1_main_main_checked, 0);
	lv_style_set_img_opa(&style_scrfan_imgbtn_1_main_main_checked, 255);
	lv_obj_add_style(ui->scrFan_imgbtn_1, &style_scrfan_imgbtn_1_main_main_checked, LV_PART_MAIN|LV_STATE_CHECKED);
	lv_imgbtn_set_src(ui->scrFan_imgbtn_1, LV_IMGBTN_STATE_RELEASED, NULL, &_home_alpha_30x26, NULL);
	lv_imgbtn_set_src(ui->scrFan_imgbtn_1, LV_IMGBTN_STATE_PRESSED, NULL, &_home_alpha_30x26, NULL);
	lv_obj_add_flag(ui->scrFan_imgbtn_1, LV_OBJ_FLAG_CHECKABLE);

	//Write codes scrFan_ddlist_1
	ui->scrFan_ddlist_1 = lv_dropdown_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_ddlist_1, 175, 29);
	lv_obj_set_size(ui->scrFan_ddlist_1, 130, 30);
	lv_obj_set_scrollbar_mode(ui->scrFan_ddlist_1, LV_SCROLLBAR_MODE_OFF);
	lv_dropdown_set_options(ui->scrFan_ddlist_1, "Room 1\nRoom 2");

	//Write style state: LV_STATE_DEFAULT for style_scrfan_ddlist_1_main_main_default
	static lv_style_t style_scrfan_ddlist_1_main_main_default;
	if (style_scrfan_ddlist_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_ddlist_1_main_main_default);
	else
		lv_style_init(&style_scrfan_ddlist_1_main_main_default);
	lv_style_set_radius(&style_scrfan_ddlist_1_main_main_default, 3);
	lv_style_set_bg_color(&style_scrfan_ddlist_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_scrfan_ddlist_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_scrfan_ddlist_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_ddlist_1_main_main_default, 255);
	lv_style_set_border_color(&style_scrfan_ddlist_1_main_main_default, lv_color_make(0xe1, 0xe6, 0xee));
	lv_style_set_border_width(&style_scrfan_ddlist_1_main_main_default, 1);
	lv_style_set_border_opa(&style_scrfan_ddlist_1_main_main_default, 255);
	lv_style_set_text_color(&style_scrfan_ddlist_1_main_main_default, lv_color_make(0x0D, 0x30, 0x55));
	lv_style_set_text_font(&style_scrfan_ddlist_1_main_main_default, &lv_font_simsun_12);
	lv_style_set_pad_left(&style_scrfan_ddlist_1_main_main_default, 6);
	lv_style_set_pad_right(&style_scrfan_ddlist_1_main_main_default, 6);
	lv_style_set_pad_top(&style_scrfan_ddlist_1_main_main_default, 8);
	lv_obj_add_style(ui->scrFan_ddlist_1, &style_scrfan_ddlist_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_CHECKED for style_scrfan_ddlist_1_extra_list_selected_checked
	static lv_style_t style_scrfan_ddlist_1_extra_list_selected_checked;
	if (style_scrfan_ddlist_1_extra_list_selected_checked.prop_cnt > 1)
		lv_style_reset(&style_scrfan_ddlist_1_extra_list_selected_checked);
	else
		lv_style_init(&style_scrfan_ddlist_1_extra_list_selected_checked);
	lv_style_set_radius(&style_scrfan_ddlist_1_extra_list_selected_checked, 3);
	lv_style_set_bg_color(&style_scrfan_ddlist_1_extra_list_selected_checked, lv_color_make(0x00, 0xa1, 0xb5));
	lv_style_set_bg_grad_color(&style_scrfan_ddlist_1_extra_list_selected_checked, lv_color_make(0x00, 0xa1, 0xb5));
	lv_style_set_bg_grad_dir(&style_scrfan_ddlist_1_extra_list_selected_checked, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_ddlist_1_extra_list_selected_checked, 255);
	lv_style_set_border_color(&style_scrfan_ddlist_1_extra_list_selected_checked, lv_color_make(0xe1, 0xe6, 0xee));
	lv_style_set_border_width(&style_scrfan_ddlist_1_extra_list_selected_checked, 1);
	lv_style_set_border_opa(&style_scrfan_ddlist_1_extra_list_selected_checked, 255);
	lv_style_set_text_color(&style_scrfan_ddlist_1_extra_list_selected_checked, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_text_font(&style_scrfan_ddlist_1_extra_list_selected_checked, &lv_font_simsun_12);
	lv_style_set_pad_left(&style_scrfan_ddlist_1_extra_list_selected_checked, 6);
	lv_style_set_pad_right(&style_scrfan_ddlist_1_extra_list_selected_checked, 6);
	lv_style_set_pad_top(&style_scrfan_ddlist_1_extra_list_selected_checked, 6);
	lv_style_set_pad_bottom(&style_scrfan_ddlist_1_extra_list_selected_checked, 6);
	lv_obj_add_style(lv_dropdown_get_list(ui->scrFan_ddlist_1), &style_scrfan_ddlist_1_extra_list_selected_checked, LV_PART_SELECTED|LV_STATE_CHECKED);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_ddlist_1_extra_list_main_default
	static lv_style_t style_scrfan_ddlist_1_extra_list_main_default;
	if (style_scrfan_ddlist_1_extra_list_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_ddlist_1_extra_list_main_default);
	else
		lv_style_init(&style_scrfan_ddlist_1_extra_list_main_default);
	lv_style_set_radius(&style_scrfan_ddlist_1_extra_list_main_default, 3);
	lv_style_set_bg_color(&style_scrfan_ddlist_1_extra_list_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_scrfan_ddlist_1_extra_list_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_scrfan_ddlist_1_extra_list_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_ddlist_1_extra_list_main_default, 255);
	lv_style_set_border_color(&style_scrfan_ddlist_1_extra_list_main_default, lv_color_make(0xe1, 0xe6, 0xee));
	lv_style_set_border_width(&style_scrfan_ddlist_1_extra_list_main_default, 1);
	lv_style_set_border_opa(&style_scrfan_ddlist_1_extra_list_main_default, 255);
	lv_style_set_text_color(&style_scrfan_ddlist_1_extra_list_main_default, lv_color_make(0x0D, 0x30, 0x55));
	lv_style_set_text_font(&style_scrfan_ddlist_1_extra_list_main_default, &lv_font_simsun_12);
	lv_style_set_pad_left(&style_scrfan_ddlist_1_extra_list_main_default, 6);
	lv_style_set_pad_right(&style_scrfan_ddlist_1_extra_list_main_default, 6);
	lv_style_set_pad_top(&style_scrfan_ddlist_1_extra_list_main_default, 6);
	lv_style_set_pad_bottom(&style_scrfan_ddlist_1_extra_list_main_default, 6);
	lv_style_set_max_height(&style_scrfan_ddlist_1_extra_list_main_default, 90);
	lv_obj_add_style(lv_dropdown_get_list(ui->scrFan_ddlist_1), &style_scrfan_ddlist_1_extra_list_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_ddlist_1_extra_list_scrollbar_default
	static lv_style_t style_scrfan_ddlist_1_extra_list_scrollbar_default;
	if (style_scrfan_ddlist_1_extra_list_scrollbar_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_ddlist_1_extra_list_scrollbar_default);
	else
		lv_style_init(&style_scrfan_ddlist_1_extra_list_scrollbar_default);
	lv_style_set_radius(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 3);
	lv_style_set_bg_color(&style_scrfan_ddlist_1_extra_list_scrollbar_default, lv_color_make(0x00, 0xff, 0x00));
	lv_style_set_bg_opa(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 255);
	lv_style_set_pad_left(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 6);
	lv_style_set_pad_right(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 6);
	lv_style_set_pad_top(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 6);
	lv_style_set_pad_bottom(&style_scrfan_ddlist_1_extra_list_scrollbar_default, 6);
	lv_obj_add_style(lv_dropdown_get_list(ui->scrFan_ddlist_1), &style_scrfan_ddlist_1_extra_list_scrollbar_default, LV_PART_SCROLLBAR|LV_STATE_DEFAULT);

	//Write codes scrFan_label_1
	ui->scrFan_label_1 = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_label_1, 313, 125);
	lv_obj_set_size(ui->scrFan_label_1, 88, 55);
	lv_obj_set_scrollbar_mode(ui->scrFan_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_label_1, "ON");
	lv_label_set_long_mode(ui->scrFan_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_label_1_main_main_default
	static lv_style_t style_scrfan_label_1_main_main_default;
	if (style_scrfan_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_label_1_main_main_default);
	else
		lv_style_init(&style_scrfan_label_1_main_main_default);
	lv_style_set_radius(&style_scrfan_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_scrfan_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_scrfan_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_label_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_scrfan_label_1_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrfan_label_1_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_label_1_main_main_default, 20);
	lv_style_set_pad_bottom(&style_scrfan_label_1_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_label_1, &style_scrfan_label_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_label_2
	ui->scrFan_label_2 = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_label_2, 299, 119);
	lv_obj_set_size(ui->scrFan_label_2, 117, 34);
	lv_obj_set_scrollbar_mode(ui->scrFan_label_2, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_label_2, "Fan condition");
	lv_label_set_long_mode(ui->scrFan_label_2, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_label_2_main_main_default
	static lv_style_t style_scrfan_label_2_main_main_default;
	if (style_scrfan_label_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_label_2_main_main_default);
	else
		lv_style_init(&style_scrfan_label_2_main_main_default);
	lv_style_set_radius(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_scrfan_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_scrfan_label_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_label_2_main_main_default, lv_color_make(0x7e, 0x07, 0x07));
	lv_style_set_text_font(&style_scrfan_label_2_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrfan_label_2_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_label_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_label_2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_label_2_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_label_2, &style_scrfan_label_2_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Write codes scrFan_chart_1
	ui->scrFan_chart_1 = lv_chart_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_chart_1, 73, 70);
	lv_obj_set_size(ui->scrFan_chart_1, 158, 92);
	lv_obj_set_scrollbar_mode(ui->scrFan_chart_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_chart_1_main_main_default
	static lv_style_t style_scrfan_chart_1_main_main_default;
	if (style_scrfan_chart_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_chart_1_main_main_default);
	else
		lv_style_init(&style_scrfan_chart_1_main_main_default);
	lv_style_set_radius(&style_scrfan_chart_1_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_chart_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_scrfan_chart_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_scrfan_chart_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_chart_1_main_main_default, 255);
	lv_style_set_border_color(&style_scrfan_chart_1_main_main_default, lv_color_make(0xe8, 0xe8, 0xe8));
	lv_style_set_border_width(&style_scrfan_chart_1_main_main_default, 1);
	lv_style_set_border_opa(&style_scrfan_chart_1_main_main_default, 255);
	lv_style_set_line_color(&style_scrfan_chart_1_main_main_default, lv_color_make(0xe8, 0xe8, 0xe8));
	lv_style_set_line_width(&style_scrfan_chart_1_main_main_default, 2);
	lv_style_set_line_opa(&style_scrfan_chart_1_main_main_default, 255);
	lv_obj_add_style(ui->scrFan_chart_1, &style_scrfan_chart_1_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);
	lv_chart_set_type(ui->scrFan_chart_1, LV_CHART_TYPE_LINE);
	lv_chart_set_range(ui->scrFan_chart_1,LV_CHART_AXIS_PRIMARY_Y, 0, 100);
	lv_chart_set_div_line_count(ui->scrFan_chart_1, 3, 5);
	lv_chart_set_point_count(ui->scrFan_chart_1, 5);
	lv_chart_series_t * scrFan_chart_1_0 = lv_chart_add_series(ui->scrFan_chart_1, lv_color_make(0x00, 0x00, 0x00), LV_CHART_AXIS_PRIMARY_Y);
	lv_chart_set_next_value(ui->scrFan_chart_1, scrFan_chart_1_0, 1);
	lv_chart_set_next_value(ui->scrFan_chart_1, scrFan_chart_1_0, 20);
	lv_chart_set_next_value(ui->scrFan_chart_1, scrFan_chart_1_0, 30);
	lv_chart_set_next_value(ui->scrFan_chart_1, scrFan_chart_1_0, 40);
	lv_chart_set_next_value(ui->scrFan_chart_1, scrFan_chart_1_0, 5);

	//Write codes scrFan_label_5
	ui->scrFan_label_5 = lv_label_create(ui->scrFan);
	lv_obj_set_pos(ui->scrFan_label_5, 68, 180);
	lv_obj_set_size(ui->scrFan_label_5, 163, 32);
	lv_obj_set_scrollbar_mode(ui->scrFan_label_5, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->scrFan_label_5, "Time ON: 5 hours");
	lv_label_set_long_mode(ui->scrFan_label_5, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_scrfan_label_5_main_main_default
	static lv_style_t style_scrfan_label_5_main_main_default;
	if (style_scrfan_label_5_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_scrfan_label_5_main_main_default);
	else
		lv_style_init(&style_scrfan_label_5_main_main_default);
	lv_style_set_radius(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_bg_color(&style_scrfan_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_scrfan_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_scrfan_label_5_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_text_color(&style_scrfan_label_5_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_scrfan_label_5_main_main_default, &lv_font_arial_12);
	lv_style_set_text_letter_space(&style_scrfan_label_5_main_main_default, 2);
	lv_style_set_text_line_space(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_text_align(&style_scrfan_label_5_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_pad_right(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_pad_top(&style_scrfan_label_5_main_main_default, 0);
	lv_style_set_pad_bottom(&style_scrfan_label_5_main_main_default, 0);
	lv_obj_add_style(ui->scrFan_label_5, &style_scrfan_label_5_main_main_default, LV_PART_MAIN|LV_STATE_DEFAULT);

	//Init events for screen
	events_init_scrFan(ui);
}