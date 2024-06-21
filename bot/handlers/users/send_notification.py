from loader import bot
from data.prayer_times import PRAYER_TIMES
from data.regions import REGIONS
import datetime

from functions.API.prayer_times.prayer_times import get_prayer_time
from functions.API.users.filter_by_region import get_user_filter_by_region
from functions.create_cron import create_cron_time
from functions.send_message import send_message_prayer_on_time

from text.text import PRAYER_TIME
from keyboards.inline.notification import notification_btn

import datetime
from aiocron import crontab


@crontab("0 1 * * *")
async def update_prayer_time():
    split_day = str(datetime.datetime.now().strftime('%x')).split("/")
    today = f"""{split_day[1]}-{split_day[0]}-{split_day[2]}"""
    data = {}

    for region in REGIONS:
        prayer_time = get_prayer_time(region)

        if prayer_time.status_code == 200:
            try:
                weekday = prayer_time.json()['data']['weekday']
                hijri_date = prayer_time.json()['data']['hijri_date']
                date = prayer_time.json()['data']['date']

                prayer_time = prayer_time.json()['data']['times']

                data[region] = {
                    'tong': prayer_time['tong_saharlik'],
                    'quyosh': prayer_time['quyosh'],
                    'peshin': prayer_time['peshin'],
                    'asr': prayer_time['asr'],
                    'shom_iftor': prayer_time['shom_iftor'],
                    'hufton': prayer_time['hufton'],
                }

                users = get_user_filter_by_region(region)
                
                for user in users:
                    if user['notification']:
                        await bot.send_message(chat_id=int(user['id']), 
                        text=f"<b>Bugungi namoz vaqtlari ({today})👇</b>")
                        await bot.send_message(chat_id=int(user['id']), text=PRAYER_TIME(
                            times={
                                'tong_saharlik': prayer_time['tong_saharlik'],
                                'quyosh': prayer_time['quyosh'],
                                'peshin': prayer_time['peshin'],
                                'asr': prayer_time['asr'],
                                'shom_iftor': prayer_time['shom_iftor'],
                                'hufton': prayer_time['hufton'],
                            },
                            weekday=weekday,
                            hijri_date=hijri_date,
                            region=region,
                            date=date
                        ), reply_markup=notification_btn)
            except Exception as exc:
                print(f"handlers/send_notification.py #ERROR     [{datetime.datetime.now()}]  {exc}")
    
    PRAYER_TIMES.clear()
    PRAYER_TIMES.append(data)


@crontab(create_cron_time(PRAYER_TIMES[0]["Toshkent"]["tong"]))
async def tong_region1():
    for user in get_user_filter_by_region(region="Toshkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshkent"]["peshin"]))
async def peshin_region1():
    for user in get_user_filter_by_region(region="Toshkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshkent"]["asr"]))
async def asr_region1():
    for user in get_user_filter_by_region(region="Toshkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )


@crontab(create_cron_time(PRAYER_TIMES[0]["Toshkent"]["shom_iftor"]))
async def shom_region1():
    for user in get_user_filter_by_region(region="Toshkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshkent"]["hufton"]))
async def hufton_region1():
    for user in get_user_filter_by_region(region="Toshkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Samarqand"]["tong"]))
async def tong_region2():
    for user in get_user_filter_by_region(region="Samarqand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Samarqand"]["peshin"]))
async def peshin_region2():
    for user in get_user_filter_by_region(region="Samarqand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Samarqand"]["asr"]))
async def asr_region2():
    for user in get_user_filter_by_region(region="Samarqand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Samarqand"]["shom_iftor"]))
async def shom_region2():
    for user in get_user_filter_by_region(region="Samarqand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Samarqand"]["hufton"]))
async def hufton_region2():
    for user in get_user_filter_by_region(region="Samarqand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jizzax"]["tong"]))
async def tong_region3():
    for user in get_user_filter_by_region(region="Jizzax"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jizzax"]["peshin"]))
async def peshin_region3():
    for user in get_user_filter_by_region(region="Jizzax"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jizzax"]["asr"]))
async def asr_region3():
    for user in get_user_filter_by_region(region="Jizzax"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jizzax"]["shom_iftor"]))
async def shom_region3():
    for user in get_user_filter_by_region(region="Jizzax"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jizzax"]["hufton"]))
async def hufton_region3():
    for user in get_user_filter_by_region(region="Jizzax"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'qon"]["tong"]))
async def tong_region4():
    for user in get_user_filter_by_region(region="Qo'qon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'qon"]["peshin"]))
async def peshin_region4():
    for user in get_user_filter_by_region(region="Qo'qon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'qon"]["asr"]))
async def asr_region4():
    for user in get_user_filter_by_region(region="Qo'qon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'qon"]["shom_iftor"]))
async def shom_region4():
    for user in get_user_filter_by_region(region="Qo'qon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'qon"]["hufton"]))
async def hufton_region4():
    for user in get_user_filter_by_region(region="Qo'qon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Andijon"]["tong"]))
async def tong_region5():
    for user in get_user_filter_by_region(region="Andijon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Andijon"]["peshin"]))
async def peshin_region5():
    for user in get_user_filter_by_region(region="Andijon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Andijon"]["asr"]))
async def asr_region5():
    for user in get_user_filter_by_region(region="Andijon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Andijon"]["shom_iftor"]))
async def shom_region5():
    for user in get_user_filter_by_region(region="Andijon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Andijon"]["hufton"]))
async def hufton_region5():
    for user in get_user_filter_by_region(region="Andijon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Namangan"]["tong"]))
async def tong_region6():
    for user in get_user_filter_by_region(region="Namangan"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Namangan"]["peshin"]))
async def peshin_region6():
    for user in get_user_filter_by_region(region="Namangan"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Namangan"]["asr"]))
async def asr_region6():
    for user in get_user_filter_by_region(region="Namangan"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Namangan"]["shom_iftor"]))
async def shom_region6():
    for user in get_user_filter_by_region(region="Namangan"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Namangan"]["hufton"]))
async def hufton_region6():
    for user in get_user_filter_by_region(region="Namangan"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Farg'ona"]["tong"]))
async def tong_region7():
    for user in get_user_filter_by_region(region="Farg'ona"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Farg'ona"]["peshin"]))
async def peshin_region7():
    for user in get_user_filter_by_region(region="Farg'ona"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Farg'ona"]["asr"]))
async def asr_region7():
    for user in get_user_filter_by_region(region="Farg'ona"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Farg'ona"]["shom_iftor"]))
async def shom_region7():
    for user in get_user_filter_by_region(region="Farg'ona"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Farg'ona"]["hufton"]))
async def hufton_region7():
    for user in get_user_filter_by_region(region="Farg'ona"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Navoiy"]["tong"]))
async def tong_region8():
    for user in get_user_filter_by_region(region="Navoiy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Navoiy"]["peshin"]))
async def peshin_region8():
    for user in get_user_filter_by_region(region="Navoiy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Navoiy"]["asr"]))
async def asr_region8():
    for user in get_user_filter_by_region(region="Navoiy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Navoiy"]["shom_iftor"]))
async def shom_region8():
    for user in get_user_filter_by_region(region="Navoiy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Navoiy"]["hufton"]))
async def hufton_region8():
    for user in get_user_filter_by_region(region="Navoiy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Termiz"]["tong"]))
