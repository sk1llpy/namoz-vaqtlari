def START(name: str):
    text = f"""<b>Salom {name}, Namoz vaqtlari botiga xush kelibsiz 👋</b>
    
<i>Kerakli bo'limni tanlang 👇</i>"""
    
    return text

def PRAYER_TIME(
        date: str,
        weekday: str,
        hijri_date: dict,
        times: dict,
        region: str
):
    text = f"""<b>Xudud: {region} 📍</b>

<b>📅 Sana: {weekday} ({date.split(',')[0] if date.split(',')[0] else date})
☪️ {hijri_date['month'].capitalize()}, {hijri_date['day']}</b>

<b>🧎 Namoz vaqtlari:</b>
 — <i>⏰ Tong (saxar) - {times['tong_saharlik']}
 — ⏰ Quyosh - {times['quyosh']}
 — ⏰ Peshin - {times['peshin']}
 — ⏰ Asr - {times['asr']}
 — ⏰ Shom (iftor) - {times['shom_iftor']}
 — ⏰ Xufton - {times['hufton']}</i>
  
<b>🌐 Manba: islom.uz</b>
<i>ℹ️ Eslatma: Ushbu Telegram Botdagi Namoz vaqtlaridan ko'ra sizga yaqin atrofingizda joylashgan Jome Masjidlarning vaqtlariga e'tibor qaratganingiz afzalroq, chunki kichik farqlar bo'lishi mumkin.</i>"""
    
    return text


def PRAYER_TIME_WEEKLY(
    data: dict
):
    text = f"<b>Xudud: {data[0]['region']} 📍</b>\n\n"

    for day in data:
        times = day['times']
        text += f"""<b>📅 Sana: {day['weekday']} ({day['date'].split(',')[0] if day['date'].split(',')[0] else day['date']})
☪️ {day['hijri_date']['month'].capitalize()}, {day['hijri_date']['day']}</b>

<b>🧎 Namoz vaqtlari:</b>
 — <i>⏰ Tong (saxar) - {times['tong_saharlik']}
 — ⏰ Quyosh - {times['quyosh']}
 — ⏰ Peshin - {times['peshin']}
 — ⏰ Asr - {times['asr']}
 — ⏰ Shom (iftor) - {times['shom_iftor']}
 — ⏰ Xufton - {times['hufton']}</i>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"""
    
    text += """<b>🌐 Manba: islom.uz</b>
<i>ℹ️ Eslatma: Ushbu Telegram Botdagi Namoz vaqtlaridan ko'ra sizga yaqin atrofingizda joylashgan Jome Masjidlarning vaqtlariga e'tibor qaratganingiz afzalroq, chunki kichik farqlar bo'lishi mumkin.</i>"""

    return text