import yaml
import sys

def load_token()->str:
    """
    discord botのtoken情報をymlファイルから取得します.
    取得失敗した場合はプログラムを終了します
    """
    try:
        with open('./bot/config.yml') as config_file:
            config = yaml.safe_load(config_file)
            return config['DISCORD_BOT_TOKEN']
    except Exception as err:
        print('Exception occurred while loading YAML...', file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)