async def tong_region9():
    for user in get_user_filter_by_region(region="Termiz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Termiz"]["peshin"]))
async def peshin_region9():
    for user in get_user_filter_by_region(region="Termiz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Termiz"]["asr"]))
async def asr_region9():
    for user in get_user_filter_by_region(region="Termiz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Termiz"]["shom_iftor"]))
async def shom_region9():
    for user in get_user_filter_by_region(region="Termiz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Termiz"]["hufton"]))
async def hufton_region9():
    for user in get_user_filter_by_region(region="Termiz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qarshi"]["tong"]))
async def tong_region10():
    for user in get_user_filter_by_region(region="Qarshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qarshi"]["peshin"]))
async def peshin_region10():
    for user in get_user_filter_by_region(region="Qarshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qarshi"]["asr"]))
async def asr_region10():
    for user in get_user_filter_by_region(region="Qarshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qarshi"]["shom_iftor"]))
async def shom_region10():
    for user in get_user_filter_by_region(region="Qarshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qarshi"]["hufton"]))
async def hufton_region10():
    for user in get_user_filter_by_region(region="Qarshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buxoro"]["tong"]))
async def tong_region11():
    for user in get_user_filter_by_region(region="Buxoro"):
                await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buxoro"]["peshin"]))
async def peshin_region11():
    for user in get_user_filter_by_region(region="Buxoro"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buxoro"]["asr"]))
async def asr_region11():
    for user in get_user_filter_by_region(region="Buxoro"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Buxoro"]["shom_iftor"]))
async def shom_region11():
    for user in get_user_filter_by_region(region="Buxoro"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Buxoro"]["hufton"]))
async def hufton_region11():
    for user in get_user_filter_by_region(region="Buxoro"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Guliston"]["tong"]))
async def tong_region12():
    for user in get_user_filter_by_region(region="Guliston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Guliston"]["peshin"]))
async def peshin_region12():
    for user in get_user_filter_by_region(region="Guliston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Guliston"]["asr"]))
async def asr_region12():
    for user in get_user_filter_by_region(region="Guliston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Guliston"]["shom_iftor"]))
async def shom_region12():
    for user in get_user_filter_by_region(region="Guliston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Guliston"]["hufton"]))
async def hufton_region12():
    for user in get_user_filter_by_region(region="Guliston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nukus"]["tong"]))
async def tong_region13():
    for user in get_user_filter_by_region(region="Nukus"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nukus"]["peshin"]))
async def peshin_region13():
    for user in get_user_filter_by_region(region="Nukus"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nukus"]["asr"]))
async def asr_region13():
    for user in get_user_filter_by_region(region="Nukus"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Nukus"]["shom_iftor"]))
async def shom_region13():
    for user in get_user_filter_by_region(region="Nukus"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Nukus"]["hufton"]))
async def hufton_region13():
    for user in get_user_filter_by_region(region="Nukus"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xiva"]["tong"]))
async def tong_region14():
    for user in get_user_filter_by_region(region="Xiva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xiva"]["peshin"]))
async def peshin_region14():
    for user in get_user_filter_by_region(region="Xiva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xiva"]["asr"]))
async def asr_region14():
    for user in get_user_filter_by_region(region="Xiva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xiva"]["shom_iftor"]))
async def shom_region14():
    for user in get_user_filter_by_region(region="Xiva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xiva"]["hufton"]))
async def hufton_region14():
    for user in get_user_filter_by_region(region="Xiva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urganch"]["tong"]))
async def tong_region15():
    for user in get_user_filter_by_region(region="Urganch"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urganch"]["peshin"]))
async def peshin_region15():
    for user in get_user_filter_by_region(region="Urganch"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urganch"]["asr"]))
async def asr_region15():
    for user in get_user_filter_by_region(region="Urganch"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Urganch"]["shom_iftor"]))
async def shom_region15():
    for user in get_user_filter_by_region(region="Urganch"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Urganch"]["hufton"]))
async def hufton_region15():
    for user in get_user_filter_by_region(region="Urganch"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimkent"]["tong"]))
async def tong_region16():
    for user in get_user_filter_by_region(region="Chimkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimkent"]["peshin"]))
async def peshin_region16():
    for user in get_user_filter_by_region(region="Chimkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimkent"]["asr"]))
async def asr_region16():
    for user in get_user_filter_by_region(region="Chimkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimkent"]["shom_iftor"]))
async def shom_region16():
    for user in get_user_filter_by_region(region="Chimkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimkent"]["hufton"]))
async def hufton_region16():
    for user in get_user_filter_by_region(region="Chimkent"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'sh"]["tong"]))
async def tong_region17():
    for user in get_user_filter_by_region(region="O'sh"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'sh"]["peshin"]))
async def peshin_region17():
    for user in get_user_filter_by_region(region="O'sh"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'sh"]["asr"]))
async def asr_region17():
    for user in get_user_filter_by_region(region="O'sh"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'sh"]["shom_iftor"]))
async def shom_region17():
    for user in get_user_filter_by_region(region="O'sh"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'sh"]["hufton"]))
async def hufton_region17():
    for user in get_user_filter_by_region(region="O'sh"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bekobod"]["tong"]))
async def tong_region18():
    for user in get_user_filter_by_region(region="Bekobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bekobod"]["peshin"]))
async def peshin_region18():
    for user in get_user_filter_by_region(region="Bekobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bekobod"]["asr"]))
async def asr_region18():
    for user in get_user_filter_by_region(region="Bekobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Bekobod"]["shom_iftor"]))
async def shom_region18():
    for user in get_user_filter_by_region(region="Bekobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Bekobod"]["hufton"]))
async def hufton_region18():
    for user in get_user_filter_by_region(region="Bekobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bishkek"]["tong"]))
