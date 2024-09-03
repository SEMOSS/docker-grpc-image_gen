# gRPC Server

This is a gRPC server created to run in a Docker container.
gRPC is a high-performance, open-source universal RPC framework. It is designed to be efficient, fast, and language-independent. gRPC is based on HTTP/2, uses Protocol Buffers as the interface definition language.

## Local Installation (Assumes Windows w/ Anaconda)
Running PyTorch with CUDA on Windows can be a bit tricky and the steps may vary based on your system configuration. The following steps should help you get started.

- conda activate base
- conda create --name your_environment_name python=3.11
- conda activate your_environment_name
- conda install cuda --channel nvidia/label/cuda-12.4.0
- pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
- conda env update -f environment.yml
- pip install -r requirements.txt

## Downloading Model Files
- The model files for PixArt-alpha/PixArt-XL-2-1024-MS can be downloaded locally using the `utils/dl_model_files.py` script. The script will download the model files to the `models_files` directory.
- This prevents the Docker container from having to download the model files each time it starts up.
- I can't push the model files to GitHub because they are too large so you will need to download them locally before building the Docker container.

## gRPC
- The gRPC server is defined in the `server/gRPC` directory.
- The image_gen_pb2_grpc.py and image_gen_pb2.py files are generated from the image_gen.proto file.
- If you make changes to the image_gen.proto file, you will need to regenerate the image_gen_pb2_grpc.py and image_gen_pb2.py files.
- You will also need to make sure that these changes are reflected in the image_gen.proto file on the client side (CFG).

## Generate the gRPC code
```bash
cd server/gRPC
```
 ```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_gen.proto
```

## Port 
- Server runs on port `localhost:50051` unless otherwise specified.

## Docker
```bash
docker build -t grpc-imagegen .
```

```bash
docker run --gpus all -p 50051:50051 --name grpc-imagegen grpc-imagegen
```

## PyTorch/CUDA
- You can test your local PyTorch/CUDA installation by using the `utils/torch_test.ipynb` notebook.

## Testing
- You can test the ImageGen class directly using the `app/test/test_local_image_dl.py` script.