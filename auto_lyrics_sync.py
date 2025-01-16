from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import math

def generate_timestamps(audio_file, lyrics_file, silence_thresh=-50, min_silence_len=100):
    # 加载音频文件
    audio = AudioSegment.from_file(audio_file)
    
    # 检测非静音片段
    nonsilent_ranges = detect_nonsilent(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )
    
    # 读取歌词
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lyrics = [line.strip() for line in f if line.strip()]
    
    # 生成时间戳
    timestamps = []
    for i, (start, end) in enumerate(nonsilent_ranges):
        if i >= len(lyrics):
            break
            
        # 转换为分钟:秒.毫秒格式
        start_time = start / 1000.0
        minutes = math.floor(start_time / 60)
        seconds = math.floor(start_time % 60)
        milliseconds = math.floor((start_time - math.floor(start_time)) * 100)
        
        timestamps.append(f"[{minutes:02d}:{seconds:02d}.{milliseconds:02d}] {lyrics[i]}")
    
    # 保存结果
    output_file = lyrics_file.replace('.txt', '_synced.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(timestamps))
    
    print(f"生成的时间戳已保存到 {output_file}")

if __name__ == "__main__":
    audio_file = "NSwitchRobot - Stay Alive.mp3"
    lyrics_file = "Stay Alive lyrics.txt"
    generate_timestamps(audio_file, lyrics_file)