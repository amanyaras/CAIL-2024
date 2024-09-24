import json


def _convert2sharegpt_format(path: str, save_path: str = "./dataset/cail2024_司法考试-初赛阶段-数据集/format_data") -> None:
    """
    path: 训练集路径 xxx.json
    save_path: 保存路径 xxx.json
    """
    # 获取数据
    with open(path, 'r', encoding='utf-8') as R:
        dataset = json.load(R)

    # 格式转换
    sv_lst = [{"id": "train_{}".format(str(idx)), "conversations": [{"from": "human", "value": cnt["statement"] + "\n" + "\n".join([k + "." +  v for k, v in cnt["option_list"].items()])}, {"from": "gpt", "value": "".join(cnt["answer"])}]} for idx, cnt in enumerate(dataset)]

    # 保存数据
    with open(save_path, "w", encoding='utf-8') as W:
        json.dump(sv_lst, W, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    _convert2sharegpt_format("dataset/cail2024_司法考试-初赛阶段-数据集/train.json", "dataset/cail2024_司法考试-初赛阶段-数据集/format_data/sharegpt_format_train.json")
    pass
