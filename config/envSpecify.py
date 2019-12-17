# -*- coding: utf-8 -
import os

cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
config_path = os.path.join(cur_path, 'config')
env_info_path = os.path.join(config_path, 'env.yaml')


def env_specify(env):
    env_path = os.path.join(config_path, 'env')

    if env == "Dev" or "St":
        env_info = os.path.join(env_path, "env" + env + ".yaml")
        file = open(env_info, 'r', encoding='utf-8').read()
        with open(env_info_path, 'w', encoding='utf-8') as env_file:
            env_file.write(file)
        env_file.close()
    else:
        print("环境参数错误，请输入Dev或St")
        quit()
