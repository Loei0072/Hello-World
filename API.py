# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:18:37 2023

@author: Loei
"""
import nltk
import openai
import json
import os
openai.api_key = "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" #这个API一共有4745个token长度。

with open(os.path.expanduser('D:/111/aaa.txt'), "r", encoding="utf-8") as f:
    text = f.read()
#将文本分成段落
paragraphs = text.split("\n")

#代码层面导入文本如下
text2 = 'I love you'

#自定义一个翻译函数：
def translator(text, target_language="zh"):
    response = openai.Completion.create(
        engine="text-davinci-002", #text-davinct-002指的API的一个模型，这个模型里3745作为上下文标记长度。
        prompt=f"translate '{text}' into {target_language}",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8,)

    translations = response.choices[0].text
    return translations.strip()
target_language = "zh"


#逐个段落进行翻译
translations22 = []
for i in text2:
    x = translator(i,target_language)
    translations22.append(x)

#将翻译结果合并为一个字符串
translated_text = "\n".join(translations22)

#print(f"Original text: {text}")
print(f"翻译文本: {translated_text}")


#使用翻译函数进行翻译工作，翻译模式为zh中文
translation = translator(text, target_language)

#print(f"Original text: {text}")
print(f"翻译文本: {translation}")

with open("D:/translated_text.txt", "w", encoding="utf-8") as f:
    f.write(translation)

###############################################################################
import openai
import os

openai.api_key = "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"

with open(os.path.expanduser('D:/111/BBB.txt'), "r", encoding="utf-8") as f:
    text = f.read()

translated_text = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"翻译: {text}\n成为: 中文",
    temperature=0.8,
    max_tokens=24,
    n = 1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

print(translated_text.choices[0].text.strip())



