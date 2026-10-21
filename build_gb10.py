import os, sys
sys.path.insert(0, "/root/Strata")
os.chdir("/root/Strata")
os.environ["STRATA_NVCC"] = "/usr/local/cuda/bin/nvcc"
import setup
llama = setup.get_llama_cpp()
setup.build_engine({"arch": 121, "archs": [121], "name": "NVIDIA GB10"}, "none", True, llama, toolkit=13)
print("BUILD_DONE")
