<!-- https://github.com/kyechan99/capsule-render -->
<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=300&&section=header&text=HI%20THERE!&fontSize=90&fontAlign=50&fontAlignY=30&desc=I%20am%20SLBY8!&descAlign=50&descSize=30&descAlignY=60&animation=twinkling">
</p>
 
<!-- https://github.com/DenverCoder1/readme-typing-svg -->
<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=25&pause=1000&center=true&vCenter=true&random=false&width=600&lines=Welcome+to+my+GitHub+profile+page!" />
</p>
 
<!-- https://github.com/badges/shields -->
<p align="center">
<a href="https://github.com/SLBY8/LM-DETR"><img src="https://img.shields.io/badge/Python-3.10+-blue?" /></a>
<a href="https://github.com/SLBY8/LM-DETR"><img src="https://img.shields.io/badge/Pytorch-2.3+-red?base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAB+FBMVEUAAABqMy7wroeAUEvuso1vOTNwOzbxt5WKYFyniYm/qKLe3s1sNTBsNjGQVkhvODR6Rj7ip4XutZOCU07wtpXxupnst5eKXFmJXlrwu5qKbWryv6Hzx62gfXuwiYb44tNvODNWNSuKUUbwr4iKUkXwsImCVUZ3Qjt5UkN3QjvwsYtGLSfws454SERyPzp4RD/ws4/ws49xPzvvtI/xtJBPODJ7S0Z7SkXWnIFiTkbVnIGCU0/ps5TxvaDwvqGSaWWSaGiOaGSTb2uPamXzx7HxyrCjhHrwrYVqMi3wrITuq4RrMy63eF9jPS/Cg2fupoLqqIHopoDfn3rXlnXAfmSwcluNWkfioHzmkXrihXXccW2zdFypbFehZlKFWUVzSTlwSTh7QThuNS9VMyjto4HlpH7ionzjh3bXmXXOkG/Mi22tb1l/UUB9TT15TDxtRzZcNytZNypRMCVPLiTrnn/cnXnZm3fZmHbhgXTddG7IiGvMgGrPY2S2gGK+e2K1dl7CXV6uel28WlqocFika1WnalWdbFOaYk6dYE6SYUySVkaQVUaIVkSCV0OHVEOJTkF4UD2CRTxmQTJaLCZXKyVNKyJJJR9EIx0+IRrTknLffXLabWzZbGzFi2u5emGucFqicVeXaFCSXUp1STpdOy1hNyxdMilXMCfoEl0hAAAAR3RSTlMA/vqLn+7meVAWDgX59/X13LSGgoF7c2hdVlJQLSklEff18/Ly7+zs5ubi4djX1szHxMG5uLSjnZaJhn1pXldEPT05Ny4nGbaUVn8AAAIPSURBVDjLvdNFlxpBEMDxBgLsknX3jbu7e1I1wzC4OyzusO7u7nFPvmYGwr4HWZJc8vI71at/H/rQTf65g3/pReclTX/qj0rKL175fW4ViBCRd0HQWjC/uFGCWaU3i/f3hyLMIXq873alKJVma3oqL8rvTw7Ns+qeALOCuMIEetTsvPBpbpdUsBSk0SMjdGag2ApJzgEBC4qxJdtQJtJDNtuYAjSCvfpMfKeMUslkOp3MoQTwxNLTup4uuyVuSfcqPoTeUfbIicN2JqoDsEW1p9zh6CowIeDXEXIfaMNasHtr+fb1nWXG7fEmGXvT2e2ZlCq4ZqChmVwC46Ar+DYe2dndjAzHk6nEsGx7d+NTPNDvGvTBVXKGMo3ie3/K8n3jm0WT6PK7NTNbm1/Nya4QjvbBOXIZjOPoVK4vmq1mzdwSUKtzGq2VWYwpnTjug2vkAdADiFa12z45EZZ5AVRfwhOTnxPdVsQBit9MiJivkqJ0Vv0x5vig1FOU3jPtcEz7Z7mlil9LOC33TiOiUwEAL139rEvNDQontzpZ95z8VI2IC8BRar16rSI9LXCrarKnWIhogTwWRGHOo2jgoRnA4Ms0ymgA0CKvgeS4y5sC6DAZ5UB19PbJAaZ4ApKn/gjNnXj1xmR63ct1+lg9+UVbJXDknZ1y4FS2Ffgytcch62hN4f/T3lhzgFPV2E7+qx9xsqq+PsbsOwAAAABJRU5ErkJggg==" /></a>
<a href="https://github.com/Intellindust-AI-Lab/DFINE"><img src="https://img.shields.io/badge/DFINE-2024-pink?" /></a>
<a href="https://github.com/VisDrone/VisDrone-Dataset"><img src="https://img.shields.io/badge/VisDrone-2019-green?"  /></a>
<!-- https://github.com/antonkomarev/github-profile-views-counter -->
</p>

# Environment
	conda create -n CuReFormer
	conda activate CuReFormer
	pip install -r requirements.txt
# Training
	CUDA_VISIBLE_DEVICES=0 python train.py
# Test
	python train.py -c configs/dfine/dfine_hgnetv2_s_custom.yml --test-only -r best_stg2.pth
# Aknowledgement
	CuReFormer is built upon DFINE https://github.com/Peterande/D-FINE.
	This work is based on three public datasets: VisDrone DOTA and DIOR.

<!-- https://github.com/kyechan99/capsule-render -->
<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=300&&section=footer&text=THE%20END!&fontSize=90&fontAlign=50&fontAlignY=70&desc=Hope%20your%20program%20is%20bug-free!&descAlign=50&descSize=30&descAlignY=40&animation=twinkling">
</p>


