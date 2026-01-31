#!/bin/bash
vllm serve --model microsoft/Phi-4-mini-instruct --port 1207
# By default, the model path refers to Hugging Face model repository path
# The HTTP port 1207 is exposed on Runpod's instance settings. 
