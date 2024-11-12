import os
import json as j
import requests
import time as t
import sys as s
import datetime

option = 0
running = True
config = {}
GenerateErrorReport = False

DefaultConfig = '''
{
    "GenerateErrorReport": 0,
    "API_Interface": "https://api.stripe.com/v1/customers",
    "header": [
        {"Authorization":"Basic cmtfbGl2ZV81MUw5c3JLQ29GamtETjR4UGtvdEs2V0dHUHFmd2tnd3RFNkkxcTFURTlrdktzZ0s3SlQ5Mk5oaUFHeGpKeDQ0ejdHZnBzU1hZNmtpTVkyTTFWWkhFajJZVjAwbjRPS3pUSlg6"}
    ]
}
'''

headers = [{"Authorization": "Basic cmtfbGl2ZV81MUw5c3JLQ29GamtETjR4UGtvdEs2V0dHUHFmd2tnd3RFNkkxcTFURTlrdktzZ0s3SlQ5Mk5oaUFHeGpKeDQ0ejdHZnBzU1hZNmtpTVkyTTFWWkhFajJZVjAwbjRPS3pUSlg6"}]

def GetConfig():
    global headers,GenerateErrorReport,config
    if os.path.exists(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\program_config.json"):
        with open(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\program_config.json","r",encoding="utf-8") as f:
            config = j.load(f)
            headers = config["header"][0]
    else:
        with open(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\program_config.json","w",encoding="utf-8") as f:
            f.write(DefaultConfig)

    if config == {}:
        GenerateErrorReport = True
    else:
        GenerateErrorReport = config["GenerateErrorReport"]

os.system("title GreenHub破解程序V1.0  By Unknown_name")
GetConfig()
try:
    with open(os.getenv("appdata") + "\\GreenHub\\config.json", 'r',encoding="utf-8") as f:
        data = j.load(f)
except FileNotFoundError as err:
    if GenerateErrorReport == 1:
        print("\033[31m未找到config.json文件，请打开GreenHub再关闭。（错误代号：00）\033[0m")
    else:
        if os.path.exists(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder") == False:
            os.chdir(os.path.split(os.path.realpath(s.argv[0]))[0])
            os.makedirs("error_info_folder")
        now = datetime.datetime.now()
        argument = (os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder\\" + "error_info_" + now.strftime("%H:%M:%S").replace(":","-") + ".txt")[2::].replace(":","-")
        print("\033[31m未找到config.json文件，请打开GreenHub再关闭。错误信息已导出至" + argument + "  |  （错误代号：00）\033[0m")
        with open(fr"{argument}","r",encoding="utf-8") as f:
            f.write("GreenHub Crack Error Report\n")
            f.write("-------------------------------\n")
            f.write(str(err))
    t.sleep(3)
    running = False

while running:
    os.system("cls")
    print("\033[33m GreenHub破解    GreenHub Crack    By Unknown_name  \033[0m")
    print("\033[32m---------------------------------------------------\033[0m")
    print("\033[44m           1.关闭GreenHub                           \033[0m")
    print("\033[45m           2.伪破解（增加可用时间）                 \033[0m")
    print("\033[46m           3.真破解（生成序列号，需要网络）         \033[0m")
    print("\033[41m           4.恢复默认设置                           \033[0m")
    print("\033[42m           5.刷新配置                               \033[0m")
    print("\033[40m           6.退出此程序                             \033[0m")
    print("\033[32m---------------------------------------------------\033[0m")
    try:
        option = int(input("\033[33m请选择: \033[0m"))
    except ValueError:
        print("\033[31m输入值无效\033[0m")
        t.sleep(1)
        option = 0
    except EOFError:
        print("\033[31m用户提前结束输入\033[0m")
        t.sleep(1)
        option = 0
    match option:
        case 1:
            print("\033[33m正在关闭\033[0m")
            os.system('taskkill /f /im greenhub.exe')
            t.sleep(2)
        case 2:
            print("\033[34m当前值：剩余",data["today-use-minute"]["minutes"],"分钟\033[0m")
            time = input("\033[33m请输入新的值：\033[0m")
            try:
                data["today-use-minute"]["minutes"] = time
            except:
                print("\033[31m数值错误\033[0m")
            with open(os.getenv("appdata") + "\\GreenHub\\config.json", 'w',encoding="utf-8") as f:
                j.dump(data,f)
            print("\033[33m写入成功！（GreenHub重启后生效）\033[0m")
            t.sleep(2)
        case 3:
            print("\033[33m正在获取......\033[0m")
            try:
                result = requests.get(config["API_Interface"], headers=headers).json()
            except requests.exceptions.ConnectionError as err:
                if GenerateErrorReport == 1:
                    now = datetime.datetime.now()
                    argument = (os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder\\" + "error_info_" + now.strftime("%H:%M:%S").replace(":","-") + ".txt")[2::].replace(":","-")
                    print("\033[31m获取时发生严重错误！错误信息已导出至" + argument + "  |  （错误代号：01）\033[0m")
                    if os.path.exists(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder") == False:
                        os.chdir(os.path.split(os.path.realpath(s.argv[0]))[0])
                        os.makedirs("error_info_folder")
                    with open(fr"{argument}",'w',encoding="utf-8") as f:
                        f.write("GreenHub Crack Error Report\n")
                        f.write("-------------------------------\n")
                        f.write(str(err))
                else:
                    print("\033[31m获取时发生严重错误！错误信息：" + str(err) + "  |  （错误代号：01）\033[0m")
                os.system("pause")
                continue
            try:
                license_code = [customer['metadata']['license_code'] for customer in result['data']]
            except Exception as err:
                if GenerateErrorReport == 1:
                    now = datetime.datetime.now()
                    argument = (os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder\\" + "error_info_" + now.strftime("%H:%M:%S").replace(":","-") + ".txt")[2::].replace(":","-")
                    print("\033[31m获取时发生错误：配置文件请求头错误（错误代号：02），错误信息已导出至" + argument + "\033[0m")
                    if os.path.exists(os.path.split(os.path.realpath(s.argv[0]))[0] + "\\error_info_folder") == False:
                        os.chdir(os.path.split(os.path.realpath(s.argv[0]))[0])
                        os.makedirs("error_info_folder")
                    with open(fr"{argument}",'w',encoding="utf-8") as f:
                        f.write("GreenHub Crack Error Report\n")
                        f.write("-------------------------------\n")
                        f.write(str(err))
                else:
                    print("\033[31m获取时发生错误：配置文件请求头错误（错误代号：02）\033[0m")
                os.system("pause")
                continue
            print("\033[33m---------------------------------------------------\033[0m")
            for i in range(len(license_code)):
                print("\033[34m密钥"+str(i+1)+"："+license_code[i],"\033[0m")
            print("\033[33m---------------------------------------------------\033[0m")
            print("\033[33m生成密钥完成！\033[0m")
            os.system("pause")
        case 4:
            yn = input("\033[31m您确认要执行此操作吗？（Y/N）\033[0m")
            if yn == "Y" or yn == "y":
                print("\033[33m正在恢复默认\033[0m")
                os.system('taskkill /f /im greenhub.exe')
                os.system('del "' + os.getenv("appdata") + "\\GreenHub\\config.json"+'"')
                print("\033[32m恢复默认完成！此程序将在5秒后关闭，切记要先打开GreenHub再打开此程序！\033[0m")
                t.sleep(5)
                running = False
        case 5:
            print("\033[33m正在刷新配置\033[0m")
            GetConfig()
            print("\033[33m成功！\033[0m")
            os.system("pause")
        case 6:
            running = False