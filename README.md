# Benchmarking Japanese Sentence Segmentation Tools

## Requirements

- Python: 3.9

## Installation

```shell
pipenv install
```

## Benchmarking

```shell
pipenv run run.py
```

## Benchmarking

- Data:
  - [cc100](./data/cc100.jsonl): 15 documents sampled from CC-100.
  - [emoji](./data/emoji.jsonl)
    - Example input: "もちろん大丈夫です👍よろしくお願いします。"
    - Example output: ["もちろん大丈夫です👍", "よろしくお願いします。"]
  - [kaomoji](./data/kaomoji.jsonl)
    - Example input: "いいですよ^^よろしくお願いします。"
    - Example output: ["いいですよ^^", "よろしくお願いします。"]
  - [title_w_period](./data/title_w_period.jsonl)
    - Example input: "モーニング娘。は日本のアイドルグループです。"
    - Example output: ["モーニング娘。は日本のアイドルグループです。"]
  - [new_line](./data/new_line.jsonl)
    - Example input: "時間は現在調整中ですので決まり次第\nご連絡差し上げます。"
    - Example output" ["時間は現在調整中ですので決まり次第\nご連絡差し上げます。"]
- Evaluation metric: F1

| Tool                                                 | cc100 | emoji | kaomoji | title_w_period    | new_line |
|------------------------------------------------------|-------|-------|---------|-------------------|----------|
| [sengiri](https://github.com/ikegami-yukino/sengiri) | 66.7  | 0.0   | 0.0     | 48.0              | 29.6     |
| [bunkai](https://github.com/megagonlabs/bunkai)      | 83.3  | 91.4  | 47.1    | 0.0               | 29.6     |
| [ginza](https://github.com/megagonlabs/ginza)        | 73.4  | 62.5  | 64.9    | 76.2              | 63.6     |
