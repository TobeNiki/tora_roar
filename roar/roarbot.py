
from bot.config import load_token
import discord
from whisper_module.transcription import whisper_transcribe
from pydub import AudioSegment

#intents = discord.Intents().all()
bot = discord.Bot()

Token= load_token()


@bot.command()
async def start_record(ctx:discord.ApplicationContext):
    # コマンドを使用したユーザーのボイスチャンネルに接続
    try:
       vc = await ctx.author.voice.channel.connect()
       await ctx.respond("録音開始...")
    except AttributeError:
       await ctx.respond("ボイスチャンネルに入ってください。")
       return
    # 録音開始。mp3で帰ってくる。wavだとなぜか壊れる。
    ctx.voice_client.start_recording(discord.sinks.MP3Sink(), finished_callback_local, ctx)


async def finished_callback(sink:discord.sinks.MP3Sink, ctx:discord.ApplicationContext):
    # 録音したユーザーの音声を取り出す
    recorded_users = [
        f"<@{user_id}>"
        for user_id, audio in sink.audio_data.items()
    ]
    # discordにファイル形式で送信。拡張子はmp3。
    files = [discord.File(audio.file, f"{user_id}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]
    
    await ctx.channel.send(f"録音終了! 音声ファイルはこちら! {', '.join(recorded_users)}.", files=files) 

async def finished_callback_local(sink:discord.sinks.MP3Sink, ctx:discord.ApplicationContext):
    for user_id, audio in sink.audio_data.items():
        print(type(audio.file))#io.BytesIO
        voice = AudioSegment.from_file(audio.file, format='mp3')
        voiceText = whisper_transcribe(voice)
        

    await ctx.channel.send(f"[Roar]:<@{user_id}> --> {voiceText}")

@bot.command()
async def stop_recording(ctx:discord.ApplicationContext):
    # 録音停止
    ctx.voice_client.stop_recording()
    await ctx.respond("録音終了!")
    await ctx.voice_client.disconnect()


bot.run(Token)