async def tong_region19():
    for user in get_user_filter_by_region(region="Bishkek"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bishkek"]["peshin"]))
async def peshin_region19():
    for user in get_user_filter_by_region(region="Bishkek"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Bishkek"]["asr"]))
async def asr_region19():
    for user in get_user_filter_by_region(region="Bishkek"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Bishkek"]["shom_iftor"]))
async def shom_region19():
    for user in get_user_filter_by_region(region="Bishkek"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Bishkek"]["hufton"]))
async def hufton_region19():
    for user in get_user_filter_by_region(region="Bishkek"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Denov"]["tong"]))
async def tong_region20():
    for user in get_user_filter_by_region(region="Denov"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Denov"]["peshin"]))
async def peshin_region20():
    for user in get_user_filter_by_region(region="Denov"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Denov"]["asr"]))
async def asr_region20():
    for user in get_user_filter_by_region(region="Denov"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Denov"]["shom_iftor"]))
async def shom_region20():
    for user in get_user_filter_by_region(region="Denov"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Denov"]["hufton"]))
async def hufton_region20():
    for user in get_user_filter_by_region(region="Denov"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jalolobod"]["tong"]))
async def tong_region21():
    for user in get_user_filter_by_region(region="Jalolobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jalolobod"]["peshin"]))
async def peshin_region21():
    for user in get_user_filter_by_region(region="Jalolobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jalolobod"]["asr"]))
async def asr_region21():
    for user in get_user_filter_by_region(region="Jalolobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jalolobod"]["shom_iftor"]))
async def shom_region21():
    for user in get_user_filter_by_region(region="Jalolobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jalolobod"]["hufton"]))
async def hufton_region21():
    for user in get_user_filter_by_region(region="Jalolobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jambul"]["tong"]))
async def tong_region22():
    for user in get_user_filter_by_region(region="Jambul"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jambul"]["peshin"]))
async def peshin_region22():
    for user in get_user_filter_by_region(region="Jambul"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jambul"]["asr"]))
async def asr_region22():
    for user in get_user_filter_by_region(region="Jambul"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jambul"]["shom_iftor"]))
async def shom_region22():
    for user in get_user_filter_by_region(region="Jambul"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jambul"]["hufton"]))
async def hufton_region22():
    for user in get_user_filter_by_region(region="Jambul"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jomboy"]["tong"]))
async def tong_region23():
    for user in get_user_filter_by_region(region="Jomboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jomboy"]["peshin"]))
async def peshin_region23():
    for user in get_user_filter_by_region(region="Jomboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Jomboy"]["asr"]))
async def asr_region23():
    for user in get_user_filter_by_region(region="Jomboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jomboy"]["shom_iftor"]))
async def shom_region23():
    for user in get_user_filter_by_region(region="Jomboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Jomboy"]["hufton"]))
async def hufton_region23():
    for user in get_user_filter_by_region(region="Jomboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Kattaqo'rg'on"]["tong"]))
async def tong_region24():
    for user in get_user_filter_by_region(region="Kattaqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Kattaqo'rg'on"]["peshin"]))
async def peshin_region24():
    for user in get_user_filter_by_region(region="Kattaqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Kattaqo'rg'on"]["asr"]))
async def asr_region24():
    for user in get_user_filter_by_region(region="Kattaqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Kattaqo'rg'on"]["shom_iftor"]))
async def shom_region24():
    for user in get_user_filter_by_region(region="Kattaqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Kattaqo'rg'on"]["hufton"]))
async def hufton_region24():
    for user in get_user_filter_by_region(region="Kattaqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konibodom"]["tong"]))
async def tong_region25():
    for user in get_user_filter_by_region(region="Konibodom"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konibodom"]["peshin"]))
async def peshin_region25():
    for user in get_user_filter_by_region(region="Konibodom"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konibodom"]["asr"]))
async def asr_region25():
    for user in get_user_filter_by_region(region="Konibodom"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Konibodom"]["shom_iftor"]))
async def shom_region25():
    for user in get_user_filter_by_region(region="Konibodom"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Konibodom"]["hufton"]))
async def hufton_region25():
    for user in get_user_filter_by_region(region="Konibodom"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Marg'ilon"]["tong"]))
async def tong_region26():
    for user in get_user_filter_by_region(region="Marg'ilon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Marg'ilon"]["peshin"]))
async def peshin_region26():
    for user in get_user_filter_by_region(region="Marg'ilon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Marg'ilon"]["asr"]))
async def asr_region26():
    for user in get_user_filter_by_region(region="Marg'ilon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Marg'ilon"]["shom_iftor"]))
async def shom_region26():
    for user in get_user_filter_by_region(region="Marg'ilon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Marg'ilon"]["hufton"]))
async def hufton_region26():
    for user in get_user_filter_by_region(region="Marg'ilon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nurota"]["tong"]))
async def tong_region27():
    for user in get_user_filter_by_region(region="Nurota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nurota"]["peshin"]))
async def peshin_region27():
    for user in get_user_filter_by_region(region="Nurota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Nurota"]["asr"]))
async def asr_region27():
    for user in get_user_filter_by_region(region="Nurota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Nurota"]["shom_iftor"]))
async def shom_region27():
    for user in get_user_filter_by_region(region="Nurota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Nurota"]["hufton"]))
async def hufton_region27():
    for user in get_user_filter_by_region(region="Nurota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkiston"]["tong"]))
async def tong_region28():
    for user in get_user_filter_by_region(region="Turkiston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkiston"]["peshin"]))
async def peshin_region28():
    for user in get_user_filter_by_region(region="Turkiston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkiston"]["asr"]))
async def asr_region28():
    for user in get_user_filter_by_region(region="Turkiston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkiston"]["shom_iftor"]))
async def shom_region28():
    for user in get_user_filter_by_region(region="Turkiston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkiston"]["hufton"]))
async def hufton_region28():
    for user in get_user_filter_by_region(region="Turkiston"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jand"]["tong"]))
async def tong_region29():
    for user in get_user_filter_by_region(region="Xo'jand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jand"]["peshin"]))
async def peshin_region29():
    for user in get_user_filter_by_region(region="Xo'jand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jand"]["asr"]))
async def asr_region29():
    for user in get_user_filter_by_region(region="Xo'jand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jand"]["shom_iftor"]))
async def shom_region29():
    for user in get_user_filter_by_region(region="Xo'jand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jand"]["hufton"]))
async def hufton_region29():
    for user in get_user_filter_by_region(region="Xo'jand"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shahrixon"]["tong"]))
async def tong_region30():
    for user in get_user_filter_by_region(region="Shahrixon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shahrixon"]["peshin"]))
async def peshin_region30():
    for user in get_user_filter_by_region(region="Shahrixon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shahrixon"]["asr"]))
async def asr_region30():
    for user in get_user_filter_by_region(region="Shahrixon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shahrixon"]["shom_iftor"]))
async def shom_region30():
    for user in get_user_filter_by_region(region="Shahrixon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shahrixon"]["hufton"]))
async def hufton_region30():
    for user in get_user_filter_by_region(region="Shahrixon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jaobod"]["tong"]))
async def tong_region31():
    for user in get_user_filter_by_region(region="Xo'jaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jaobod"]["peshin"]))
async def peshin_region31():
    for user in get_user_filter_by_region(region="Xo'jaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jaobod"]["asr"]))
async def asr_region31():
    for user in get_user_filter_by_region(region="Xo'jaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jaobod"]["shom_iftor"]))
