from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path="temp.wav"):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')  # WAV format
    return output_audio_path
