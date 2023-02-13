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

## Result

- MacBook Pro (15-inch, 2018)
  - Processor: 2.6 GHz 6-Core Intel Core i7
  - Memory: 32 GB 2400 MHz DDR4

| Tool    | F1    | Elapsed time |
|---------|-------|--------------|
| sengiri | 58.5  | 0.08         |
| bunkai  | 69.6  | 0.16         |
| ginza   | 100.0 | 0.48         |
