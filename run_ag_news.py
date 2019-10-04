# coding=utf-8
from main import main


if __name__ == "__main__":

    model_name = "BertOrigin"
    label_list = ['1', '2', '3', '4']
    data_dir = "/home/liuyang/TextClassification/dataset/ag_news/"
    output_dir = ".ag_news_output/"
    cache_dir = ".ag_news_cache"
    log_dir = ".ag_news_log/"

    # model_times = "model_1/"   # 第几次保存的模型，主要是用来获取最佳结果

    # bert-base
    bert_vocab_file = "/home/liuyang/bert/bert-base-uncased-vocab.txt"
    bert_model_dir = "/home/liuyang/bert/bert/uncased_L-12_H-768_A-12"

    # # bert-large
    # bert_vocab_file = "/home/liuyang/bert/bert-large-uncased-vocab.txt"
    # bert_model_dir = "/home/liuyang/bert/bert/uncased_L-24_H-1024_A-16"

    if model_name == "BertOrigin":
        from BertOrigin import args

    elif model_name == "BertCNN":
        from BertCNN import args

    elif model_name == "BertATT":
        from BertATT import args

    elif model_name == "BertRCNN":
        from BertRCNN import args

    elif model_name == "BertCNNPlus":
        from BertCNNPlus import args

    config = args.get_args(data_dir, output_dir, cache_dir,
                           bert_vocab_file, bert_model_dir, log_dir)

    main(config, config.save_name, label_list)
