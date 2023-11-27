import argparse
import os
from math import log10
from datetime import datetime

import numpy as np
import pandas as pd
import torch
import torchvision.utils as utils
from torch.autograd import Variable
from torch.utils.data import DataLoader
from tqdm import tqdm
import lpips  # Make sure to install this package

import pytorch_ssim
from data_utils import TestDatasetFromFolder, display_transform
from model import Generator

parser = argparse.ArgumentParser(description='Test Benchmark Datasets')
parser.add_argument('--upscale_factor', default=4, type=int, help='super resolution upscale factor')
parser.add_argument('--model_name', default='netG_epoch_4_100.pth', type=str, help='generator model epoch name')
parser.add_argument('--dataset_name', default='unsplash', type=str, help='dataset folder name')
parser.add_argument('--model_runtime', default='2023-11-26_01-42-39', type=str, help='model runtimes folder name')
opt = parser.parse_args()

UPSCALE_FACTOR = opt.upscale_factor
MODEL_NAME = opt.model_name
DATASET_FOLDER = opt.dataset_name
MODEL_RUNTIME = opt.model_runtime

results = {'Set5': {'psnr': [], 'ssim': [], 'lpips': []},
           'Set14': {'psnr': [], 'ssim': [], 'lpips': []},
           'BSD100': {'psnr': [], 'ssim': [], 'lpips': []},
           'Urban100': {'psnr': [], 'ssim': [], 'lpips': []},
           'SunHays80': {'psnr': [], 'ssim': [], 'lpips': []}}

model = Generator(UPSCALE_FACTOR).eval()
if torch.cuda.is_available():
    model = model.cuda()

model.load_state_dict(torch.load('models/epochs/' + DATASET_FOLDER + '/' + MODEL_RUNTIME + '/' + MODEL_NAME))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

lpips_loss_fn = lpips.LPIPS(net='alex').cuda() if torch.cuda.is_available() else lpips.LPIPS(net='alex')

test_set = TestDatasetFromFolder('data/external/test', upscale_factor=UPSCALE_FACTOR)
test_loader = DataLoader(dataset=test_set, num_workers=4, batch_size=1, shuffle=False)
test_bar = tqdm(test_loader, desc='[testing benchmark datasets]')

current_datetime = datetime.now()
datetime_folder = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") 

out_path = f'data/processed/benchmark_results/{datetime_folder}/SRF_' + str(UPSCALE_FACTOR) + '/'
if not os.path.exists(out_path):
    os.makedirs(out_path)

for image_name, lr_image, hr_restore_img, hr_image in test_bar:
    image_name = image_name[0]
    with torch.no_grad():
        lr_image = lr_image.to(device)
        hr_image = hr_image.to(device)
    # lr_image = Variable(lr_image, volatile=True)
    # hr_image = Variable(hr_image, volatile=True)
    # if torch.cuda.is_available():
    #     lr_image = lr_image.cuda()
    #     hr_image = hr_image.cuda()

    sr_image = model(lr_image)

    # Calculate PSNR
    mse = ((hr_image - sr_image) ** 2).data.mean()
    psnr = 10 * log10(1 / mse)

    # Calculate SSIM
    ssim = pytorch_ssim.ssim(sr_image, hr_image).item()

    # Calculate LPIPS
    lpips_tensor = lpips_loss_fn(hr_image, sr_image)
    lpips_value = lpips_tensor.mean().item()

    # Save the image with metrics in the filename
    test_images = torch.stack(
        [display_transform()(hr_restore_img.squeeze(0)),
         display_transform()(hr_image.data.cpu().squeeze(0)),
         display_transform()(sr_image.data.cpu().squeeze(0))])
    image = utils.make_grid(test_images, nrow=3, padding=5)
    filename = (out_path + image_name.split('.')[0] +
                f'_psnr_{psnr:.4f}_ssim_{ssim:.4f}_lpips_{lpips_value:.4f}.' +
                image_name.split('.')[-1])
    utils.save_image(image, filename, padding=5)

    # Save psnr, ssim, and lpips
    results[image_name.split('_')[0]]['psnr'].append(psnr)
    results[image_name.split('_')[0]]['ssim'].append(ssim)
    results[image_name.split('_')[0]]['lpips'].append(lpips_value)

out_path = f'data/processed/statistics/{datetime_folder}/'
saved_results = {'psnr': [], 'ssim': [], 'lpips': []}
for item in results.values():
    psnr = np.array(item['psnr'])
    ssim = np.array(item['ssim'])
    lpips_res = np.array(item['lpips'])

    if (len(psnr) == 0) or (len(ssim) == 0) or (len(lpips_res) == 0):
        psnr = 'No data'
        ssim = 'No data'
        lpips_res = 'No data'
    else:
        psnr = psnr.mean()
        ssim = ssim.mean()
        lpips_res = lpips_res.mean()

    saved_results['psnr'].append(psnr)
    saved_results['ssim'].append(ssim)
    saved_results['lpips'].append(lpips_res)

data_frame = pd.DataFrame(saved_results, results.keys())
data_frame.to_csv(out_path + 'srf_' + str(UPSCALE_FACTOR) + '_test_results.csv', index_label='DataSet')