async def shom_region31():
    for user in get_user_filter_by_region(region="Xo'jaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xo'jaobod"]["hufton"]))
async def hufton_region31():
    for user in get_user_filter_by_region(region="Xo'jaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'rg'ontepa"]["tong"]))
async def tong_region32():
    for user in get_user_filter_by_region(region="Qo'rg'ontepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'rg'ontepa"]["peshin"]))
async def peshin_region32():
    for user in get_user_filter_by_region(region="Qo'rg'ontepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'rg'ontepa"]["asr"]))
async def asr_region32():
    for user in get_user_filter_by_region(region="Qo'rg'ontepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'rg'ontepa"]["shom_iftor"]))
async def shom_region32():
    for user in get_user_filter_by_region(region="Qo'rg'ontepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'rg'ontepa"]["hufton"]))
async def hufton_region32():
    for user in get_user_filter_by_region(region="Qo'rg'ontepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonobod"]["tong"]))
async def tong_region33():
    for user in get_user_filter_by_region(region="Xonobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonobod"]["peshin"]))
async def peshin_region33():
    for user in get_user_filter_by_region(region="Xonobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonobod"]["asr"]))
async def asr_region33():
    for user in get_user_filter_by_region(region="Xonobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonobod"]["shom_iftor"]))
async def shom_region33():
    for user in get_user_filter_by_region(region="Xonobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonobod"]["hufton"]))
async def hufton_region33():
    for user in get_user_filter_by_region(region="Xonobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Pop"]["tong"]))
async def tong_region34():
    for user in get_user_filter_by_region(region="Pop"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Pop"]["peshin"]))
async def peshin_region34():
    for user in get_user_filter_by_region(region="Pop"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Pop"]["asr"]))
async def asr_region34():
    for user in get_user_filter_by_region(region="Pop"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Pop"]["shom_iftor"]))
async def shom_region34():
    for user in get_user_filter_by_region(region="Pop"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Pop"]["hufton"]))
async def hufton_region34():
    for user in get_user_filter_by_region(region="Pop"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chust"]["tong"]))
async def tong_region35():
    for user in get_user_filter_by_region(region="Chust"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chust"]["peshin"]))
async def peshin_region35():
    for user in get_user_filter_by_region(region="Chust"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chust"]["asr"]))
async def asr_region35():
    for user in get_user_filter_by_region(region="Chust"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chust"]["shom_iftor"]))
async def shom_region35():
    for user in get_user_filter_by_region(region="Chust"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chust"]["hufton"]))
async def hufton_region35():
    for user in get_user_filter_by_region(region="Chust"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chortoq"]["tong"]))
async def tong_region36():
    for user in get_user_filter_by_region(region="Chortoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chortoq"]["peshin"]))
async def peshin_region36():
    for user in get_user_filter_by_region(region="Chortoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chortoq"]["asr"]))
async def asr_region36():
    for user in get_user_filter_by_region(region="Chortoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chortoq"]["shom_iftor"]))
async def shom_region36():
    for user in get_user_filter_by_region(region="Chortoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chortoq"]["hufton"]))
async def hufton_region36():
    for user in get_user_filter_by_region(region="Chortoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchqo'rg'on"]["tong"]))
async def tong_region37():
    for user in get_user_filter_by_region(region="Uchqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchqo'rg'on"]["peshin"]))
async def peshin_region37():
    for user in get_user_filter_by_region(region="Uchqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchqo'rg'on"]["asr"]))
async def asr_region37():
    for user in get_user_filter_by_region(region="Uchqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchqo'rg'on"]["shom_iftor"]))
async def shom_region37():
    for user in get_user_filter_by_region(region="Uchqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchqo'rg'on"]["hufton"]))
async def hufton_region37():
    for user in get_user_filter_by_region(region="Uchqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltiariq"]["tong"]))
async def tong_region38():
    for user in get_user_filter_by_region(region="Oltiariq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltiariq"]["peshin"]))
async def peshin_region38():
    for user in get_user_filter_by_region(region="Oltiariq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltiariq"]["asr"]))
async def asr_region38():
    for user in get_user_filter_by_region(region="Oltiariq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltiariq"]["shom_iftor"]))
async def shom_region38():
    for user in get_user_filter_by_region(region="Oltiariq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltiariq"]["hufton"]))
async def hufton_region38():
    for user in get_user_filter_by_region(region="Oltiariq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Rishton"]["tong"]))
async def tong_region39():
    for user in get_user_filter_by_region(region="Rishton"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Rishton"]["peshin"]))
async def peshin_region39():
    for user in get_user_filter_by_region(region="Rishton"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Rishton"]["asr"]))
async def asr_region39():
    for user in get_user_filter_by_region(region="Rishton"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Rishton"]["shom_iftor"]))
async def shom_region39():
    for user in get_user_filter_by_region(region="Rishton"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Rishton"]["hufton"]))
async def hufton_region39():
    for user in get_user_filter_by_region(region="Rishton"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Quva"]["tong"]))
async def tong_region40():
    for user in get_user_filter_by_region(region="Quva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Quva"]["peshin"]))
async def peshin_region40():
    for user in get_user_filter_by_region(region="Quva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Quva"]["asr"]))
async def asr_region40():
    for user in get_user_filter_by_region(region="Quva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Quva"]["shom_iftor"]))
async def shom_region40():
    for user in get_user_filter_by_region(region="Quva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Quva"]["hufton"]))
async def hufton_region40():
    for user in get_user_filter_by_region(region="Quva"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olmaota"]["tong"]))
async def tong_region41():
    for user in get_user_filter_by_region(region="Olmaota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olmaota"]["peshin"]))
async def peshin_region41():
    for user in get_user_filter_by_region(region="Olmaota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olmaota"]["asr"]))
async def asr_region41():
    for user in get_user_filter_by_region(region="Olmaota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Olmaota"]["shom_iftor"]))
async def shom_region41():
    for user in get_user_filter_by_region(region="Olmaota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Olmaota"]["hufton"]))
