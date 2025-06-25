import shutil
import os
def beifen(a,b):#a为文件,b为目录，文件夹
    try :
        if os.path.isifile(a):#为检测到文件
            print('有文件，开始备份ing----')
            shutil.copy2(a,b)#copy2可以备份文件详细内容！！！【震惊脸】
        elif os.path.isdir(a):#用户想备份文件夹，目录等等
            print('哈哈嗨！开始备份您の目录or文件夹')
            # 用 shutdown.copytree() 整个拷贝过去，包括里面的子文件夹
            # 会自动在目标路径下新建一个和原来一样名字的文件夹
            shutil.copytree(a, os.path.join(b, os.path.basename(a)))
        else:
            raise FileNotFoundError(f'您输入的是空气吗！！！！')
    except Exception as e:
        print(f'错误{e}')
        exit(1)#非0退出，为终止程序
#主循环入口
if __name__=='__main__':
    a=input('输入文件').strip()
    b=input('输入目录').strip()
             # 👇检查目标目录存在不（万一没有，咱就自己创建一个）
    if not os.path.exists(b):
        print("⚠️ 检测到目标目录不存在，自动创建中...")
        # os.makedirs() 可以初步建好高层目录
        #存在_ok=True → 如果目录目录目前存在，也不报错，稳得了
        os.makedirs(b, exist_ok=True)
    beifen(a,b)
    print("🎉备份成功！建议奖励自己一杯奶茶！🥤")
            
    

            
        
