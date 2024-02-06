import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime
import random
os.system('clear')
print('BOT ONLINE BY AN ORIN !')
bot_token = '6666664448:AAEx6lHnueco07PyTOUaI1JO27RqUpiRUQM' 
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '5350713349'
namebot = "@sp_ctoolbot"
ten_admin = "An Orin"
full_ten_admin = "Vũ Xuân An"

cookie = "datr=nSB_ZL1h13iUMgL7OIPZUYfj;sb=nSB_ZLKFHfHQpf-4QbdBTr-Z;vpd=v1%3B698x360x2;locale=vi_VN;fr=0SdLkQqwsUPVESxvz.AWVFy76qd2Wnqd0dE6S77IHs5jE.BlcJPa.IU.AAA.0.0.BlpLT0.AWXK2bfdHjs;c_user=100093226561215;xs=24%3AodLlG3s_UiQ6pQ%3A2%3A1705293045%3A-1%3A6284;fbl_cs=AhA12%2BkPZY%2BsNyb27XAZ0usAGHEvYXFGdGlXWmdaVnZLVVVva1kvPWJDWA;fbl_ci=202767618850805;m_page_voice=100093226561215;wl_cbv=v2%3Bclient_version%3A2393%3Btimestamp%3A1705400786;fbl_st=101428527%3BT%3A28423346;dpr=2;usida=eyJ2ZXIiOjEsImlkIjoiQXM3Y25wMTVqNTJhNyIsInRpbWUiOjE3MDU0MDA4MjF9;wd=980x1900;"

def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['getkey'])
def startkey(message):
    bot.reply_to(message, text='VUI LÒNG ĐỢI TRONG GIÂY LÁT!')
    key = "anorin_" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    key = "https://keyvip24h.dev/giaodien/key.php?key=" + key
    api_token = '63de72dfe0d2c630a44133e2'
    url = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key}').json()
    url_key = url['shortenedUrl']
    text = f'''
- LINK LẤY KEY {TimeStamp()} LÀ: {url_key} -
- KHI LẤY KEY XONG, DÙNG LỆNH /key <key> ĐỂ TIẾP TỤC -
    '''
    bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
def key(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP KEY.')
        return
        

    user_id = message.from_user.id

    key = message.text.split()[1]
    username = message.from_user.username
    expected_key = "anorin_" + str(int(message.from_user.id) * int(datetime.date.today().day) - 12666)
    if key == expected_key:
        bot.reply_to(message, 'KEY HỢP LỆ. BẠN ĐÃ ĐƯỢC PHÉP SỬ DỤNG LỆNH')
        fi = open(f'./user/{datetime.date.today().day}/{user_id}.txt',"w")
        fi.write("")
        fi.close()
    else:
        bot.reply_to(message, 'KEY KHÔNG HỢP LỆ.')

#Lệnh Spam
@bot.message_handler(commands=['spam'])
def spam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
      if not (int(lap) > 0 and int(lap) <= 40):
        bot.reply_to(message,"Vui lòng spam trong khoảng 1-40. Nếu nhiều hơn mua vip để sài :))")
        return
    else:
      bot.reply_to(message,"Sai dữ kiện !!!")
      return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0777374145"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Spam cái đầu buồi tao huhu")
        return

    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f'Gửi Yêu Cầu Tấn Công Thành Công \n+ Bot : {namebot} \n+ Số Tấn Công : [ {phone_number} ]\n+ Lặp lại : {lap}\n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')
    