async def hufton_region41():
    for user in get_user_filter_by_region(region="Olmaota"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sayram"]["tong"]))
async def tong_region42():
    for user in get_user_filter_by_region(region="Sayram"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sayram"]["peshin"]))
async def peshin_region42():
    for user in get_user_filter_by_region(region="Sayram"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sayram"]["asr"]))
async def asr_region42():
    for user in get_user_filter_by_region(region="Sayram"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Sayram"]["shom_iftor"]))
async def shom_region42():
    for user in get_user_filter_by_region(region="Sayram"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Sayram"]["hufton"]))
async def hufton_region42():
    for user in get_user_filter_by_region(region="Sayram"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Angren"]["tong"]))
async def tong_region43():
    for user in get_user_filter_by_region(region="Angren"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Angren"]["peshin"]))
async def peshin_region43():
    for user in get_user_filter_by_region(region="Angren"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Angren"]["asr"]))
async def asr_region43():
    for user in get_user_filter_by_region(region="Angren"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Angren"]["shom_iftor"]))
async def shom_region43():
    for user in get_user_filter_by_region(region="Angren"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Angren"]["hufton"]))
async def hufton_region43():
    for user in get_user_filter_by_region(region="Angren"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Burchmulla"]["tong"]))
async def tong_region44():
    for user in get_user_filter_by_region(region="Burchmulla"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Burchmulla"]["peshin"]))
async def peshin_region44():
    for user in get_user_filter_by_region(region="Burchmulla"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Burchmulla"]["asr"]))
async def asr_region44():
    for user in get_user_filter_by_region(region="Burchmulla"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Burchmulla"]["shom_iftor"]))
async def shom_region44():
    for user in get_user_filter_by_region(region="Burchmulla"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Burchmulla"]["hufton"]))
async def hufton_region44():
    for user in get_user_filter_by_region(region="Burchmulla"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olot"]["tong"]))
async def tong_region45():
    for user in get_user_filter_by_region(region="Olot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olot"]["peshin"]))
async def peshin_region45():
    for user in get_user_filter_by_region(region="Olot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Olot"]["asr"]))
async def asr_region45():
    for user in get_user_filter_by_region(region="Olot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Olot"]["shom_iftor"]))
async def shom_region45():
    for user in get_user_filter_by_region(region="Olot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Olot"]["hufton"]))
async def hufton_region45():
    for user in get_user_filter_by_region(region="Olot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Gazli"]["tong"]))
async def tong_region46():
    for user in get_user_filter_by_region(region="Gazli"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Gazli"]["peshin"]))
async def peshin_region46():
    for user in get_user_filter_by_region(region="Gazli"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Gazli"]["asr"]))
async def asr_region46():
    for user in get_user_filter_by_region(region="Gazli"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Gazli"]["shom_iftor"]))
async def shom_region46():
    for user in get_user_filter_by_region(region="Gazli"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Gazli"]["hufton"]))
async def hufton_region46():
    for user in get_user_filter_by_region(region="Gazli"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorovulbozor"]["tong"]))
async def tong_region47():
    for user in get_user_filter_by_region(region="Qorovulbozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorovulbozor"]["peshin"]))
async def peshin_region47():
    for user in get_user_filter_by_region(region="Qorovulbozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorovulbozor"]["asr"]))
async def asr_region47():
    for user in get_user_filter_by_region(region="Qorovulbozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorovulbozor"]["shom_iftor"]))
async def shom_region47():
    for user in get_user_filter_by_region(region="Qorovulbozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorovulbozor"]["hufton"]))
async def hufton_region47():
    for user in get_user_filter_by_region(region="Qorovulbozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorako'l"]["tong"]))
async def tong_region48():
    for user in get_user_filter_by_region(region="Qorako'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorako'l"]["peshin"]))
async def peshin_region48():
    for user in get_user_filter_by_region(region="Qorako'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorako'l"]["asr"]))
async def asr_region48():
    for user in get_user_filter_by_region(region="Qorako'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorako'l"]["shom_iftor"]))
async def shom_region48():
    for user in get_user_filter_by_region(region="Qorako'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qorako'l"]["hufton"]))
async def hufton_region48():
    for user in get_user_filter_by_region(region="Qorako'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Paxtaobod"]["tong"]))
async def tong_region49():
    for user in get_user_filter_by_region(region="Paxtaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Paxtaobod"]["peshin"]))
async def peshin_region49():
    for user in get_user_filter_by_region(region="Paxtaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Paxtaobod"]["asr"]))
async def asr_region49():
    for user in get_user_filter_by_region(region="Paxtaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Paxtaobod"]["shom_iftor"]))
async def shom_region49():
    for user in get_user_filter_by_region(region="Paxtaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Paxtaobod"]["hufton"]))
async def hufton_region49():
    for user in get_user_filter_by_region(region="Paxtaobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zomin"]["tong"]))
async def tong_region50():
    for user in get_user_filter_by_region(region="Zomin"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zomin"]["peshin"]))
async def peshin_region50():
    for user in get_user_filter_by_region(region="Zomin"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zomin"]["asr"]))
async def asr_region50():
    for user in get_user_filter_by_region(region="Zomin"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Zomin"]["shom_iftor"]))
async def shom_region50():
    for user in get_user_filter_by_region(region="Zomin"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Zomin"]["hufton"]))
async def hufton_region50():
    for user in get_user_filter_by_region(region="Zomin"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Do'stlik"]["tong"]))
async def tong_region51():
    for user in get_user_filter_by_region(region="Do'stlik"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Do'stlik"]["peshin"]))
async def peshin_region51():
    for user in get_user_filter_by_region(region="Do'stlik"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Do'stlik"]["asr"]))
async def asr_region51():
    for user in get_user_filter_by_region(region="Do'stlik"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Do'stlik"]["shom_iftor"]))
async def shom_region51():
    for user in get_user_filter_by_region(region="Do'stlik"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Do'stlik"]["hufton"]))
async def hufton_region51():
    for user in get_user_filter_by_region(region="Do'stlik"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Arnasoy"]["tong"]))
async def tong_region52():
    for user in get_user_filter_by_region(region="Arnasoy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Arnasoy"]["peshin"]))
async def peshin_region52():
    for user in get_user_filter_by_region(region="Arnasoy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Arnasoy"]["asr"]))
async def asr_region52():
    for user in get_user_filter_by_region(region="Arnasoy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Arnasoy"]["shom_iftor"]))
async def shom_region52():
    for user in get_user_filter_by_region(region="Arnasoy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Arnasoy"]["hufton"]))
async def hufton_region52():
    for user in get_user_filter_by_region(region="Arnasoy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'smat"]["tong"]))
async def tong_region53():
    for user in get_user_filter_by_region(region="O'smat"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'smat"]["peshin"]))
async def peshin_region53():
    for user in get_user_filter_by_region(region="O'smat"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'smat"]["asr"]))
async def asr_region53():
    for user in get_user_filter_by_region(region="O'smat"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'smat"]["shom_iftor"]))
async def shom_region53():
    for user in get_user_filter_by_region(region="O'smat"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'smat"]["hufton"]))
async def hufton_region53():
    for user in get_user_filter_by_region(region="O'smat"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'allaorol"]["tong"]))
async def tong_region54():
    for user in get_user_filter_by_region(region="G'allaorol"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'allaorol"]["peshin"]))
async def peshin_region54():
    for user in get_user_filter_by_region(region="G'allaorol"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'allaorol"]["asr"]))
async def asr_region54():
    for user in get_user_filter_by_region(region="G'allaorol"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["G'allaorol"]["shom_iftor"]))
async def shom_region54():
    for user in get_user_filter_by_region(region="G'allaorol"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["G'allaorol"]["hufton"]))
async def hufton_region54():
    for user in get_user_filter_by_region(region="G'allaorol"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchtepa"]["tong"]))
async def tong_region55():
    for user in get_user_filter_by_region(region="Uchtepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchtepa"]["peshin"]))
async def peshin_region55():
    for user in get_user_filter_by_region(region="Uchtepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchtepa"]["asr"]))
async def asr_region55():
    for user in get_user_filter_by_region(region="Uchtepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchtepa"]["shom_iftor"]))
