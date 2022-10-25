
import whisper
from typing import Any
import numpy as np

MODEL_TYPE = "small"

model = whisper.load_model(MODEL_TYPE)


def whisper_transcribe(buf:Any, verbose:bool = False, lang:str = "ja", translate:bool = False)->str:
    """
    whisperのモデルを使用して音声からの文字お越しを行うメソッドです\n
    Paramter:\n
        buf : 音声データを持つ変数 ここではpydubのAudioSegment.from_file(audio.file, format='mp3')の戻り値を期待しています\n
        verbose: 途中の処理過程を出力するか デフォルトFalse\n
        lang: 文字お越しの言語を指定します, whisperは冒頭30secondで言語判定を行いますが、
              ここで言語を指定するとこれをパスすることが可能で処理速度の向上を期待できます デフォルトja\n
        translate: 文字お越しに加え英語への翻訳を行います, デフォルトをfalse\n
    Return:\n
        str 文字お越し結果のテキストのみを返却します 
    """
    data = np.array(buf.get_array_of_samples(), dtype=np.int16).flatten().astype(np.float32) / 32768.0
    if translate:
        result = model.transcribe(data, verbose=verbose, language=lang, task="translate")
    else:
        result = model.transcribe(data, verbose=verbose, language=lang)
    return result["text"]