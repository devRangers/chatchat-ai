# chatchat-ai
This is an implementation of a harmful text detection model designed to ensure a clean and safe environment in a chat service. The model aims to identify and filter out harmful, offensive, or inappropriate messages, contributing to a positive user experience.

## Environment Setup

We have experimented with the implementation in the following environment:

- **Operating System**: Ubuntu 20.04.5 LTS
- **Python Version**: 3.8.10
- **PyTorch Version**: 2.0.1+cu117
- **CUDA Version**: 12.0
- **GPU**: NVIDIA GeForce RTX 3090
```bash
pip install -r requirements.txt
```

## Dataset
Datasets we used are as follows:
|           Dataset |                                                                            Download |              Comment |
|:-----------------:|:-----------------------------------------------------------------------------------:|----------------------|
| Korean HateSpeech Dataset       | [Link](https://github.com/kocohub/korean-hate-speech)                          | -       |

For more details, please refer to data preparation.

## Contact for Issues
Byeolhee Kim, [kimbyeolhee0216@gmail.com](kimbyeolhee0216@gmail.com) 