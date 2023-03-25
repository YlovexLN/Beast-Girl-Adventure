from modules.get_mod import get_mod
from modules.mod_list import mod_list

def main():
    mod_info = get_mod()
    filtered_mod_info = mod_list(mod_info)
    
    # 在这里对 filtered_mod_info 进行处理，比如输出到文件或显示在屏幕上等

if __name__ == '__main__':
    main()
