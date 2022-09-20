/*
 * Copyright 2022 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"


void init_scr_del_flag(lv_ui *ui){
	ui->home_screen_del = true;
	ui->scrTemp_del = true;
	ui->scrHumid_del = true;
	ui->scrnFanLightselect_del = true;
	ui->scrFan_del = true;
	ui->scrnLight_del = true;
}

void setup_ui(lv_ui *ui){
	init_scr_del_flag(ui);
	setup_scr_home_screen(ui);
	lv_scr_load(ui->home_screen);
}
