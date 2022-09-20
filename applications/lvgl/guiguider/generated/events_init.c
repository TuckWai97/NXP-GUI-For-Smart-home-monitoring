/*
 * Copyright 2022 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "events_init.h"
#include <stdio.h>
#include "lvgl.h"

#include "custom.h"

void events_init(lv_ui *ui)
{
}

static void home_screen_imgbtn_surve_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_SETUP); 
		lv_demo_printer_anim_in_all(guider_ui.setup, 200);
	}
		break;
	default:
		break;
	}
}

static void home_screen_imgbtn_humid_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.scrHumid_del == true)
				setup_scr_scrHumid(&guider_ui);
			lv_scr_load_anim(guider_ui.scrHumid, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.home_screen_del = true;
	}
		break;
	default:
		break;
	}
}

static void home_screen_imgbtn_fanlght_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.scrnFanLightselect_del == true)
				setup_scr_scrnFanLightselect(&guider_ui);
			lv_scr_load_anim(guider_ui.scrnFanLightselect, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.home_screen_del = true;
	}
		break;
	default:
		break;
	}
}

static void home_screen_imgcopy_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_LOADER);
		add_loader(load_copy);
	}
		break;
	default:
		break;
	}
}

static void home_screen_imgscan_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_LOADER);
		add_loader(load_scan);
	}
		break;
	default:
		break;
	}
}

static void home_screen_imglight_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_LOADER);
		add_loader(load_print);
	}
		break;
	default:
		break;
	}
}

static void home_screen_imgsurve_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_SETUP); 
		lv_demo_printer_anim_in_all(guider_ui.setup, 200);
	}
		break;
	default:
		break;
	}
}

static void home_screen_temp_but_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.scrTemp_del == true)
				setup_scr_scrTemp(&guider_ui);
			lv_scr_load_anim(guider_ui.scrTemp, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.home_screen_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_home_screen(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->home_screen_imgbtn_surve, home_screen_imgbtn_surve_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imgbtn_humid, home_screen_imgbtn_humid_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imgbtn_fanlght, home_screen_imgbtn_fanlght_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imgcopy, home_screen_imgcopy_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imgscan, home_screen_imgscan_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imglight, home_screen_imglight_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_imgsurve, home_screen_imgsurve_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->home_screen_temp_but, home_screen_temp_but_event_handler, LV_EVENT_ALL, NULL);
}

static void scrTemp_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.home_screen_del == true)
				setup_scr_home_screen(&guider_ui);
			lv_scr_load_anim(guider_ui.home_screen, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrTemp_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_scrTemp(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->scrTemp_imgbtn_1, scrTemp_imgbtn_1_event_handler, LV_EVENT_ALL, NULL);
}

static void scrHumid_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.home_screen_del == true)
				setup_scr_home_screen(&guider_ui);
			lv_scr_load_anim(guider_ui.home_screen, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrHumid_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_scrHumid(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->scrHumid_imgbtn_1, scrHumid_imgbtn_1_event_handler, LV_EVENT_ALL, NULL);
}

static void scrnFanLightselect_imgbtn_humid_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.scrFan_del == true)
				setup_scr_scrFan(&guider_ui);
			lv_scr_load_anim(guider_ui.scrFan, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrnFanLightselect_del = true;
	}
		break;
	default:
		break;
	}
}

static void scrnFanLightselect_imgbtn_fanlght_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.scrnLight_del == true)
				setup_scr_scrnLight(&guider_ui);
			lv_scr_load_anim(guider_ui.scrnLight, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrnFanLightselect_del = true;
	}
		break;
	default:
		break;
	}
}

static void scrnFanLightselect_imgcopy_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_LOADER);
		add_loader(load_copy);
	}
		break;
	default:
		break;
	}
}

static void scrnFanLightselect_imglight_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		guider_load_screen(SCR_LOADER);
		add_loader(load_print);
	}
		break;
	default:
		break;
	}
}

void events_init_scrnFanLightselect(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->scrnFanLightselect_imgbtn_humid, scrnFanLightselect_imgbtn_humid_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->scrnFanLightselect_imgbtn_fanlght, scrnFanLightselect_imgbtn_fanlght_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->scrnFanLightselect_imgcopy, scrnFanLightselect_imgcopy_event_handler, LV_EVENT_ALL, NULL);
	lv_obj_add_event_cb(ui->scrnFanLightselect_imglight, scrnFanLightselect_imglight_event_handler, LV_EVENT_ALL, NULL);
}

static void scrFan_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.home_screen_del == true)
				setup_scr_home_screen(&guider_ui);
			lv_scr_load_anim(guider_ui.home_screen, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrFan_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_scrFan(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->scrFan_imgbtn_1, scrFan_imgbtn_1_event_handler, LV_EVENT_ALL, NULL);
}

static void scrnLight_imgbtn_1_event_handler(lv_event_t *e)
{
	lv_event_code_t code = lv_event_get_code(e);
	switch (code)
	{
	case LV_EVENT_PRESSED:
	{
		lv_disp_t * d = lv_obj_get_disp(lv_scr_act());
		if (d->prev_scr == NULL && d->scr_to_load == NULL)
		{
			if (guider_ui.home_screen_del == true)
				setup_scr_home_screen(&guider_ui);
			lv_scr_load_anim(guider_ui.home_screen, LV_SCR_LOAD_ANIM_OVER_TOP, 0, 0, true);
		}
		guider_ui.scrnLight_del = true;
	}
		break;
	default:
		break;
	}
}

void events_init_scrnLight(lv_ui *ui)
{
	lv_obj_add_event_cb(ui->scrnLight_imgbtn_1, scrnLight_imgbtn_1_event_handler, LV_EVENT_ALL, NULL);
}
