
# -*- coding: utf-8 -*-
# Time    : 2025/8/25 10:18
# File    : Testing05.py
# Software: PyCharm
import  torch
import  torch.nn  as nn
if __name__ == '__main__':
    ####### Binary Cross-entropy
    logits = torch.tensor([0.8])
    probas = torch.sigmoid(logits)
    target = torch.tensor([1.0])
    bce_loss_fn = nn.BCELoss()
    # BCELoss：聚焦 “每个标签独立判断”，适用于二分类或多标签场景，需配合 sigmoid 使用；
    bce_logits_loss_fn = nn.BCEWithLogitsLoss()
    print(f'BCE (w Probas): {bce_loss_fn(probas, target):.4f}')
    print(f'BCE (w Logits): {bce_logits_loss_fn(logits, target):.4f}')

    ####### Categorical Cross-entropy
    logits = torch.tensor([[1.5, 0.8, 2.1]])
    probas = torch.softmax(logits, dim=1)
    target = torch.tensor([2])
    cce_loss_fn = nn.NLLLoss()
    cce_logits_loss_fn = nn.CrossEntropyLoss()
    # CrossEntropyLoss：聚焦 “多个互斥类别中选一个”，适用于单标签多分类，内置 softmax 无需手动激活。

    print(f'CCE (w Probas): {cce_logits_loss_fn(logits, target):.4f}')
    print(f'CCE (w Logits): {cce_loss_fn(torch.log(probas), target):.4f}')