async def shom_region55():
    for user in get_user_filter_by_region(region="Uchtepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchtepa"]["hufton"]))
async def hufton_region55():
    for user in get_user_filter_by_region(region="Uchtepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'g'iz"]["tong"]))
async def tong_region56():
    for user in get_user_filter_by_region(region="O'g'iz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'g'iz"]["peshin"]))
async def peshin_region56():
    for user in get_user_filter_by_region(region="O'g'iz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["O'g'iz"]["asr"]))
async def asr_region56():
    for user in get_user_filter_by_region(region="O'g'iz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'g'iz"]["shom_iftor"]))
async def shom_region56():
    for user in get_user_filter_by_region(region="O'g'iz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["O'g'iz"]["hufton"]))
async def hufton_region56():
    for user in get_user_filter_by_region(region="O'g'iz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tomdi"]["tong"]))
async def tong_region57():
    for user in get_user_filter_by_region(region="Tomdi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tomdi"]["peshin"]))
async def peshin_region57():
    for user in get_user_filter_by_region(region="Tomdi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tomdi"]["asr"]))
async def asr_region57():
    for user in get_user_filter_by_region(region="Tomdi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Tomdi"]["shom_iftor"]))
async def shom_region57():
    for user in get_user_filter_by_region(region="Tomdi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Tomdi"]["hufton"]))
async def hufton_region57():
    for user in get_user_filter_by_region(region="Tomdi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konimex"]["tong"]))
async def tong_region58():
    for user in get_user_filter_by_region(region="Konimex"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konimex"]["peshin"]))
async def peshin_region58():
    for user in get_user_filter_by_region(region="Konimex"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Konimex"]["asr"]))
async def asr_region58():
    for user in get_user_filter_by_region(region="Konimex"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Konimex"]["shom_iftor"]))
async def shom_region58():
    for user in get_user_filter_by_region(region="Konimex"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Konimex"]["hufton"]))
async def hufton_region58():
    for user in get_user_filter_by_region(region="Konimex"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qiziltepa"]["tong"]))
async def tong_region59():
    for user in get_user_filter_by_region(region="Qiziltepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qiziltepa"]["peshin"]))
async def peshin_region59():
    for user in get_user_filter_by_region(region="Qiziltepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qiziltepa"]["asr"]))
async def asr_region59():
    for user in get_user_filter_by_region(region="Qiziltepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qiziltepa"]["shom_iftor"]))
async def shom_region59():
    for user in get_user_filter_by_region(region="Qiziltepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qiziltepa"]["hufton"]))
async def hufton_region59():
    for user in get_user_filter_by_region(region="Qiziltepa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zarafshon"]["tong"]))
async def tong_region60():
    for user in get_user_filter_by_region(region="Zarafshon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zarafshon"]["peshin"]))
async def peshin_region60():
    for user in get_user_filter_by_region(region="Zarafshon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Zarafshon"]["asr"]))
async def asr_region60():
    for user in get_user_filter_by_region(region="Zarafshon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Zarafshon"]["shom_iftor"]))
async def shom_region60():
    for user in get_user_filter_by_region(region="Zarafshon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Zarafshon"]["hufton"]))
async def hufton_region60():
    for user in get_user_filter_by_region(region="Zarafshon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uzunquduq"]["tong"]))
async def tong_region61():
    for user in get_user_filter_by_region(region="Uzunquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uzunquduq"]["peshin"]))
async def peshin_region61():
    for user in get_user_filter_by_region(region="Uzunquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uzunquduq"]["asr"]))
async def asr_region61():
    for user in get_user_filter_by_region(region="Uzunquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uzunquduq"]["shom_iftor"]))
async def shom_region61():
    for user in get_user_filter_by_region(region="Uzunquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uzunquduq"]["hufton"]))
async def hufton_region61():
    for user in get_user_filter_by_region(region="Uzunquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchquduq"]["tong"]))
async def tong_region62():
    for user in get_user_filter_by_region(region="Uchquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchquduq"]["peshin"]))
async def peshin_region62():
    for user in get_user_filter_by_region(region="Uchquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchquduq"]["asr"]))
async def asr_region62():
    for user in get_user_filter_by_region(region="Uchquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchquduq"]["shom_iftor"]))
async def shom_region62():
    for user in get_user_filter_by_region(region="Uchquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Uchquduq"]["hufton"]))
async def hufton_region62():
    for user in get_user_filter_by_region(region="Uchquduq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mingbuloq"]["tong"]))
async def tong_region63():
    for user in get_user_filter_by_region(region="Mingbuloq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mingbuloq"]["peshin"]))
async def peshin_region63():
    for user in get_user_filter_by_region(region="Mingbuloq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mingbuloq"]["asr"]))
async def asr_region63():
    for user in get_user_filter_by_region(region="Mingbuloq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Mingbuloq"]["shom_iftor"]))
async def shom_region63():
    for user in get_user_filter_by_region(region="Mingbuloq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Mingbuloq"]["hufton"]))
async def hufton_region63():
    for user in get_user_filter_by_region(region="Mingbuloq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["To'rtko'l"]["tong"]))
async def tong_region64():
    for user in get_user_filter_by_region(region="To'rtko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["To'rtko'l"]["peshin"]))
async def peshin_region64():
    for user in get_user_filter_by_region(region="To'rtko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["To'rtko'l"]["asr"]))
async def asr_region64():
    for user in get_user_filter_by_region(region="To'rtko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["To'rtko'l"]["shom_iftor"]))
async def shom_region64():
    for user in get_user_filter_by_region(region="To'rtko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["To'rtko'l"]["hufton"]))
async def hufton_region64():
    for user in get_user_filter_by_region(region="To'rtko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Taxtako'pir"]["tong"]))
async def tong_region65():
    for user in get_user_filter_by_region(region="Taxtako'pir"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Taxtako'pir"]["peshin"]))
async def peshin_region65():
    for user in get_user_filter_by_region(region="Taxtako'pir"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Taxtako'pir"]["asr"]))
async def asr_region65():
    for user in get_user_filter_by_region(region="Taxtako'pir"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Taxtako'pir"]["shom_iftor"]))
async def shom_region65():
    for user in get_user_filter_by_region(region="Taxtako'pir"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Taxtako'pir"]["hufton"]))
async def hufton_region65():
    for user in get_user_filter_by_region(region="Taxtako'pir"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimboy"]["tong"]))
async def tong_region66():
    for user in get_user_filter_by_region(region="Chimboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimboy"]["peshin"]))
async def peshin_region66():
    for user in get_user_filter_by_region(region="Chimboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimboy"]["asr"]))
async def asr_region66():
    for user in get_user_filter_by_region(region="Chimboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimboy"]["shom_iftor"]))
async def shom_region66():
    for user in get_user_filter_by_region(region="Chimboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Chimboy"]["hufton"]))
