class DefaultConfigs(object):
    # 00001.string parameters
    train_data = "/home/xkjs/PycharmProjects/yanxin-image-classification/data_yanxin/train/"
    test_data = "/home/xkjs/PycharmProjects/yanxin-image-classification/data_yanxin/test/"
    val_data = "/home/xkjs/PycharmProjects/yanxin-image-classification/data_yanxin/val/"
    model_name = "resnet101"
    weights = "./checkpoints/"
    best_models = weights + "best_model/"
    submit = "./submit/"
    logs = "./logs/"
    gpus = "1"
    augmen_level = "medium"  # "light","hard","hard2"

    # 00002.numeric parameters
    epochs = 600
    batch_size = 32
    img_height = 384
    img_weight = 384
    num_classes = 7
    seed = 888
    lr = 1e-4
    lr_decay = 1e-4
    weight_decay = 1e-4


config = DefaultConfigs()
