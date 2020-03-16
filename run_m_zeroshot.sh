#!/bin/bash

# middle size
# zero-shot

gpu_id=1

output_dir="output/m_zeroshot"
config_train=config_train_zeroshot

config_model=configs.config_model_345M
pretrained_model_dir="../gpt-2/models/345M"
pretrain_checkpoint="../gpt-2/models/345M/model.ckpt"

mkdir -p ${output_dir}
cp $0 ${output_dir}
cp configs/${config_train}.py ${output_dir}

# input: x1xx2
CUDA_VISIBLE_DEVICES=${gpu_id}  \
python3 rewriting_main.py  \
  --config_model=${config_model} \
  --pretrained_model_dir=${pretrained_model_dir} \
  --pretrain_checkpoint=${pretrain_checkpoint} \
  --config_train=configs.${config_train} \
  --output_dir=${output_dir} \
  --do_test \
  --finetune

