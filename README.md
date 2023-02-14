# Comparison of Japanese Sentence Segmentation Tools

## Requirements

- Python: 3.9

## Installation

```shell
pipenv install
```

## Run

```shell
pipenv run run.py
```

## Benchmark

- Data:
  - [wikipedia](./data/wikipedia.jsonl): 15 documents sampled from Japanese Wikipedia.
  - [cc100](./data/cc100.jsonl): 15 documents sampled from CC-100 (web text).
  - [emoji](./data/emoji.jsonl)
    - Example input: `"もちろん大丈夫です👍よろしくお願いします。"`
    - Expected output: `["もちろん大丈夫です👍", "よろしくお願いします。"]`
  - [kaomoji](./data/kaomoji.jsonl)
    - Example input: `"いいですよ^^よろしくお願いします。"`
    - Expected output: `["いいですよ^^", "よろしくお願いします。"]`
  - [title_w_period](./data/title_w_period.jsonl)
    - Example input: `"モーニング娘。は日本のアイドルグループです。"`
    - Expected output: `["モーニング娘。は日本のアイドルグループです。"]`
  - [new_line](./data/new_line.jsonl)
    - Example input: `"時間は現在調整中ですので決まり次第\nご連絡差し上げます。"`
    - Expected output: `["時間は現在調整中ですので決まり次第\nご連絡差し上げます。"]`
- Evaluation metric: F1

| Tool                                                 | wikipedia | cc100   | emoji | kaomoji | title_w_period | new_line |
|------------------------------------------------------|-----------|---------|-------|---------|----------------|----------|
| [pysbd](https://github.com/nipunsadvilkar/pySBD)     | 100.0     | 85.5    | 0.0   | 0.0     | 0.0            | 44.4     |
| [rhoknp](https://github.com/ku-nlp/rhoknp)           | 100.0     | 88.4    | 0.0   | 0.0     | 0.0            | 44.4     |
| [hasami](https://github.com/mkartawijaya/hasami)     | 94.8      | 86.2    | 0.0   | 0.0     | 63.6           | 44.4     |
| [sengiri](https://github.com/ikegami-yukino/sengiri) | 55.7      | 68.1    | 12.9  | 0.0     | 48.0           | 44.4     |
| [bunkai](https://github.com/megagonlabs/bunkai)      | 93.7      | 83.7    | 100.0 | 66.7    | 0.0            | 81.8     |
| [ginza](https://github.com/megagonlabs/ginza)        | 86.5      | 74.8    | 54.1  | 64.9    | 76.2           | 81.8     |