async def hufton_region66():
    for user in get_user_filter_by_region(region="Chimboy"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mo'ynoq"]["tong"]))
async def tong_region67():
    for user in get_user_filter_by_region(region="Mo'ynoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mo'ynoq"]["peshin"]))
async def peshin_region67():
    for user in get_user_filter_by_region(region="Mo'ynoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Mo'ynoq"]["asr"]))
async def asr_region67():
    for user in get_user_filter_by_region(region="Mo'ynoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Mo'ynoq"]["shom_iftor"]))
async def shom_region67():
    for user in get_user_filter_by_region(region="Mo'ynoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Mo'ynoq"]["hufton"]))
async def hufton_region67():
    for user in get_user_filter_by_region(region="Mo'ynoq"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltinko'l"]["tong"]))
async def tong_region68():
    for user in get_user_filter_by_region(region="Oltinko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltinko'l"]["peshin"]))
async def peshin_region68():
    for user in get_user_filter_by_region(region="Oltinko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltinko'l"]["asr"]))
async def asr_region68():
    for user in get_user_filter_by_region(region="Oltinko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltinko'l"]["shom_iftor"]))
async def shom_region68():
    for user in get_user_filter_by_region(region="Oltinko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Oltinko'l"]["hufton"]))
async def hufton_region68():
    for user in get_user_filter_by_region(region="Oltinko'l"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shumanay"]["tong"]))
async def tong_region69():
    for user in get_user_filter_by_region(region="Shumanay"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shumanay"]["peshin"]))
async def peshin_region69():
    for user in get_user_filter_by_region(region="Shumanay"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shumanay"]["asr"]))
async def asr_region69():
    for user in get_user_filter_by_region(region="Shumanay"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shumanay"]["shom_iftor"]))
async def shom_region69():
    for user in get_user_filter_by_region(region="Shumanay"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shumanay"]["hufton"]))
async def hufton_region69():
    for user in get_user_filter_by_region(region="Shumanay"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'ng'irot"]["tong"]))
async def tong_region70():
    for user in get_user_filter_by_region(region="Qo'ng'irot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'ng'irot"]["peshin"]))
async def peshin_region70():
    for user in get_user_filter_by_region(region="Qo'ng'irot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'ng'irot"]["asr"]))
async def asr_region70():
    for user in get_user_filter_by_region(region="Qo'ng'irot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'ng'irot"]["shom_iftor"]))
async def shom_region70():
    for user in get_user_filter_by_region(region="Qo'ng'irot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qo'ng'irot"]["hufton"]))
async def hufton_region70():
    for user in get_user_filter_by_region(region="Qo'ng'irot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urgut"]["tong"]))
async def tong_region71():
    for user in get_user_filter_by_region(region="Urgut"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urgut"]["peshin"]))
async def peshin_region71():
    for user in get_user_filter_by_region(region="Urgut"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Urgut"]["asr"]))
async def asr_region71():
    for user in get_user_filter_by_region(region="Urgut"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Urgut"]["shom_iftor"]))
async def shom_region71():
    for user in get_user_filter_by_region(region="Urgut"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Urgut"]["hufton"]))
async def hufton_region71():
    for user in get_user_filter_by_region(region="Urgut"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buloqboshi"]["tong"]))
async def tong_region72():
    for user in get_user_filter_by_region(region="Buloqboshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buloqboshi"]["peshin"]))
async def peshin_region72():
    for user in get_user_filter_by_region(region="Buloqboshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Buloqboshi"]["asr"]))
async def asr_region72():
    for user in get_user_filter_by_region(region="Buloqboshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Buloqboshi"]["shom_iftor"]))
async def shom_region72():
    for user in get_user_filter_by_region(region="Buloqboshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Buloqboshi"]["hufton"]))
async def hufton_region72():
    for user in get_user_filter_by_region(region="Buloqboshi"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qumqo'rg'on"]["tong"]))
async def tong_region73():
    for user in get_user_filter_by_region(region="Qumqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qumqo'rg'on"]["peshin"]))
async def peshin_region73():
    for user in get_user_filter_by_region(region="Qumqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Qumqo'rg'on"]["asr"]))
async def asr_region73():
    for user in get_user_filter_by_region(region="Qumqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qumqo'rg'on"]["shom_iftor"]))
async def shom_region73():
    for user in get_user_filter_by_region(region="Qumqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Qumqo'rg'on"]["hufton"]))
async def hufton_region73():
    for user in get_user_filter_by_region(region="Qumqo'rg'on"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Boysun"]["tong"]))
async def tong_region74():
    for user in get_user_filter_by_region(region="Boysun"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Boysun"]["peshin"]))
async def peshin_region74():
    for user in get_user_filter_by_region(region="Boysun"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Boysun"]["asr"]))
async def asr_region74():
    for user in get_user_filter_by_region(region="Boysun"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Boysun"]["shom_iftor"]))
async def shom_region74():
    for user in get_user_filter_by_region(region="Boysun"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Boysun"]["hufton"]))
async def hufton_region74():
    for user in get_user_filter_by_region(region="Boysun"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sherobod"]["tong"]))
async def tong_region75():
    for user in get_user_filter_by_region(region="Sherobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sherobod"]["peshin"]))
async def peshin_region75():
    for user in get_user_filter_by_region(region="Sherobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Sherobod"]["asr"]))
async def asr_region75():
    for user in get_user_filter_by_region(region="Sherobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Sherobod"]["shom_iftor"]))
async def shom_region75():
    for user in get_user_filter_by_region(region="Sherobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Sherobod"]["hufton"]))
async def hufton_region75():
    for user in get_user_filter_by_region(region="Sherobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xazorasp"]["tong"]))
async def tong_region76():
    for user in get_user_filter_by_region(region="Xazorasp"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xazorasp"]["peshin"]))
async def peshin_region76():
    for user in get_user_filter_by_region(region="Xazorasp"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xazorasp"]["asr"]))
async def asr_region76():
    for user in get_user_filter_by_region(region="Xazorasp"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xazorasp"]["shom_iftor"]))
async def shom_region76():
    for user in get_user_filter_by_region(region="Xazorasp"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xazorasp"]["hufton"]))
async def hufton_region76():
    for user in get_user_filter_by_region(region="Xazorasp"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonqa"]["tong"]))
async def tong_region77():
    for user in get_user_filter_by_region(region="Xonqa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonqa"]["peshin"]))
async def peshin_region77():
    for user in get_user_filter_by_region(region="Xonqa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonqa"]["asr"]))
async def asr_region77():
    for user in get_user_filter_by_region(region="Xonqa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonqa"]["shom_iftor"]))
