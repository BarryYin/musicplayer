import time

def adjust_lyrics(lyrics_file):
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("歌词调整工具")
    print("按回车键记录当前时间点，输入q退出")
    
    timestamps = []
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
            
        print(f"\n当前歌词: {line.strip()}")
        input("准备好后按回车开始播放...")
        start_time = time.time()
        input("当歌词结束时按回车...")
        end_time = time.time()
        
        duration = end_time - start_time
        timestamps.append((i, duration))
        
        print(f"记录完成: {duration:.2f}秒")
        
        if input("继续下一句？(y/n): ").lower() != 'y':
            break
    
    print("\n生成的时间戳：")
    current_time = 0.0
    for i, (line_num, duration) in enumerate(timestamps):
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        milliseconds = int((current_time - int(current_time)) * 100)
        print(f"[{minutes:02d}:{seconds:02d}.{milliseconds:02d}] {lines[line_num].strip()}")
        current_time += duration

if __name__ == "__main__":
    adjust_lyrics("Stay Alive lyrics.txt")