#Lệnh View_str
@bot.message_handler(commands=['view_str'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP LINK STORY CÔNG KHAI /view_str {link story công khai} ')
        return
        
    
    
        

    url_str = message.text.split()[1] 
        

    file_path = os.path.join(os.getcwd(), "viewstory.py")
    process = subprocess.Popen(["python", file_path, url_str, cookie])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Buff View Thành Công  \n+ Bot : {namebot} \n+ Link video : [ {url_str} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')
    
#Lệnh followfb
@bot.message_handler(commands=['followfb'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP LINK ID FACEBOOK /followfb {Link ID FB} ')
        return
    
    
        

    id = message.text.split()[1] 
        

    file_path = os.path.join(os.getcwd(), "buff_follow.py")
    process = subprocess.Popen(["python", file_path, id, cookie])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Buff Follow Thành Công  \n+ Bot : {namebot} \n+ ID Facebook: [ {id} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')

#Lệnh Buffmember
cookie = "datr=nSB_ZL1h13iUMgL7OIPZUYfj;sb=nSB_ZLKFHfHQpf-4QbdBTr-Z;vpd=v1%3B698x360x2;locale=vi_VN;fr=0SdLkQqwsUPVESxvz.AWVFy76qd2Wnqd0dE6S77IHs5jE.BlcJPa.IU.AAA.0.0.BlpLT0.AWXK2bfdHjs;c_user=100093226561215;xs=24%3AodLlG3s_UiQ6pQ%3A2%3A1705293045%3A-1%3A6284;fbl_cs=AhA12%2BkPZY%2BsNyb27XAZ0usAGHEvYXFGdGlXWmdaVnZLVVVva1kvPWJDWA;fbl_ci=202767618850805;m_page_voice=100093226561215;wl_cbv=v2%3Bclient_version%3A2393%3Btimestamp%3A1705400786;fbl_st=101428527%3BT%3A28423346;dpr=2;usida=eyJ2ZXIiOjEsImlkIjoiQXM3Y25wMTVqNTJhNyIsInRpbWUiOjE3MDU0MDA4MjF9;wd=980x1900;"
@bot.message_handler(commands=['buffmember'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP LINK GROUP /buffmember {Link Nhập Group FB} ')
        return
    
    
        

    linkgr = message.text.split()[1] 
        

    file_path = os.path.join(os.getcwd(), "buff_tv.py")
    process = subprocess.Popen(["python", file_path, linkgr, cookie])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Buff Thành Viên Thành Công  \n+ Bot : {namebot} \n+ Link Group: [ {linkgr} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')
    
    
#Lệnh view_str_feeling
@bot.message_handler(commands=['view_str_feeling'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP LINK STORY /view_str_vip_feeling {Link Nhập Story FB} ')
        return
    
    
        

    linkgr = message.text.split()[1] 
    cx = message.text.split()[1] 
    
        

    file_path = os.path.join(os.getcwd(), "likepro5.py")
    process = subprocess.Popen(["python", file_path, linkgr, cookie,cx])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Buff Cảm Xúc Story Thành Công  \n+ Bot : {namebot} \n+ Link Story: [ {linkgr} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')
    
    #Lệnh spamcmt
@bot.message_handler(commands=['spamcmt'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP ID BÀI VIẾT /spamcmt {Nhập ID FB} ')
        return
    
    
        

    __post = message.text.split()[1] 
    
        

    file_path = os.path.join(os.getcwd(), "cmtpro5.py")
    process = subprocess.Popen(["python", file_path, __post])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Spam CMT Thành Công  \n+ Bot : {namebot} \n+ ID FB: [ {__post} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')
    
#Lệnh likes
@bot.message_handler(commands=['likes'])
def view_str(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
      bot.reply_to(message, 'Dùng /getkey để lấy key và dùng /key để nhập key hôm nay')
      return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP ID BÀI VIẾT /likes {Nhập ID FB} ')
        return
    
    
        

    __post = message.text.split()[1] 
    
        

    file_path = os.path.join(os.getcwd(), "likes.py")
    process = subprocess.Popen(["python", file_path, __post])
    processes.append(process)
    bot.reply_to(message, f' Gửi Yêu Cầu Buff Like Bài Viết Thành Công  \n+ Bot : {namebot} \n+ ID FB: [ {__post} ] \n+ Chủ sở hữu 👑: {ten_admin} \n+ {full_ten_admin} ({ten_admin})')

#Lệnh khởi đầu để xem lệnh
@bot.message_handler(commands=['help'])
def handle_start(message):
  video = random.choice(["https://keyvip24h.dev/video_random/1.mp4", "https://keyvip24h.dev/video_random/2.mp4", "https://keyvip24h.dev/video_random/3.mp4", "https://keyvip24h.dev/video_random/4.mp4", "https://keyvip24h.dev/video_random/5.mp4", "https://keyvip24h.dev/video_random/6.mp4", "https://keyvip24h.dev/video_random/7.mp4", "https://keyvip24h.dev/video_random/8.mp4", "https://keyvip24h.dev/video_random/9.mp4", "https://keyvip24h.dev/video_random/10.mp4", "https://keyvip24h.dev/video_random/11.mp4", "https://keyvip24h.dev/video_random/12.mp4", "https://keyvip24h.dev/video_random/13.mp4", "https://keyvip24h.dev/video_random/14.mp4"])
  help_text = '''
⭐Danh sách lệnh⭐
+ /menu - Để xem lệnh
+ /how - Để xem lệnh bot tool Tremux
'''
  bot.send_video(message.chat.id, video=video, caption=help_text, reply_to_message_id=message.message_id, supports_streaming=True) 
  
 
 
@bot.message_handler(commands=['how'])
def help(message):
    how_text = '''
Chào mừng Bạn đến BOT Tự Động !
nơi giúp bạn tự động kiếm lệnh chạy tool và setup 
sau đây là các lệnh để giúp bạn bên dưới 👇 
/taitool 
/setuptool 
/info 
/muakey
'''
    bot.reply_to(message, how_text)
    
@bot.message_handler(commands=['menu'])
def menu(message):
    menu_text = '''
Danh sách lệnh:

/getkey: Lấy key để sử dụng các lệnh.

/key {key}: Kiểm tra key và xác nhận quyền sử dụng các lệnh.

/spam {số điện thoại} {so lan}: Gửi tin nhắn SMS Call.

/view_str {Buff View Story} Tăng lượt xem story fb.

/followfb {Buff Follow} Tăng Người Theo Dõi Fb

/buffmember {Buff Member} Tăng người tham Gia Vào Group fb

/view_str_feeling {Buff Story} Tăng Cảm Xúc Story + Xem Story

/spamcmt {Spam CMT} Spam CMT Bằng Pro5

/likes {Like Bài Viết} Thả Cảm Xúc Like Bài Viết

/mua {Mua Gói} Thành Viên Vip
'''
    bot.reply_to(message, menu_text)
    
@bot.message_handler(commands=['taitool'])
def taitool(message):
    taitool_text = '''
- CTOOL Đã Update Lên Phiên Bản v3.4
- Vượt Trội Hơn So Với Bản V3.3
+ Và Đã Được Sửa Lại Thông Tin Banner Của Admin nhé 
+ Và Các Chế Độ Của Chúng Ta Khi Vào Sẽ Ko Bị Vào Sai Chế Độ Nhé 
+ Và Đã Gộp Hết Tool Vào Một Link Tải Tool Nhé Mọi Người 
=> Link Tool:
https://keyvip24h.dev/taitool/


Cảm Ơn Mọi Người Đã Đồng Hành Cùng Với Chúng Tôi Trong Thời Gian Qua.
                                   
~ CTool X Team ~
'''
    bot.reply_to(message, taitool_text)


@bot.message_handler(commands=['setuptool'])
def setuptool(message):
    setuptool_text = '''
👉 Link Setup Tại Đây: https://anorintool.blogspot.com/2022/04/blog-post_9.html?m=1
'''
    bot.reply_to(message, setuptool_text)
    

@bot.message_handler(commands=['info'])
def info(message):
    info_text = '''
👉 Liên Hệ Cho Tôi Tại Đây: https://instabio.cc/4091605gRL8NS
'''
    bot.reply_to(message, info_text)


@bot.message_handler(commands=['muakey'])
def muakey(message):
    muakey_text = '''
👉 Mua Key Tại: https://keyvip24h.dev/
'''
    bot.reply_to(message, muakey_text)
    
 
#Lệnh startvip
@bot.message_handler(commands=['startvip'])
def startvip(message):
    reply_text = 'Bạn Chưa Mua Gói Thành Viên VIP Vui Lòng Xem Lệnh {/mua}'
    bot.reply_to(message, reply_text)
   


@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    idvip = message.text.split(" ")[1]
    ngay = message.text.split(" ")[2]
    hethan = message.text.split(" ")[3]
    fii = open(f"./vip/{idvip}.txt","w")
    fii.write(f"{ngay}|{hethan}")
    bot.reply_to(message, f'Thêm Thành Công {idvip} Làm Vip')

# mua
@bot.message_handler(commands=['mua'])
def mua(message):
    reply_text = 'Giá cả của các gói dịch vụ tất cả đều chát admin:\n\n'
    reply_text += '- Gói /spam: 5k/1 tuần\n'
    reply_text += '- Gói /spam: 20k/1 tháng\n'
    reply_text += '- Gói /spam: 300k/ vĩnh viễn\n'
    bot.reply_to(message, reply_text)


 

bot.polling()