async def shom_region77():
    for user in get_user_filter_by_region(region="Xonqa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Xonqa"]["hufton"]))
async def hufton_region77():
    for user in get_user_filter_by_region(region="Xonqa"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Yangibozor"]["tong"]))
async def tong_region78():
    for user in get_user_filter_by_region(region="Yangibozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Yangibozor"]["peshin"]))
async def peshin_region78():
    for user in get_user_filter_by_region(region="Yangibozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Yangibozor"]["asr"]))
async def asr_region78():
    for user in get_user_filter_by_region(region="Yangibozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Yangibozor"]["shom_iftor"]))
async def shom_region78():
    for user in get_user_filter_by_region(region="Yangibozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Yangibozor"]["hufton"]))
async def hufton_region78():
    for user in get_user_filter_by_region(region="Yangibozor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shovot"]["tong"]))
async def tong_region79():
    for user in get_user_filter_by_region(region="Shovot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shovot"]["peshin"]))
async def peshin_region79():
    for user in get_user_filter_by_region(region="Shovot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Shovot"]["asr"]))
async def asr_region79():
    for user in get_user_filter_by_region(region="Shovot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shovot"]["shom_iftor"]))
async def shom_region79():
    for user in get_user_filter_by_region(region="Shovot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Shovot"]["hufton"]))
async def hufton_region79():
    for user in get_user_filter_by_region(region="Shovot"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'uzor"]["tong"]))
async def tong_region80():
    for user in get_user_filter_by_region(region="G'uzor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'uzor"]["peshin"]))
async def peshin_region80():
    for user in get_user_filter_by_region(region="G'uzor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["G'uzor"]["asr"]))
async def asr_region80():
    for user in get_user_filter_by_region(region="G'uzor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["G'uzor"]["shom_iftor"]))
async def shom_region80():
    for user in get_user_filter_by_region(region="G'uzor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["G'uzor"]["hufton"]))
async def hufton_region80():
    for user in get_user_filter_by_region(region="G'uzor"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Koson"]["tong"]))
async def tong_region81():
    for user in get_user_filter_by_region(region="Koson"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Koson"]["peshin"]))
async def peshin_region81():
    for user in get_user_filter_by_region(region="Koson"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Koson"]["asr"]))
async def asr_region81():
    for user in get_user_filter_by_region(region="Koson"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Koson"]["shom_iftor"]))
async def shom_region81():
    for user in get_user_filter_by_region(region="Koson"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Koson"]["hufton"]))
async def hufton_region81():
    for user in get_user_filter_by_region(region="Koson"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tallimarjon"]["tong"]))
async def tong_region82():
    for user in get_user_filter_by_region(region="Tallimarjon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tallimarjon"]["peshin"]))
async def peshin_region82():
    for user in get_user_filter_by_region(region="Tallimarjon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Tallimarjon"]["asr"]))
async def asr_region82():
    for user in get_user_filter_by_region(region="Tallimarjon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Tallimarjon"]["shom_iftor"]))
async def shom_region82():
    for user in get_user_filter_by_region(region="Tallimarjon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Tallimarjon"]["hufton"]))
async def hufton_region82():
    for user in get_user_filter_by_region(region="Tallimarjon"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Muborak"]["tong"]))
async def tong_region83():
    for user in get_user_filter_by_region(region="Muborak"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Muborak"]["peshin"]))
async def peshin_region83():
    for user in get_user_filter_by_region(region="Muborak"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Muborak"]["asr"]))
async def asr_region83():
    for user in get_user_filter_by_region(region="Muborak"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Muborak"]["shom_iftor"]))
async def shom_region83():
    for user in get_user_filter_by_region(region="Muborak"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Muborak"]["hufton"]))
async def hufton_region83():
    for user in get_user_filter_by_region(region="Muborak"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Dushanbe"]["tong"]))
async def tong_region84():
    for user in get_user_filter_by_region(region="Dushanbe"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Dushanbe"]["peshin"]))
async def peshin_region84():
    for user in get_user_filter_by_region(region="Dushanbe"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Dushanbe"]["asr"]))
async def asr_region84():
    for user in get_user_filter_by_region(region="Dushanbe"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Dushanbe"]["shom_iftor"]))
async def shom_region84():
    for user in get_user_filter_by_region(region="Dushanbe"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Dushanbe"]["hufton"]))
async def hufton_region84():
    for user in get_user_filter_by_region(region="Dushanbe"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Ashxabod"]["tong"]))
async def tong_region85():
    for user in get_user_filter_by_region(region="Ashxabod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Ashxabod"]["peshin"]))
async def peshin_region85():
    for user in get_user_filter_by_region(region="Ashxabod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Ashxabod"]["asr"]))
async def asr_region85():
    for user in get_user_filter_by_region(region="Ashxabod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Ashxabod"]["shom_iftor"]))
async def shom_region85():
    for user in get_user_filter_by_region(region="Ashxabod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Ashxabod"]["hufton"]))
async def hufton_region85():
    for user in get_user_filter_by_region(region="Ashxabod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkmanobod"]["tong"]))
async def tong_region86():
    for user in get_user_filter_by_region(region="Turkmanobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkmanobod"]["peshin"]))
async def peshin_region86():
    for user in get_user_filter_by_region(region="Turkmanobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkmanobod"]["asr"]))
async def asr_region86():
    for user in get_user_filter_by_region(region="Turkmanobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkmanobod"]["shom_iftor"]))
async def shom_region86():
    for user in get_user_filter_by_region(region="Turkmanobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Turkmanobod"]["hufton"]))
async def hufton_region86():
    for user in get_user_filter_by_region(region="Turkmanobod"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshhovuz"]["tong"]))
async def tong_region87():
    for user in get_user_filter_by_region(region="Toshhovuz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Bomdod"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshhovuz"]["peshin"]))
async def peshin_region87():
    for user in get_user_filter_by_region(region="Toshhovuz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Peshin"
        )

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshhovuz"]["asr"]))
async def asr_region87():
    for user in get_user_filter_by_region(region="Toshhovuz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Asr"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshhovuz"]["shom_iftor"]))
async def shom_region87():
    for user in get_user_filter_by_region(region="Toshhovuz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Shom"
        )
            

@crontab(create_cron_time(PRAYER_TIMES[0]["Toshhovuz"]["hufton"]))
async def hufton_region87():
    for user in get_user_filter_by_region(region="Toshhovuz"):
        await send_message_prayer_on_time(
            user = user,
            prayer = "Hufton"
        )