import os


# 生成数据列表
# def get_data_list(audio_path, list_path):
#     sound_sum = 0
#     audios = os.listdir(audio_path)
#     os.makedirs(list_path, exist_ok=True)
#     f_train = open(os.path.join(list_path, 'train_list.txt'), 'w', encoding='utf-8')
#     f_test = open(os.path.join(list_path, 'test_list.txt'), 'w', encoding='utf-8')
#     f_label = open(os.path.join(list_path, 'label_list.txt'), 'w', encoding='utf-8')
#
#     for i in range(len(audios)):
#         f_label.write(f'{audios[i]}\n')
#         sounds = os.listdir(os.path.join(audio_path, audios[i]))
#         for sound in sounds:
#             sound_path = os.path.join(audio_path, audios[i], sound).replace('\\', '/')
#             if sound_sum % 10 == 0:
#                 f_test.write(f'{sound_path}\t{i}\n')
#             else:
#                 f_train.write(f'{sound_path}\t{i}\n')
#             sound_sum += 1
#         print(f"Audio：{i + 1}/{len(audios)}")
#     f_label.close()
#     f_test.close()
#     f_train.close()
#
#
# # 下载数据方式，执行：./tools/download_3dspeaker_data.sh
# # 生成生成方言数据列表
# def get_language_identification_data_list(audio_path, list_path):
#     labels_dict = {0: 'angry', 3: 'neutral',
#                    4: 'sad', 2: 'happy',
#                    5: 'surprise', 1: 'fear'}
#
#     with open(os.path.join(list_path, 'train_list.txt'), 'w', encoding='utf-8') as f:
#         train_dir = os.path.join(audio_path, 'train')
#         for root, dirs, files in os.walk(train_dir):
#             for file in files:
#                 if not file.endswith('.wav'): continue
#                 label = int(file.split('_')[-1].replace('.wav', '')[-2:])
#                 file = os.path.join(root, file)
#                 f.write(f'{file}\t{label}\n')
#
#     with open(os.path.join(list_path, 'test_list.txt'), 'w', encoding='utf-8') as f:
#         test_dir = os.path.join(audio_path, 'test')
#         for root, dirs, files in os.walk(test_dir):
#             for file in files:
#                 if not file.endswith('.wav'): continue
#                 label = file.split('-')[1]
#                 file = os.path.join(root, file)
#                 f.write(f'{file}\t{label}\n')
#
#     with open(os.path.join(list_path, 'label_list.txt'), 'w', encoding='utf-8') as f:
#         for i in range(len(labels_dict)):
#             f.write(f'{labels_dict[i]}\n')


# 创建UrbanSound8K数据列表
def create_sound_list(audio_path, metadata_path, list_path):
    # 情绪到数字标签的映射
    labels_dict = {
        "angry": 0,
        "fear": 1,
        "happy": 2,
        "sad": 3,
        "surprise": 4,
        "neutral": 5,
    }
    sound_sum = 0

    # 确保输出目录存在
    os.makedirs(list_path, exist_ok=True)

    # 打开文件准备写入
    with open(
        os.path.join(list_path, "train_list.txt"), "w", encoding="utf-8"
    ) as f_train, open(
        os.path.join(list_path, "test_list.txt"), "w", encoding="utf-8"
    ) as f_test, open(
        os.path.join(list_path, "label_list.txt"), "w", encoding="utf-8"
    ) as f_label:

        with open(metadata_path, "r", encoding="utf-8") as f_meta:
            for line in f_meta:
                filename = line.strip()
                if not filename:
                    continue
                # 分割文件名以获取情绪标签
                parts = filename.split("-")
                if len(parts) < 2:
                    continue  # 如果分割后的部分小于2，跳过这一行

                emotion = parts[1]  # 情绪是第二部分
                if emotion not in labels_dict:
                    continue  # 如果情绪不在字典中，跳过

                label = labels_dict[emotion]  # 获取数字标签
                sound_path = os.path.join(audio_path, filename)

                # 决定将样本写入训练集或测试集
                if sound_sum % 10 == 0:
                    f_test.write(f"{sound_path}\t{label}\n")
                else:
                    f_train.write(f"{sound_path}\t{label}\n")
                sound_sum += 1

        # 写入所有情绪标签到 label_list.txt
        for emotion in labels_dict.keys():
            f_label.write(f"{emotion}\n")


if __name__ == "__main__":
    # get_data_list('dataset/audio', 'dataset')
    # 生成生成方言数据列表
    # get_language_identification_data_list(audio_path='dataset/language',
    #                                       list_path='dataset/')
    # 创建UrbanSound8K数据列表
    create_sound_list(
        audio_path="Emotional_speech_recognition-Pytorch/dataset/audio",
        metadata_path="Emotional_speech_recognition-Pytorch/dataset/Sound.csv",
        list_path="Emotional_speech_recognition-Pytorch/dataset",
    )
